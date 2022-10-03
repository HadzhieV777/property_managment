from utils.validators import validate_password_contain_digit, validate_password_contain_uppercase_letter, validate_password_contain_lowercase_letter, validate_password_contain_symbol
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.password_validation import validate_password as v_passwords

from django.core import exceptions
from core.user.models import AppUser
from rest_framework import serializers
from django.contrib.auth import password_validation as validators


class UserSerializer(serializers.ModelSerializer):
    __doc__ = _(
        """
        Serializer for User model
        """
    )

    class Meta:
        model = AppUser
        fields = ['id', 'email', 'password', 'phone_number', 'date_of_birth', 'is_active']

    
    def validate(self, data):
        if AppUser.objects.filter(email=data['email']).exists():
            raise serializers.ValidationError({'email', ('This email is already taken!')})
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
    
    def create(self, validated_data):
        return AppUser.objects.create_user(validated_data)


class UserPwdChangeSerializer(serializers.Serializer):
    __doc__ = _(
        """
         Serializer for user model password change
        """
    )

    old_password = serializers.CharField(max_length=128, write_only=True, required=True)
    new_password1 = serializers.CharField(max_length=128, write_only=True, required=True)
    new_password2 = serializers.CharField(max_length=128, write_only=True, required=True)

    def validate_old_password(self, value):
        user = self.context['user']
        if not user.check_password(value):
            raise serializers.ValidationError(
                _('Your old password was entered incorrectly. Please enter it again.')
            )
        return value
    
    def validate(self, data):
        if data['new_password1'] != data['new_password2']:
            raise serializers.ValidationError({'new_password2': _("The two password fields didn't match.")})

        validate_password_contain_digit(data['new_password1'])
        validate_password_contain_uppercase_letter(data['new_password1']) 
        validate_password_contain_lowercase_letter(data['new_password1'])
        validate_password_contain_symbol(data['new_password1'])
        v_passwords(data['new_password1'], self.context['user'])
        return data    
    
    def save(self, **kwargs):
        password = self.validated_data['new_password1']
        user = self.context['user']
        user.set_password(password)
        user.save()
        return user





