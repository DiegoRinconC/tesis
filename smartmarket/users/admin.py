from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, DocumentType, Country, City, Rol
# Register your models here.


class DocumentTypeAdmin(admin.ModelAdmin):
    exclude = ('modified_by',)

    def save_model(self, request, obj, form, change):
        obj.modified_by = request.user
        print(request.user)
        super().save_model(request, obj, form, change)


class CountryAdmin(admin.ModelAdmin):
    exclude = ('modified_by',)

    def save_model(self, request, obj, form, change):
        obj.modified_by = request.user
        print(request.user)
        super().save_model(request, obj, form, change)


class CityAdmin(admin.ModelAdmin):
    exclude = ('modified_by',)

    def save_model(self, request, obj, form, change):
        obj.modified_by = request.user
        print(request.user)
        super().save_model(request, obj, form, change)


class RolAdmin(admin.ModelAdmin):
    exclude = ('modified_by',)

    def save_model(self, request, obj, form, change):
        obj.modified_by = request.user
        print(request.user)
        super().save_model(request, obj, form, change)


admin.site.register(User, UserAdmin)
admin.site.register(DocumentType, DocumentTypeAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(Rol, RolAdmin)
admin.site.register(City, CityAdmin)
