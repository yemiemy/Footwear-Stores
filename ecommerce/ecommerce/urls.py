"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from products.views import *
from carts.views import *
from orders import views
from accounts.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('product-detail/<slug>', productDetail, name='productDetail'),
    path('shopping-cart/<int:id>/', remove_from_cart, name='remove_from_cart'),
    path('shopping-cart/', cart, name='cart'),
    path('', include('orders.urls')),
    path('s/', search, name='search'),
    path('men/', men, name='men'),
    path('women/', women, name='women'),
    path('suede/', suede, name='suede'),
    path('grey/', grey, name='grey'),
    path('casual/', casual, name='casual'),
    path('leather/', leather, name='leather'),
    path('green/', green, name='green'),
    path('red/', red, name='red'),
    path('nike/', nike, name='nike'),
    path('adidas/', adidas, name='adidas'),
    path('givenchy/', givenchy, name='givenchy'),
    path('gucci/', gucci, name='gucci'),
    path('slip-ons/', slip_ons, name='slip-ons'),
    path('products-lace-ups/', lace_ups, name='lace-ups'),
    path('products-oxfords/', oxfords, name='oxfords'),
    path('product-black/', black, name='black'),
    path('product-white/', white, name='white'),
    path('product-blue/', blue, name='blue'),
    path('product-orange/', orange, name='orange'),
    path('product-brown/', brown, name='brown'),
    path('product-sandals/', sandals, name='sandals'),
    path('product-boots/', boots, name='boots'),
    path('product-formal/', formal, name='formal'),
    path('product-sport/', sport, name='sport'),
    path('product-female/', female, name='female'),
    path('product-male/', male, name='male'),
    path('accounts/logout/', logout_view, name='auth_logout'),
    path('accounts/login/', login_view, name='auth_login'),
    path('accounts/register/', registration_view, name='auth_register'),
    path('accounts/activate/<activation_key>/', activation_view, name='activation_view' )

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)