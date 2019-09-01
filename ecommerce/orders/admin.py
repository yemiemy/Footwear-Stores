from django.contrib import admin
from .models import Order, Payment, Coupon
# Register your models here.
class OrderAdmin(admin.ModelAdmin):
	list_display = ['order_id', 'ordered']
admin.site.register(Order, OrderAdmin)
admin.site.register(Payment)
admin.site.register(Coupon)
