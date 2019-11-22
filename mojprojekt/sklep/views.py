from django.http import HttpResponse
from django.shortcuts import render


products = [
    {
        "name": "Film",
        "price": 100,
        "id": 1
    },
    {"name": "Ksiazka", "price": 30, "id": 2},
    {"name": "Plyta", "price": 60, "id": 3},
]


def product_list(request):
    return render(
        request,
        "sklep/list.html",
        {"products": products}
    )


def index(request, tekst):
    return render(
        request,
        "sklep/glowna.html",
        {"imie_klienta": tekst}
    )

