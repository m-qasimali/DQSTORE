from ECOMMERCE.forms import Contact_form
from django.shortcuts import render,HttpResponse, redirect
from django.contrib import messages


def contact_form(request):
    if request.method == 'POST':
        form = Contact_form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thanks for your response, We will contact you soon!')
        else:
            return render(request, 'ECOMMERCE/contact_us.html', {'form': form})
    form = Contact_form()
    return render(request,'ECOMMERCE/contact_us.html',{'form':form})