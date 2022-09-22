from utils.validators import validate_password_contain_digit, validate_password_contain_uppercase_letter, validate_password_contain_lowercase_letter, validate_password_contain_symbol

from django.core import exceptions
from core.user.models import AppUser
from rest_framework import serializers
from django.contrib.auth import password_validation as validators


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = AppUser
        fields = ['id', 'email', 'password', 'phone_number', 'date_of_birth', 'is_active']

    
    def validate(self, data):
        user = AppUser(**data)
        password = data.get('password')
        errors = {}

        # Validate Password 
        validate_password_contain_digit(password)
        validate_password_contain_uppercase_letter(password) 
        validate_password_contain_lowercase_letter(password)
        validate_password_contain_symbol(password)
      
        try:
            validators.validate_password(password, user)
        except exceptions.ValidationError as e:
            errors['password'] = list(e.messages)
        
        if errors:
           raise serializers.ValidationError(errors)
        return super().validate(data)



#    https://dev.to/koladev/django-rest-authentication-cmh
#    https://jpmeyer.dev/blog/django-rest-framework-custom-users
#    https://krakensystems.co/blog/2020/custom-users-using-django-rest-framework
#    https://kimmosaaskilahti.fi/blog/2021-04-02-django-custom-user/
#    https://www.remoteinning.com/blog/how-to-use-jwt-authentication-with-django-rest-framework
#    https://hackernoon.com/110percent-complete-jwt-authentication-with-django-and-react-2020-iejq34ta
#    https://rental.turbotenant.com/owners/dashboard