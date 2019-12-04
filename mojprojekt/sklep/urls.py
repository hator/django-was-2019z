from django.urls import path

from . import views

urlpatterns = [
    path("products/", views.product_list),
    path("product/<int:product_id>", views.product_details),
    path("", views.index)
]
