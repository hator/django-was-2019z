from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from .forms import OrderForm, ComplaintForm
from .models import Product, Order, OrderedProduct, Complaint


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


def index(request):
    return render(
        request,
        "sklep/index.html"
    )


def order(request):
    products_to_order = _get_products_in_cart(request)

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = Order(
                name=form.cleaned_data['name'],
                address=form.cleaned_data['address'],
                delivery=form.cleaned_data['delivery']
            )
            order.save()

            # Dodajemy wszystkie produkty z koszyka do zamowienia
            for product in products_to_order:
                OrderedProduct(
                    product=product,
                    order=order,
                    amount=1
                ).save()

            request.session['cart'] = []    # Czyscimy koszyk

            return HttpResponseRedirect('/order/'+str(order.id))
    else:
        form = OrderForm()

    return render(request, "sklep/order_form.html", {"form": form, "products": products_to_order})


def order_details(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    total_price = order.get_total_price()

    ordered_products = OrderedProduct.objects.filter(order=order)

    return render(request, "sklep/order_details.html",
                  {"total_price": total_price, "ordered_products": ordered_products})


def complaint(request):
    if request.method == "POST":
        form = ComplaintForm(request.POST)
        if form.is_valid():
            complaint = Complaint(name=form.cleaned_data['name'], message=form.cleaned_data['message'])
            complaint.save()
            return HttpResponseRedirect('/complaint/'+str(complaint.id))
    else:
        form = ComplaintForm()
    return render(request, "sklep/complaint_form.html", {"form": form})


def complaint_details(request, complaint_id):
    complaint = get_object_or_404(Complaint, pk=complaint_id)
    return render(request, "sklep/complaint_details.html", {"complaint": complaint})


def add_to_cart(request):
    if request.method == "POST":
        if 'cart' not in request.session:
            request.session['cart'] = []
        request.session['cart'].append(request.POST['item_id'])
        request.session.modified = True

    return HttpResponseRedirect('/cart')


def _get_products_in_cart(request):
    products_in_cart = []
    for item_id in request.session.get('cart', []):
        product = Product.objects.get(pk=item_id)
        products_in_cart.append(product)
    return products_in_cart


def cart(request):
    products_in_cart = _get_products_in_cart(request)
    return render(request, "sklep/cart.html", {"products": products_in_cart})
