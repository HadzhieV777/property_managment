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
    unit = models.IntegerField()

    city = models.CharField(
        max_length=CITY_MAX_LEN
    )
    zip_code = models.CharField(
        max_length=ZIP_MAX_LEN
    )
    type = models.CharField(
        max_length=TYPE_MAX_LEN
    )
    status = models.CharField(
        max_length=STATUS_MAX_LEN
    )
    bedrooms =models.IntegerField()
    price = models.FloatField()
    baths = models.IntegerField()
    square_feet = models.FloatField()
    year_built = models.IntegerField(null=True, blank=True)
    pets = models.BooleanField()
    need_maintenace = models.BooleanField(null=True, blank=True)
    realtor = models.ForeignKey(UserModel, related_name='realtor', on_delete=models.CASCADE)
    tenant = models.ForeignKey(UserModel, null=True, blank=True, related_name='tenant',  on_delete=models.SET_NULL)
    # documents = models.ForeignKey(SingleDocument, related_name='document', on_delete=models.CASCADE, null=True, blank=True)
