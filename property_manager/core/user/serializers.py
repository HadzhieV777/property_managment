from core.user.models import AppUser
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = AppUser
        fields = ['id', 'email', 'phone_number', 'date_of_birth', 'is_active', 'created', 'updated']
 

#    https://dev.to/koladev/django-rest-authentication-cmh
#    https://jpmeyer.dev/blog/django-rest-framework-custom-users
#    https://krakensystems.co/blog/2020/custom-users-using-django-rest-framework
#    https://kimmosaaskilahti.fi/blog/2021-04-02-django-custom-user/
#    https://www.remoteinning.com/blog/how-to-use-jwt-authentication-with-django-rest-framework
#    https://hackernoon.com/110percent-complete-jwt-authentication-with-django-and-react-2020-iejq34ta
#    https://rental.turbotenant.com/owners/dashboard