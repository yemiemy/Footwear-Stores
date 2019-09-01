from django.contrib.auth import get_user_model
from django.db import models
from django_countries.fields import CountryField
from carts.models import Cart
# Create your models here.
User = get_user_model()

STATUS_CHOICES = (
	('Started', 'Started'),
	('Abandoned', 'Abandoned'),
	('Finished', 'Finished'),
	)



class Order(models.Model):
	user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
	order_id = models.CharField(max_length=120, default='ABC', unique=True)
	cart = models.ForeignKey(Cart, on_delete = models.CASCADE)
	status = models.CharField(max_length=120, choices=STATUS_CHOICES, default='Started')
	ordered = models.BooleanField(default=False)
	# address**
	coupon = models.ForeignKey('Coupon', on_delete=models.SET_NULL, blank=True,null=True)
	billing_address = models.ForeignKey('BillingAddress', on_delete=models.SET_NULL, blank=True,null=True)
	payment = models.ForeignKey('Payment', on_delete=models.SET_NULL, blank=True,null=True)
	sub_total = models.DecimalField(default=10.99, max_digits=1000, decimal_places=2)
	tax_total = models.DecimalField(default=0.00, max_digits=1000, decimal_places=2)
	final_total = models.DecimalField(default=10.99, max_digits=1000, decimal_places=2)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def get_total(self):

		if self.coupon:
			self.cart.total = self.cart.total - self.coupon.price
		else:
			self.cart.total
		return self.cart.total


	
	def __str__(self):
		return self.order_id

class BillingAddress(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	country = CountryField(multiple=False)
	first_name = models.CharField(max_length=120)
	last_name = models.CharField(max_length=120)
	street_address = models.CharField(max_length=350)
	apartment_address = models.CharField(max_length=350)
	town = models.CharField(max_length=350)
	state = models.CharField(max_length=350)
	zip = models.CharField(max_length=100)
	email = models.CharField(max_length=150)
	tel = models.CharField(max_length=100)	

	def __str__(self):
		return self.user.username


class Payment(models.Model):
    stripe_charge_id = models.CharField(max_length=50)
    user = models.ForeignKey(User,
                             on_delete=models.SET_NULL, blank=True, null=True)
    amount = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

class Coupon(models.Model):
	code = models.CharField(max_length=15)
	price = models.DecimalField(max_digits=1000, decimal_places=2, default=29.99)

	def __str__(self):
		return str(self.price)
