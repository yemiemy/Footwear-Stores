from django import forms
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget


PAYMENT_CHOICES = (
	('S','Stripe'),
	('P','PayPal')
	)
class CheckoutForm(forms.Form):
	country = CountryField(blank_label='select country').formfield(widget=CountrySelectWidget(attrs={'class':'form-control'}))
	first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Your first name', 'class':'form-control'}))
	last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Your last name', 'class':'form-control'}))
	street_address = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'1234 Main St', 'class':'form-control'}))
	apartment_address = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'example bus stop, somewhere Rd', 'class':'form-control'}))
	town = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Town / City', 'class':'form-control'}))
	state = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'State / Province', 'class':'form-control'}))
	zip = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Town / City', 'class':'form-control'}))
	email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder':'email address', 'class':'form-control'}))
	tel = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Phone Number ', 'class':'form-control'}))
	same_billing_address = forms.BooleanField(required=False)
	save_info = forms.BooleanField(required=False)
	payment_option = forms.ChoiceField(
		widget=forms.RadioSelect(), choices=PAYMENT_CHOICES
		)

class CouponForm(forms.Form):
	code = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control input-number', 'placeholder':'Your Coupon Code'}))