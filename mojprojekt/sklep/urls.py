from django.urls import path

from . import views

urlpatterns = [
    path("products/", views.product_list),
    path("product/<int:product_id>", views.product_details),
    path("order/", views.order),
    path("order/<int:order_id>", views.order_details),
    path("complaint/", views.complaint),
    path("complaint/<int:complaint_id>", views.complaint_details),
    path("cart/add/", views.add_to_cart),
    path("cart/", views.cart),
    path("", views.index)
]
