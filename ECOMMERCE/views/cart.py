from django.shortcuts import render,redirect
from ECOMMERCE.models import Product,Order,Ordered_product,Category
from account.models import Account
import razorpay
from Ecommerce_website.settings import *
from time import time

def cart(request):
    # if not request.user.is_authenticated:
    #     return redirect('login')
    client = razorpay.Client(auth=(KEY_ID, KEY_SECRET))
    delete = request.GET.get('delete')
    total_bill = request.GET.get('bill')
    cart=request.session.get('cart')
    if cart is not None:
        if delete is not None:
            if delete in cart:
                cart.pop(delete)
            request.session['cart']=cart
        ids = list(request.session.get('cart').keys())
        products = Product.get_products_by_id(ids)
        if request.user.is_authenticated:
            if total_bill != '0' and total_bill is not None:
                customer_email = request.user.email
                customer = Account.objects.get(email=customer_email)
                address = request.user.address
                phone=request.user.phone_number
                customer_order = Order(customer_ID=customer,address=address,phone=phone,total_bill=eval(total_bill))
                customer_order.save()

                for product in products:
                    ordered_obj = Order.objects.get(id=customer_order.id)
                    print(customer_order.id)
                    p_name = Product.objects.get(id=product.id)
                    p_quantity = request.session.get('cart')[str(product.id)]['quantity']
                    p_price = product.price * p_quantity
                    customer_products = Ordered_product(order=ordered_obj, product=p_name, quantity=p_quantity,
                                                        price=p_price)
                    customer_products.save()

                currency = 'PKR'
                notes = {
                    'email': customer_email,
                    'name': f"{request.user.first_name} {request.user.last_name}"
                }
                receipt = f"DQSTORE-{int(time())}"
                order = client.order.create({
                    'amount': int(total_bill)*100,
                    'currency': currency,
                    'notes': notes,
                    'receipt': receipt
                })

                customer_order.order_id = order.get('id')
                customer_order.save()
                return render(request, 'ECOMMERCE/cart.html', {'products': products, 'order': order})
        return render(request, 'ECOMMERCE/cart.html',{'products':products})



    return render(request, 'ECOMMERCE/cart.html')