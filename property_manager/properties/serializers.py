from .models import SingleProperty
from rest_framework import serializers


class PropertyforListSerializer(serializers.ModelSerializer):
    class Meta:
        model = SingleProperty
        fields = ('address', 'baths', 'bedrooms', 'city', 'maintenance', 'owner', 'price', 'rented', 'type', 'zip')     

class PropertyFullSerializer(serializers.ModelSerializer):
    class Meta:
        model = SingleProperty
        fields = '__all__'
