from django.db import models


class Product(models.Model):

    def __str__(self):
        return self.name

    name = models.CharField(max_length=100)
    price = models.FloatField(default=0)
    description = models.CharField(max_length=500, default='Brak Opisu')
    weight = models.FloatField(default=0)
