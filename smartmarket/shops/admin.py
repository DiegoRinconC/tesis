from django.contrib import admin
from .models import Shop, BrandShop


class ShopAdmin(admin.ModelAdmin):
    exclude = ('modified_by',)

    def save_model(self, request, obj, form, change):
        obj.modified_by = request.user
        print(request.user)
        super().save_model(request, obj, form, change)


class BrandShopAdmin(admin.ModelAdmin):
    exclude = ('modified_by',)

    def save_model(self, request, obj, form, change):
        obj.modified_by = request.user
        print(request.user)
        super().save_model(request, obj, form, change)


admin.site.register(Shop, ShopAdmin)
admin.site.register(BrandShop, BrandShopAdmin)
