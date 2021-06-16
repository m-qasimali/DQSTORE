from django import forms
from django.contrib.auth import authenticate

from account.models import Account


class AccountAuthenticationForm(forms.Form):
    email = forms.EmailField(label='email',widget=forms.EmailInput(attrs={'class': 'qwe', 'placeholder': 'Email','id':'email'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'space','placeholder':'Password','id':'password'}))
