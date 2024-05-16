from django.shortcuts import render, redirect
from .models import Product
from .utils import CartAuthenticatedUser
from django.http import HttpResponse, HttpRequest


# Create your views here.

def index(request):
    context = {
        'products': Product.objects.all()
    }
    return render(request, 'index.html', context=context)


def cart(request):
    if request.user.is_authenticated:
        cart_info = CartAuthenticatedUser(request).get_cart_info()

        context = {
            'order_products': cart_info['order_products'],
            'cart_total_price': cart_info['cart_total_price'],
            'cart_total_quantity': cart_info['cart_total_quantity'],

        }
        return render(request, 'cart.html', context=context)
    else:
        return HttpResponse("Avval tizimga kiring!")


def to_cart(request: HttpRequest, product_id, action):
    if request.user.is_authenticated:
        CartAuthenticatedUser(request, product_id=product_id, action=action)
        page = request.META.get('HTTP_REFERER')
        return redirect(page)

    else:
        return HttpResponse("Avval tizimga kiring!")
