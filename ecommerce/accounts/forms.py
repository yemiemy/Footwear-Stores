from django import forms 
from django.contrib.auth import get_user_model

User = get_user_model()

class LoginForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter your username'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password'}))

	def clean_username(self):
		username = self.cleaned_data.get('username')
		try:
			user = User.objects.get(username=username)
		except User.DoesNotExist:
			raise forms.ValidationError('Are you sure you are registered? We cannot find this user.')
		return username 

	def clean_password(self):
		username = self.cleaned_data.get('username')
		password = self.cleaned_data.get('password')
		try:
			user = User.objects.get(username=username)
		except:
			user = None
		if user is not None and not user.check_password(password):
			raise forms.ValidationError('Invalid Password')
		elif user is None:
			pass
		else:
			return password


class RegistrationForm(forms.ModelForm):
	username = forms.CharField(label='', \
					widget=forms.TextInput(attrs={'placeholder': 'username'}))
	email = forms.EmailField(label='', widget=forms.TextInput(attrs={'placeholder': 'Email Address'}))
	first_name = forms.CharField(label='', \
					widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
	last_name = forms.CharField(label='', \
					widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
	password1 = forms.CharField(label='', \
					widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
	password2 = forms.CharField(label='', \
					widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))

	class Meta:
		model = User
		fields = ['first_name','last_name','username', 'email']
	def clean_password2(self):
		password1 = self.cleaned_data.get('password1')
		password2 = self.cleaned_data.get('password2')
		if password1 and password2 and password1 != password2:
			raise forms.ValidationError('Passwords do not match')
		return password2


	def clean_email(self):
		email = self.cleaned_data.get('email')
		user_count = User.objects.filter(email=email).count()
		print(user_count)
		if user_count > 0 :
			raise forms.ValidationError('This email has already been registered')
		return email

	def save(self, commit=True):
		user = super(RegistrationForm, self).save(commit=False)
		user.set_password(self.cleaned_data['password1'])
		if commit:
			user.save()
		return user 
