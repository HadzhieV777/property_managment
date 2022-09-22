import re
from rest_framework import serializers

def validate_password_contain_digit(password):
    if not re.findall('\d', password):
        raise serializers.ValidationError("The password must contain at least 1 digit, 0-9.")
        
def validate_password_contain_uppercase_letter(password):
    if not re.findall('[A-Z]', password):
        raise serializers.ValidationError("The password must contain at least 1 uppercase letter, A-Z.")

def validate_password_contain_lowercase_letter(password):
    if not re.findall('[a-z]', password):
        raise serializers.ValidationError("The password must contain at least 1 lowercase letter, a-z.")

def validate_password_contain_symbol(password):
    if not re.findall('[()[\]{}|\\`~!@#$%^&*_\-+=;:\'",<>./?]', password):
        raise serializers.ValidationError("The password must contain at least 1 symbol: " + "()[]{}|\`~!@#$%^&*_-+=;:'\",<>./?")