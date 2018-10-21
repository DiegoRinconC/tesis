from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class BrandShop(models.Model):
    brand_shop = models.CharField(max_length=200)
    modified_date = models.DateField(auto_now=True)
    modified_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.brand_shop


class Shop(models.Model):
    shop = models.CharField(max_length=200)
    brand_shop = models.ForeignKey(BrandShop, on_delete=models.DO_NOTHING, null=True, blank=True)
    modified_date = models.DateField(auto_now=True)
    modified_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.shop
