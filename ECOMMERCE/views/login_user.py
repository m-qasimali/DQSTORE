from django.shortcuts import render,HttpResponse, redirect
from account.forms import AccountAuthenticationForm
from account.models import Account
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout


def login_form(request,id):
    if request.user.is_authenticated:
        return redirect("home")
    if request.method == 'POST':
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)

            if user:
                login(request, user)
                if id==1:
                    return redirect("cart")
                else:
                    return redirect("home")
            else:
                messages.add_message(request,messages.SUCCESS,'Invalid Login')
                return render(request, 'ECOMMERCE/login_form.html', {'form': form})
        else:
            # ========   Form Validation    ============
            valid = []
            invalid = []
            for field in form.errors:
                invalid.append(field)
                form[field].field.widget.attrs['class'] += ' is-invalid form-control'
            for field in form:
                field = field.name
                if field not in invalid:
                    valid.append(field)

            for field in valid:
                form[field].field.widget.attrs['class'] += ' is-valid form-control'
            return render(request,'ECOMMERCE/login_form.html',{'form':form})
    else:
        form = AccountAuthenticationForm()
        return render(request,'ECOMMERCE/login_form.html',{'form':form})