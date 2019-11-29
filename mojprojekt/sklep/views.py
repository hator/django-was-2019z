from django.shortcuts import render
from .models import Product


def product_list(request):
    products = Product.objects.order_by('id')
    context = {'products': products}

    return render(
        request,
        "sklep/list.html",
        context
    )


def product_details(request, product_id):
    product = Product.objects.get(id=product_id)
    context = {"product": product}
    return render(
        request,
        "sklep/details.html",
        context
    )


def index(request, tekst):
    return render(
        request,
        "sklep/glowna.html",
        {"imie_klienta": tekst}
    )

