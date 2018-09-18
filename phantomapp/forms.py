from django import forms
from django.db import models
from phantomapp.models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.files.images import get_image_dimensions

class ContactForm(forms.ModelForm):
	class Meta:
		model = Contact
		fields = ('first_name','last_name','email','subject','message',)

class CartForm(forms.Form):
	quantity_choice = [(i,str(i)) for i in range(1,11)]
	unit_price = forms.IntegerField()
	quantity = forms.TypedChoiceField(choices=quantity_choice,coerce=int)

class CheckOutForm(forms.ModelForm):
	class Meta:
		model = Order
		fields = ('username','email','first_name','last_name','company','country','state','address','telephone',)

class UserProfileForm(forms.ModelForm):
	first_name = forms.CharField(max_length=255)
	last_name = forms.CharField(max_length=255)
	
	class Meta:
		model = UserProfile
		fields = ('company','country','state','address','telephone',)

class LoginForm(forms.ModelForm):
	username = forms.CharField(widget=forms.TextInput(attrs={'class':'special', 'size': '35'}),label='username')
	password1 = forms.CharField(widget = forms.PasswordInput(attrs={'class':'special', 'size': '35'}), min_length=8, max_length=100,label='password')

	class Meta:
		model = User
		fields = ('username','password1')

class RegisterForm(UserCreationForm):
	def clean_email(self):
		data = self.cleaned_data['email']
		duplicate_users = User.objects.filter(email=data)
		if self.instance.pk is not None:
			duplicate_users = duplicate_users.exclude(pk=self.instance.pk)
		if duplicate_users.exists():
			raise forms.ValidationError("E-mail is already registered!")
		return data

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )