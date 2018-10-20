from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    document_type = models.ForeignKey('DocumentType', on_delete=models.DO_NOTHING, null=True, blank=True)
    identification_number = models.IntegerField(null=True, blank=True)
    born_date = models.DateField(null=True, blank=True)
    born_city = models.ForeignKey('City', on_delete=models.DO_NOTHING, null=True, blank=True)
    rol = models.ForeignKey('Rol', on_delete=models.DO_NOTHING, related_name="user_rol", null=True, blank=True)
    familiar_group = models.IntegerField(null=True, blank=True)
    modified_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.first_name + " " + self.last_name


class DocumentType(models.Model):
    document_type = models.CharField(max_length=200)
    modified_date = models.DateField(auto_now=True)
    modified_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.document_type


class Country(models.Model):
    country_name = models.CharField(max_length=200)
    modified_date = models.DateField(auto_now=True)
    modified_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.country_name


class City(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    city_name = models.CharField(max_length=200)
    modified_date = models.DateField(auto_now=True)
    modified_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.city_name


class Rol(models.Model):
    rol_name = models.CharField(max_length=200)
    modified_date = models.DateField(auto_now=True)
    modified_by = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, related_name="user_modify_by")

    def __str__(self):
        return self.rol_name

