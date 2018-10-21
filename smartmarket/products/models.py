from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class ProductType(models.Model):
    product_type = models.CharField(max_length=200)
    modified_date = models.DateField(auto_now=True)
    modified_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.product_type


class SubProduct(models.Model):
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE)
    sub_product_type = models.CharField(max_length=200)
    modified_date = models.DateField(auto_now=True)
    modified_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.sub_product_type


class BrandProduct(models.Model):
    brand = models.CharField(max_length=200)
    modified_date = models.DateField(auto_now=True)
    modified_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.brand


class MeasureProduct(models.Model):
    unit_measure = models.CharField(max_length=200)
    modified_date = models.DateField(auto_now=True)
    modified_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.unit_measure


class Product(models.Model):
    reference = models.CharField(max_length=200)
    product_type = models.ForeignKey(ProductType, on_delete=models.DO_NOTHING, null=True, blank=True)
    sub_product_type = models.ForeignKey(SubProduct, on_delete=models.DO_NOTHING, null=True, blank=True)
    weight_unit = models.DecimalField(max_digits=20, decimal_places=2)
    unit_measure = models.ForeignKey(MeasureProduct, on_delete=models.DO_NOTHING, null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    modified_date = models.DateField(auto_now=True)
    modified_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.reference + " " + self.product_type + " " + self.sub_product_type + " " + self.weight_unit + " " + self.unit_measure + " " + self.quantity
