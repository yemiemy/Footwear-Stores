from django.urls import path
from .views import orders, CheckoutView, PaymentView, add_coupon, add_to_cart

app_name = 'orders'

urlpatterns = [
	path('checkout/', CheckoutView.as_view(), name='checkout'),
	path('payment/<payment_option>/', PaymentView.as_view(), name='payment'),
	path('add-coupon/', add_coupon, name='add-coupon'),
    path('orders/', orders, name='user_orders'),
    # path('ceate-order/', ceate_order, name='ceate-order'),
    path('shopping-cart/<slug>/', add_to_cart, name='add_to_cart'),
]



