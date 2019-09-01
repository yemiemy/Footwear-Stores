import re
from django.shortcuts import render, redirect, Http404
from django.contrib.auth import logout, login, authenticate
from .forms import *
from .models import *
from django.contrib import messages
from django.urls import reverse
# Create your views here.
def logout_view(request):
	logout(request)
	messages.success(request, 'Your account has been successfully logged out. <a href={}>Login</a> again'.format(reverse("auth_login")), extra_tags='safe')
		
	return redirect(reverse('auth_login'))
def login_view(request):
	form = LoginForm(request.POST or None)
	btn = 'Login'
	header = 'Login to your account.'
	if form.is_valid():
		username = form.cleaned_data['username']
		password = form.cleaned_data['password']
		user = authenticate(username=username, password=password)
		login(request, user)
		messages.success(request, 'Your account has been successfully logged in')
		return redirect('/')
		#user.emailconfirmed.activate_user_email()
	context = {
		'form':form,
		'submit_btn':btn,
		'header':header
	}
	return render(request, 'form.html', context)

def registration_view(request):
	form = RegistrationForm(request.POST or None)
	btn = 'create'
	header = 'Create an account with us today!'	
	if form.is_valid():
		print('is valid')
		new_user = form.save(commit=False)
		#new_user.first_name = 'Justin'
		new_user.save()
		messages.success(request, 'Your account has been created Successfully. Check your email to confirm your email address.')
		return redirect('auth_login')
	# 	username = form.cleaned_data['username']
	# 	password = form.cleaned_data['password']
	# 	user = authenticate(username=username, password=password)
	# 	login(request, user)
	context = {
		'form':form,
		'submit_btn' : btn,
		'header':header,
	}
	return render(request, 'form.html', context)
SHA1_RE = re.compile('^[a-f0-9]{40}$')
def activation_view(request, activation_key):
	if SHA1_RE.search(activation_key):
		print ('activation key is valid')
		try:
			user_confirmed = EmailConfirmed.objects.get(activation_key=activation_key)
		except EmailConfirmed.DoesNotExist:
			user_confirmed = None
			messages.success(request, 'There was an error with your request')
			return redirect('/')
		if user_confirmed is not None and not user_confirmed.confirmed:
			message = 'Confirmation Successful!!'
			user_confirmed.confirmed = True
			user_confirmed.activation_key = 'confirmed'
			user_confirmed.save()
			messages.success(request, 'Your account has been activated')
		
		elif user_confirmed is not None and user_confirmed.confirmed:
			message = 'Already confirmed'
			messages.success(request, 'Your account has already been activated')
		
		else:
			message = ''
		context = {'message':message}
		return render(request, 'accounts/activation.html', context)
	else:
		raise Http404