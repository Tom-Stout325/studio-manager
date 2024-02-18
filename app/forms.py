from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.forms.models import inlineformset_factory
from django.forms.widgets import PasswordInput, TextInput
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms
from .models import *



class CreateInvoiceForm(forms.ModelForm):
	STATUS = (
		('Pending', 'Pending'),
		('Paid', 'Paid'),
		('Past Due', 'Past Due')
	)
	GROUP = (
        ('Airborne Images', 'Airborne Images'),
        ('Tom Stout Photography', 'Tom Stout Photography'),
        ('12bytes', '12bytes'),
    )

	group           = forms.ModelChoiceField(widget=forms.Select(attrs={'class': 'form-control'}),queryset=Group.objects.all())
	client          = forms.ModelChoiceField(widget=forms.Select(attrs={'class': 'form-control'}),queryset=Client.objects.all())
	date 	        = forms.DateField(widget=forms.DateInput(attrs={'class':'form-content', 'type':'date', 'input_type': 'text'}))
	inv_numb		= forms.IntegerField(label='Invoice Number', widget=forms.NumberInput(attrs={'class': 'form-control'}))
	location		= forms.CharField(label='Location',widget=forms.TextInput(attrs={'class': 'form-control'}))
	event	        = forms.CharField(label='Event',widget=forms.TextInput(attrs={'class': 'form-control'}))
	amount			= forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
	status			= forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}),choices=STATUS)

	class Meta:
		model = Invoice
		fields = ['group', 'client', 'date', 'inv_numb', 'location', 'event', 'amount', 'status']
 

class AddProductForm(forms.ModelForm):
	Invoice			= forms.ModelChoiceField(widget=forms.Select(attrs={'class': 'form-control'}),queryset=Invoice.objects.all())
	name			= forms.ModelChoiceField(widget=forms.Select(attrs={'class': 'form-control'}),queryset=Product.objects.all())
	price			= forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))	

	class Meta:
		model = Product
		fields = ['name', 'price']




class ClientForm(ModelForm):
	fname		= forms.CharField(label='First Name*',widget=forms.TextInput(attrs={'class': 'form-control'}))
	lname		= forms.CharField(label='Last Name*',widget=forms.TextInput(attrs={'class': 'form-control'}))
	phone		= forms.IntegerField(label='Phone*',widget=forms.NumberInput(attrs={'class': 'form-control'}))
	email		= forms.EmailField(label='Email*',widget=forms.EmailInput(attrs={'class': 'form-control'}))
	business	= forms.CharField(label='Business*',widget=forms.TextInput(attrs={'class': 'form-control'}))
	street		= forms.CharField(label='Street Address*',widget=forms.TextInput(attrs={'class': 'form-control'}))
	city		= forms.CharField(label='City*',widget=forms.TextInput(attrs={'class': 'form-control'}))
	state		= forms.CharField(label='State*',widget=forms.TextInput(attrs={'class': 'form-control'}))
	zip_code	= forms.IntegerField(label='Zip Code*',widget=forms.NumberInput(attrs={'class': 'form-control'}))

	class Meta:
		model = Client
		fields = '__all__'



class RegisterForm4(UserCreationForm):
	email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'type': 'email'}))
	username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
	first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
	last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
	password1 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'password'}))
	password2 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'password'}))
    
	class Meta:
		model = User
		fields = ('email', 'username', 'first_name', 'last_name', 'password1', 'password2')


class RegisterUpdate4(UserChangeForm):
	email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'type': 'email'}))
	username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

	class Meta:
		model = User
		fields = ('email', 'username')
			
	def __init__(self, *args, **kwargs):
		super(RegisterUpdate4, self).__init__(*args, **kwargs)


class LoginForm4(AuthenticationForm):
	username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
	password = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'password'}))

	class Meta:
		model = User
		fields = ('username', 'password')




class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())


class CreateUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('email', 'username', 'first_name', 'last_name', 'password1', 'password2')