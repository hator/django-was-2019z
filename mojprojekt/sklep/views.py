from django.http import HttpResponse
from django.shortcuts import render


products = [
    {
        "name": "Film",
        "price": 100,
        "id": 1,
        "description": "Mam nowy fantastyczny film - \"Śmierć w Wenecji\". Dobre, nie?",
        "weight": "300 grams"
    },
    {
        "name": "Ksiazka", "price": 30, "id": 2,
        "description": "Jakaś generyczna książka o coachingu i challengowaniu????",
        "weight": "1 kg"
    },
    {
        "name": "Plyta", "price": 60, "id": 3,
        "description": "Metal subtelnie napieprza z głośników...",
        "weight": "100 grams"
    },
]


def product_list(request):
    return render(
        request,
        "sklep/list.html",
        {"products": products}
    )


def product_details(request, id):
    product = None
    # Find product that has the given ID
    for p in products:
        if p['id'] == id:
            product = p

    return render(
        request,
        "sklep/details.html",
        {"product": product}
    )


def index(request, tekst):
    return render(
        request,
        "sklep/glowna.html",
        {"imie_klienta": tekst}
    )

