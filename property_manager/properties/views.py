from django.core import exceptions
from django.shortcuts import render

from rest_framework import generics as api_views, permissions

from .models import SingleProperty
from .serializers import PropertyforListSerializer, PropertyFullSerializer


class PropertyListAndCreateView(api_views.ListCreateAPIView):
    queryset = SingleProperty.objects.all()
    permission_classes = (
        permissions.IsAuthenticated,
    )

    list_serializer_class = PropertyforListSerializer
    create_serializer_class = PropertyFullSerializer

    def get_queryset(self):
        queryset =  super().get_queryset()
        queryset = queryset.filter(owner_id=self.request.user.id)
        # queryset = self.__apply_query_filters(queryset)
        return queryset
    
    def get_serializer_class(self):
        if self.request.method.lower() == 'post':
            return self.create_serializer_class
        return self.list_serializer_class

class PropertyDetailsAndUpdateView(api_views.RetrieveUpdateAPIView):
    queryset = SingleProperty.objects.all()
    serializer_class = PropertyFullSerializer
    permission_classes = (
        permissions.IsAuthenticated,
    )

    # def get_object(self):
    #     obj = super().get_object()
    #     if obj.owner != self.request.user:
    #         raise exceptions.PermissionDenied
    #     return obj