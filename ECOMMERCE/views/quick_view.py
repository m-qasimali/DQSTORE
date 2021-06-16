from ECOMMERCE.models import Product, Products_images, Category
from django.shortcuts import render
from django.http import JsonResponse
from django.core.paginator import Paginator


def quick_view(request, id):
    quantity=1
    if request.method == 'POST':
        quantity=request.POST.get('quantity')
    # ============     CART START        ===============
    product_id = request.GET.get('product')
    if product_id is not None:
        print('hello')
        cart = request.session.get('cart')
        if not cart:
            request.session.cart = {}
            cart = {}
            request.session.cart=cart
        else:
            if product_id in cart:
                if 'quantity' in cart[product_id]:
                    quantity = cart[product_id]['quantity']
                    cart[product_id]['quantity'] = quantity
                else:
                    cart[product_id]['quantity'] = quantity
            else:
                cart[product_id] = {}
                cart[product_id]['quantity'] = quantity
        request.session['cart'] = cart
    # ===================   CART END          ======================
    product = Product.objects.filter(id=id)
    for p in product:
        id = p.categoryID
    products = Product.objects.filter(categoryID=id)[0:10]
    context = {'product': product, 'products': products}
    return render(request, 'ECOMMERCE/for_each_product.html', context)


def add_to_cart(request):
    cart = request.session.get('cart')
    product_id = request.GET.get('product')
    quantity = request.GET.get('quantity')

    if product_id is not None:
        cart = request.session.get('cart')
        if not cart:
            request.session.cart = {}
            cart = {}
            cart[product_id] = {}
            cart[product_id]['quantity'] = quantity
        else:
            if product_id in cart:
                cart[product_id]['quantity'] = quantity
            else:
                cart[product_id] = {}
                cart[product_id]['quantity'] = quantity

        request.session['cart'] = cart


    return JsonResponse({'data':cart,'total_items':len(request.session['cart'])})

