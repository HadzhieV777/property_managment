from .models import SingleProperty
from rest_framework import serializers


class PropertyforListSerializer(serializers.ModelSerializer):
    class Meta:
        model = SingleProperty
        fields = ('address', 'city', 'type', 'price', 'status')     

class PropertyFullSerializer(serializers.ModelSerializer):
    class Meta:
        model = SingleProperty
        fields = '__all__'
