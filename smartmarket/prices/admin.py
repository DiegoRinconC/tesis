from django.contrib import admin
from .models import Price


class PriceAdmin(admin.ModelAdmin):
    exclude = ('modified_by', )
    list_display = ('product', 'store', 'price', 'modified_by')

    def save_model(self, request, obj, form, change):
        obj.modified_by = request.user
        print(request.user)
        super().save_model(request, obj, form, change)


admin.site.register(Price, PriceAdmin)

