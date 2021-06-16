from django.shortcuts import render,redirect
from django.contrib.auth import logout

def logout_form(request):
    logout(request)
    # Redirect to a success page
    return render(request,'ECOMMERCE/logout.html')