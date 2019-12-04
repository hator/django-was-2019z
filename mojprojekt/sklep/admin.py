from django.contrib import admin
from .models import Product, Order, OrderedProduct

admin.site.register(Product)
admin.site.register(Order)

admin.site.register(OrderedProduct)
# Register your models here.
