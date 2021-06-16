from ECOMMERCE.models import Contact
from django import forms

class Contact_form(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ('first_name','last_name','email','message')
        widgets = {'first_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter First Name'}),
                  'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Last Name'}),
                  'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email'}),
                  'message': forms.Textarea(attrs={'class': 'form-control resize', 'placeholder': 'EnterYour Message','rows':9})
                  }