from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, DocumentType, Country, City, Rol
# Register your models here.


class DocumentTypeAdmin(admin.ModelAdmin):
    pass


class CountryAdmin(admin.ModelAdmin):
    pass


class CityAdmin(admin.ModelAdmin):
    pass


class RolAdmin(admin.ModelAdmin):
    pass


admin.site.register(User, UserAdmin)
admin.site.register(DocumentType, DocumentTypeAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(Rol, RolAdmin)
admin.site.register(City, CityAdmin)
