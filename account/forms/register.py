from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from account.models import Account


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Add a valid email address.',widget=forms.EmailInput(attrs={'autofocus':False,'class': 'space', 'placeholder': 'Email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'space', 'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'space', 'placeholder': 'Confirm Password'}))

    class Meta:
        model = Account
        fields = ('username', 'first_name', 'last_name','phone_number','address','email','password1','password2')
        widgets = {'username':forms.TextInput(attrs={'class':'space','placeholder':'Username','autofocus':True}),
                   'first_name':forms.TextInput(attrs={'class':'space form-control','placeholder':'First Name'}),
                   'last_name': forms.TextInput(attrs={'class': 'space', 'placeholder': 'Last Name'}),
                   'phone_number': forms.TextInput(attrs={'class': 'space', 'placeholder': 'Phone Number'}),
                   'address': forms.TextInput(attrs={'class': 'space', 'placeholder': 'Address'}),
                   }
