from django.shortcuts import render,HttpResponse,redirect
from ECOMMERCE.models import Order,Ordered_product,CustomerOrder,Social_links
from Ecommerce_website.settings import *
from account.models import Account
import razorpay
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.core.mail import send_mail,EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from ECOMMERCE.models import Product,Order,Ordered_product,Category
from account.models import Account
import datetime

@csrf_exempt
def verify_payment(request):
    client = razorpay.Client(auth=(KEY_ID, KEY_SECRET))
    if request.method == 'POST':
        data = request.POST
        try:
            client.utility.verify_payment_signature(data)
            order_id = data['razorpay_order_id']
            payment_id = data['razorpay_payment_id']
            payment = Order.objects.get(order_id=order_id)
            payment.Payment_ID=payment_id
            # payment.status = True
            payment.save()

            customer_order = CustomerOrder(user=Account.objects.get(email=request.user.email),ordered=Order.objects.get(order_id=payment.order_id))
            customer_order.save()


            # ------------   Success message        --------------
            # send_mail('testing', 'hello testing', 'qa624889@gmail.com', ['muhammadqasimali96@gmail.com'],
            #           fail_silently=False)

            ids = list(request.session.get('cart').keys())
            products = Product.get_products_by_id(ids)
            date = Order.objects.get(order_id=payment.order_id).order_date.strftime("%d %B,%Y  %X")
            address = request.user.address
            social = Social_links.objects.all()
            context={'products': products,'order_id':order_id,'user':f"{request.user.first_name} {request.user.last_name}",'bill':Order.objects.get(order_id=payment.order_id).total_bill,'address':address,'date':date,'social':social}
            subject = f'Good News – Your DQSTORE order ({order_id}) has received!'
            to = 'muhammadqasimali96@gmail.com'
            from_email = EMAIL_HOST_USER
            html_message = render_to_string('ECOMMERCE/email_order_confirmation.html', context)
            plain_message = strip_tags(html_message)
            email = EmailMultiAlternatives(subject,
                                           plain_message,
                                           from_email,
                                           [to])
            email.attach_alternative(html_message,'text/html')
            email.send()

            messages.info(request,f'Your order has received, order id is {order_id}!')

            #  -------------      Clearing cart        -------------
            cart = request.session.get('cart')
            cart.clear()
            request.session['cart'] = cart

            return redirect('cart')
        except:
            return HttpResponse("Invalid Payment Details")