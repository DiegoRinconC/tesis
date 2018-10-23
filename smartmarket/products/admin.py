from django.contrib import admin
from .models import ProductType, SubProduct, BrandProduct, MeasureProduct, Product


class ProductTypeAdmin(admin.ModelAdmin):
    exclude = ('modified_by',)

    def save_model(self, request, obj, form, change):
        obj.modified_by = request.user
        print(request.user)
        super().save_model(request, obj, form, change)


class SubProductAdmin(admin.ModelAdmin):
    exclude = ('modified_by',)

    def save_model(self, request, obj, form, change):
        obj.modified_by = request.user
        print(request.user)
        super().save_model(request, obj, form, change)


class BrandProductAdmin(admin.ModelAdmin):
    exclude = ('modified_by',)

    def save_model(self, request, obj, form, change):
        obj.modified_by = request.user
        print(request.user)
        super().save_model(request, obj, form, change)


class MeasureProductAdmin(admin.ModelAdmin):
    exclude = ('modified_by',)

    def save_model(self, request, obj, form, change):
        obj.modified_by = request.user
        print(request.user)
        super().save_model(request, obj, form, change)


class ProductAdmin(admin.ModelAdmin):
    exclude = ('modified_by',)

    def save_model(self, request, obj, form, change):
        obj.modified_by = request.user
        print(request.user)
        super().save_model(request, obj, form, change)


admin.site.register(ProductType, ProductTypeAdmin)
admin.site.register(SubProduct, SubProductAdmin)
admin.site.register(BrandProduct, BrandProductAdmin)
admin.site.register(MeasureProduct, MeasureProductAdmin)
admin.site.register(Product, ProductAdmin)
