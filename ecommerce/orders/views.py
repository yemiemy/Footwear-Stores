import stripe
import time
from django.shortcuts import render,redirect
from django.urls import reverse
from carts.models import Cart, CartItem
#from products.models import Coupon
from accounts.models import UserStripe
from .models import Order, BillingAddress, Payment, Coupon
from django.views.generic import ListView, DetailView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CheckoutForm, CouponForm
from django.contrib import messages
from .utils import id_generator
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from products.models import Product




stripe.api_key = settings.STRIPE_SECRET_KEY
# Create your views here.S
def orders(request):

	context = {}
	template = 'orders/user.html'
	return render(request, template, context)
#require user login**

@login_required
def add_to_cart(request, slug):
	request.session.set_expiry(120000)

	try:
		the_id = request.session['cart_id']
	except:
		new_cart = Cart()
		new_cart.save()
		request.session['cart_id'] = new_cart.id
		the_id = new_cart.id
	cart = Cart.objects.get(id=the_id)
	try:
		product = Product.objects.get(slug=slug)
	except Product.DoesNotExist:
		pass
	except:
		pass

	product_var = [] #product variation
	
	if request.method == 'POST':
		qty = request.POST['qty']
		for item in request.POST:
			key = item
			val = request.POST[key]
			try:
				v = Variation.objects.get(product=product, category__iexact=key, title__iexact=val)
				product_var.append(v)
				print (v)
			except:
				pass
		cart_item = CartItem.objects.create(cart=cart, product=product)
		if len(product_var) > 0:
			cart_item.variations.add(*product_var)
		cart_item.quantity = qty
		cart_item.save()
		new_total = 0.00
		for item in cart.cartitem_set.all():
			line_total = float(item.product.price) * item.quantity
			new_total += line_total
		request.session['items_total'] = cart.cartitem_set.count()
		print(cart.cartitem_set.count())
		cart_item.line_total = line_total
		print(cart_item.line_total)
		cart_item.save()

		try:
			the_id = request.session['cart_id']
			if the_id:
				cart = Cart.objects.get(id=the_id)
				print(cart)
				print('now it works')
			
		except:
			the_id = None
			return redirect(reverse('cart'))
		try:
			new_order = Order.objects.get(cart=cart)
		except Order.DoesNotExist:
			new_order = Order()
			new_order.cart = cart
			new_order.user = request.user
			new_order.order_id = id_generator()
			new_order.save()
		except:
			#work on some error message
			message.warning(request, 'You do not have an active order.')
			return redirect(reverse('cart'))
		#assign address
		#run credit card
		if new_order.status == 'Finished':
			del request.session['cart_id']
			del request.session['items_total']
			return redirect(reverse('cart'))
		
		return redirect(reverse('cart'))


	return redirect(reverse('cart'))


# @login_required
# def ceate_order(request):
	
# 	# context = {}
# 	# template = 'orders/cart.html'
# 	return redirect(reverse('add_to_cart'))




def get_coupon(request, code):
	try:
		coupon = Coupon.objects.get(code=code)
		return coupon
	except ObjectDoesNotExist:
		messages.error(request, 'This coupon does not exist.')
		return redirect('orders:checkout')




def add_coupon(request):
	if request.method == 'POST':
		form = CouponForm(request.POST or None)
		the_id = request.session['cart_id']
		if the_id:
			cart = Cart.objects.get(id=the_id)
		if form.is_valid():
			code = form.cleaned_data.get('code')
			try:
				order = Order.objects.get(cart=cart)
				order.coupon = get_coupon(request, code)
				order.save()
				messages.success(request, 'Successfully added coupon')
				return redirect('orders:checkout')
			except:
				messages.warning(request, 'Coupon was not added successfully')
				return redirect('orders:checkout')
	#TODO: raise error order.get_total()
	return None

class CheckoutView(LoginRequiredMixin, View):
	def get(self, *args, **kwargs):
		form = CheckoutForm()
		the_id = self.request.session['cart_id']
		if the_id:
			cart = Cart.objects.get(id=the_id)	

		order = Order.objects.get(cart=cart)

		context = {
			'form':form,
			'couponform':CouponForm(),
			'cart':cart,
			'order':order 

		}
		return render(self.request, 'orders/checkout.html', context)

	def post(self, *args, **kwargs):
		form = CheckoutForm(self.request.POST or None)
		the_id = self.request.session['cart_id']
		if the_id:
			cart = Cart.objects.get(id=the_id)	

		order = Order.objects.get(cart=cart)
		print('well, bus stop')
		if form.is_valid():
			country = form.cleaned_data.get('country')
			first_name = form.cleaned_data.get('first_name')
			last_name = form.cleaned_data.get('last_name')
			street_address = form.cleaned_data.get('street_address')
			apartment_address = form.cleaned_data.get('apartment_address')
			town = form.cleaned_data.get('town')
			state = form.cleaned_data.get('state')
			zip = form.cleaned_data.get('zip')
			email = form.cleaned_data.get('email')
			tel = form.cleaned_data.get('tel')
			#TODO:add functionality for these fields
			# same_billing_address = form.cleaned_data('same_billing_address')
			# save_info = form.cleaned_data('save_info')
			payment_option = form.cleaned_data.get('payment_option')
			print(payment_option)
			billing_address = BillingAddress(
				user = self.request.user,
				country = country,
				first_name = first_name,
				last_name = last_name,
				street_address =street_address, 
				apartment_address = apartment_address,
				town = town,
				state = state, 
				zip = zip,
				email = email,
				tel = tel
			)
			print('the form is valid')
			billing_address.save()
			order.billing_address = billing_address
			order.save()
			#TODO: add redirect to the payment option
			if payment_option == 'S':
				print('it got here')
				return redirect('orders:payment', payment_option='stripe')
			elif payment_option == 'P':
				return redirect('orders:payment', payment_option='stripe')
			else:
				messages.error(self.request, 'Invalid payment option selected.')
				return redirect('orders:checkout')
		# except:
		# 	#work on some error message
		# 	messages.warning(self.request, 'You do not have an active order.')
		# 	return redirect('orders:checkout')
		return render(self.request, 'orders/checkout.html',{'form':form})
		#assign address
		#run credit card






class PaymentView(LoginRequiredMixin, View):
	def get(self, *args, **kwargs):
		#order
		the_id = self.request.session['cart_id']
		cart = Cart.objects.get(id=the_id)
		new_order = Order.objects.get(cart=cart)
		if new_order.billing_address:
			context = {
				'cart':cart,
				'order':new_order
			}
			return render(self.request, 'orders/payment.html', context)
		else:
			messages.warning(self.request, 'You have not added a billing address')
			return redirect('oreders:checkout')

	def post(self, *args, **kwargs):
		try:
			the_id = self.request.session['cart_id']
			if the_id:
				cart = Cart.objects.get(id=the_id)
				print(cart)
			
		except:
			the_id = None
			return redirect(reverse('cart'))
		try:
			new_order = Order.objects.get(cart=cart)
			print(int(new_order.cart.total))
		except Order.DoesNotExist:
			messages.warning(self.request, 'You do not have an active order.')
		token = self.request.POST.get('stripeToken')
		print(token)
		amount = int(new_order.get_total())
		print(amount)

		try:
			charge = stripe.Charge.create(
				amount=amount,
				currency="usd",
				source=token # obtained with Stripe.js
			)

			#create  the payment

			payment = Payment()
			payment.stripe_charge_id = charge['id']
			payment.user = self.request.user
			payment.amount = amount
			print(payment.amount)
			payment.save()

			#assign payment to the order
			new_order.final_total = amount
			new_order.payment = payment
			new_order.ordered = True
			print(new_order.ordered)
			new_order.save()
			if new_order.ordered :
				del self.request.session['cart_id']
				del self.request.session['items_total']
				new_order.save()
			# Use Stripe's library to make requests...
			messages.success(self.request, 'Your order was successful')
			return redirect('/')
		except stripe.error.CardError as e:
			# Since it's a decline, stripe.error.CardError will be caught
			body = e.json_body
			err  = body.get('error', {})
			messages.error(self.request, f"{err.get('message')}")
			return redirect('/')
		except stripe.error.RateLimitError as e:
			# Too many requests made to the API too quickly
			messages.error(self.request, "Rate Limit Error")
			return redirect('/')

		except stripe.error.InvalidRequestError as e:
			# Invalid parameters were supplied to Stripe's API
			messages.error(self.request, "Invalid Parameters")
			return redirect('/')

		except stripe.error.AuthenticationError as e:
			# Authentication with Stripe's API failed
			# (maybe you changed API keys recently)
			messages.error(self.request, "Not authenticated")
			return redirect('/')

		except stripe.error.APIConnectionError as e:
			# Network communication with Stripe failed
			messages.error(self.request, "Network error")
			return redirect('/')

		except stripe.error.StripeError as e:
			# Display a very generic error to the user, and maybe send
			# yourself an email
			messages.error(self.request, "Something went wrong. You were not charged. Please try again!")
			return redirect('/')

		except Exception as e:
			# Send an email to myself
			messages.error(self.request, "A serious error occured. We have been notified.")
			return redirect('/')



# class AddCouponView(View):
# 	def post(self, *args, **kwargs):
# 		form = CouponForm(self.request.POST or None)
# 		the_id = self.request.session['cart_id']
# 		if the_id:
# 			cart = Cart.objects.get(id=the_id)
# 		if form.is_valid():
# 			code = form.cleaned_data.get('code')
# 			try:
# 				order = Order.objects.get(cart=cart)
# 				order.coupon = get_coupon(request, code)
# 				order.save()
# 				messages.success(self.request, 'Successfully added coupon')
# 				return redirect('orders:checkout')
# 			except:
# 				messages.warning(self.request, 'Coupon was not added successfully')
# 				return redirect('orders:checkout')