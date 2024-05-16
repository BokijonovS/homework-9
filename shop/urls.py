from django.urls import path
from .views import index, cart, to_cart

urlpatterns = [
    path('', index, name="index"),
    path('cart/', cart, name="cart"),
    path('to-cart/<int:product_id>/<str:action>/', to_cart, name="to_cart"),
]