from django.contrib.auth import get_user_model
from django.db import models
# from documents.models import SingleDocument



UserModel = get_user_model()


class SingleProperty(models.Model):
    ADDRESS_MAX_LEN = 200
    CITY_MAX_LEN = 200
    ZIP_MAX_LEN = 10
    TYPE_MAX_LEN = 200
    STATUS_MAX_LEN = 100

    address = models.CharField(
        max_length=ADDRESS_MAX_LEN
    )

    baths = models.IntegerField()

    bedrooms = models.IntegerField() 

    city = models.CharField(
        max_length=CITY_MAX_LEN
    )
    maintenance = models.BooleanField(
        null=True, 
        blank=True
    )

    owner = models.ForeignKey(UserModel, related_name='realtor', on_delete=models.CASCADE)

    price = models.IntegerField()

    rented = models.BooleanField(
        null=True, 
        blank=True
    )
    
    type = models.CharField(
        max_length=TYPE_MAX_LEN
    )

    zip = models.CharField(
        max_length=ZIP_MAX_LEN
    )

    square_feet = models.FloatField()

    pets = models.BooleanField(
        null=True, 
        blank=True
    )
