from django.contrib import admin
from .models import Product, Order, OrderedProduct, Complaint

admin.site.register(Product)
admin.site.register(Order)

admin.site.register(OrderedProduct)

admin.site.register(Complaint)
# Register your models here.
