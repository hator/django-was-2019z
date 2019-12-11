from django.db import models


class Product(models.Model):

    def __str__(self):
        return self.name

    name = models.CharField(max_length=100)
    price = models.FloatField(default=0)
    description = models.CharField(max_length=500, default='Brak Opisu')
    weight = models.FloatField(default=0)


class Order(models.Model):

    def __str__(self):
        return self.name

    def get_total_price(self):
        total = 0
        ordered_products = OrderedProduct.objects.filter(order=self)
        for ordered_product in ordered_products:
            total += ordered_product.amount * ordered_product.product.price
        return total

    name = models.CharField(max_length=64)
    address = models.CharField(max_length=128)
    delivery = models.CharField(max_length=64)
    ordered_products = models.ManyToManyField("Product", through="OrderedProduct")


class OrderedProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    amount = models.IntegerField(default=1)


class Complaint(models.Model):
    name = models.CharField(max_length=64)
    message = models.CharField(max_length=255)
