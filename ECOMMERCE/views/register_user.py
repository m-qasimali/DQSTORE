from django.shortcuts import render,HttpResponse
from account.forms import RegistrationForm
from account.models import Account


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Register successfully!!")
        else:
            # ========   Form Validation    ============
            valid =[]
            invalid = []
            for field in form.errors:
                invalid.append(field)
                form[field].field.widget.attrs['class'] += ' is-invalid form-control'
            for field in form:
                field = field.name
                valid.append(field)

            for field in valid:
                form[field].field.widget.attrs['class'] += ' is-valid form-control'
            return render(request, 'ECOMMERCE/registration.html', {'form': form})
    else:
        form = RegistrationForm()
        return render(request,'ECOMMERCE/registration.html',{'form':form})