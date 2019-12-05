from django.urls import path

from . import views

urlpatterns = [
    path("products/", views.product_list),
    path("product/<int:product_id>", views.product_details),
    path("order/", views.order),
    path("order/<int:order_id>", views.order_details),
    path("", views.index)
]
