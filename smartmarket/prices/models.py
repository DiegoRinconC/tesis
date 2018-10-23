from django.db import models
from products.models import Product
from shops.models import Shop
from users.models import User


class Price(models.Model):
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    store = models.ForeignKey(Shop, on_delete=models.DO_NOTHING)
    price = models.IntegerField()
    modified_date = models.DateField(auto_now=True)
    modified_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.product.reference
