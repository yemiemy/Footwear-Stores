from django.shortcuts import render
from .models import Product, ProductImage
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
# Create your views here. 

def home(request):
	products = Product.objects.all()
	feature = ProductImage.objects.filter(featured=True)
	return render(request, 'products/index.html', {'products':products, 'feature':feature})
def contact(request):
	if request.method == 'POST':
		fname = request.POST['fname']
		lname = request.POST['lname']
		email = request.POST['email']
		subject = request.POST['subject']
		message = request.POST['message']
		context = {
			'fname':fname,
			'lname':lname,
			'email':email,
			'message':message,
		}
		body = render_to_string('contact_form.txt', context)
		send_mail('Contact Form: {}'.format(subject), body, settings.DEFAULT_FROM_EMAIL, ['rasholayemi@gmail.com'])
		
	return render(request, 'contact.html', {})
def about(request):
	return render(request, 'about.html', {})
def search(request):
	try:
		q = request.GET.get('q')
	except:
		q = None
	if q:
		products = Product.objects.filter(title__icontains=q)|Product.objects.filter(price__icontains=q)
		template = 'products/results.html'
		context =  {'query': q, 'products':products}
	else:
		template = 'products/results.html'
		context = {}
	return render(request, template, context)

def productDetail(request, slug):
	try:
		product = Product.objects.get(slug=slug)
		images = ProductImage.objects.filter(product=product)
		return render(request, 'products/product-detail.html', {'product':product, 'images':images})
	except:
		return render(request, '404.html', {})

def men(request):
	men = ProductImage.objects.filter(male=True)
	return render(request, 'products/men.html', {'men':men})

def women(request):
	women = ProductImage.objects.filter(female=True)
	return render(request, 'products/women.html', {'women':women})

def nike(request):
	nike = ProductImage.objects.filter(nike=True)
	return render(request, 'products/nike.html', {'nike':nike})

def gucci(request):
	gucci = ProductImage.objects.filter(gucci=True)
	return render(request, 'products/gucci.html', {'gucci':gucci})

def adidas(request):
	adidas = ProductImage.objects.filter(adidas=True)
	return render(request, 'products/adidas.html', {'adidas':adidas})
def givenchy(request):
	givenchy = ProductImage.objects.filter(givenchy=True)
	return render(request, 'products/givenchy.html', {'givenchy':givenchy})
def casual(request):
	casual = ProductImage.objects.filter(casual=True)
	return render(request, 'products/casuals-men.html', {'casual':casual})
def sport(request):
	sport = ProductImage.objects.filter(sport=True)
	return render(request, 'products/sports.html', {'sport':sport})
def female(request):
	female = ProductImage.objects.filter(female=True)
	return render(request, 'products/female.html', {'female':female})
def male(request):
	male = ProductImage.objects.filter(male=True)
	return render(request, 'products/male.html', {'male':male})
def slip_ons(request):
	slip_ons = ProductImage.objects.filter(slip_ons=True)
	return render(request, 'products/slip_ons.html', {'slip_ons':slip_ons})
def boots(request):
	boots = ProductImage.objects.filter(boots=True)
	return render(request, 'boots.html', {'boots':boots})
def sandals(request):
	sandals = ProductImage.objects.filter(sandals=True)
	return render(request, 'sandals.html', {'sandals':sandals})
def lace_ups(request):
	lace_ups = ProductImage.objects.filter(lace_ups=True)
	return render(request, 'lace_ups.html', {'lace_ups':lace_ups})
def oxfords(request):
	oxfords = ProductImage.objects.filter(oxfords=True)
	return render(request, 'oxfords.html', {'oxfords':oxfords})
def black(request):
	black = ProductImage.objects.filter(black=True)
	return render(request, 'black.html', {'black':black})
def white(request):
	white = ProductImage.objects.filter(white=True)
	return render(request, 'white.html', {'white':white})
def blue(request):
	blue = ProductImage.objects.filter(blue=True)
	return render(request, 'women.html', {'blue':blue})
def red(request):
	red = ProductImage.objects.filter(red=True)
	return render(request, 'red.html', {'red':red})
def green(request):
	green = ProductImage.objects.filter(green=True)
	return render(request, 'green.html', {'green':green})
def grey(request):
	grey = ProductImage.objects.filter(grey=True)
	return render(request, 'grey.html', {'grey':grey})
def orange(request):
	orange = ProductImage.objects.filter(orange=True)
	return render(request, 'orange.html', {'orange':orange})
def brown(request):
	brown = ProductImage.objects.filter(brown=True)
	return render(request, 'brown.html', {'brown':brown})
def leather(request):
	leather = ProductImage.objects.filter(leather=True)
	return render(request, 'products/leather.html', {'leather':leather})
def suede(request):
	suede = ProductImage.objects.filter(suede=True)
	return render(request, 'suede.html', {'suede':suede})
def formal(request):
	formal = ProductImage.objects.filter(formal=True)
	return render(request, 'formal.html', {'formal':formal})