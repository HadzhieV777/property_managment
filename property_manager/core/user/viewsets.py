from rest_framework import status
from rest_framework import viewsets

from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from django.utils.translation import gettext_lazy as _

from core.user.models import AppUser
from core.user.permissions import IsSelf
from core.user.serializers import UserSerializer, UserPwdChangeSerializer


class UserViewSet(viewsets.ModelViewSet):
    __doc__ = _(
        """
        A User ViewSet
        Adding -@action for the password updating, 
        this way you can still handle every aspect of the user model using the ModelViewSet
        and still customize the behavior and serializer utilized on this action
        Also added a custom permission to verify the user is trying to update it's own information.
        """
    )
    permission_classes = (IsAuthenticated, IsSelf)
    serializer_class = UserSerializer

    def get_queryset(self):
        if self.request.user.is_superuser:
            return AppUser.objects.all()
        return AppUser.objects.filter(pk=self.request.user.pk)
    
    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes] 
    
    def get_object(self):
        lookup_field_value = self.kwargs[self.lookup_field]

        obj = AppUser.objects.get(lookup_field_value)
        self.check_object_permissions(self.request, obj)

        return obj

    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=["put"])
    def upassword(self, request, pk=None):
        user = AppUser.objects.get(pk=pk)
        self.check_object_permissions(request, user)

        u = UserPwdChangeSerializer(user, data=request.data, many=False, context={
            "user":request.user
        })
        u.is_valid(raise_exception=True)
        user = u.save()
        return Response(u.data, status=status.HTTP_200_OK)
