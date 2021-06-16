from django.shortcuts import render
from django.views.generic import ListView
from ECOMMERCE.models import Category, Product, Products_images, CustomerReview, Social_links


def home_view(request):
    # ============     CART START        ===============
    product_id = request.GET.get('product')
    if product_id is not None:
        cart = request.session.get('cart')
        if not cart:
            request.session.cart = {}
            cart = {}
            cart[product_id] = {}
            cart[product_id]['quantity'] = 1
        else:
            if product_id in cart:
                if 'quantity' in cart[product_id]:
                    quantity = cart[product_id]['quantity']
                    cart[product_id]['quantity'] = int(quantity) + 1
                else:
                    cart[product_id]['quantity'] = 1
            else:
                cart[product_id] = {}
                cart[product_id]['quantity'] = 1
        request.session['cart'] = cart
    products = Product.objects.filter(sale=True).order_by('-id')[0:10]
    category = Category.objects.filter(active=True)
    customer_reviews = CustomerReview.objects.all()

    context = {'category': category, 'products': products, 'customer_reviews': customer_reviews}
    return render(request, 'ECOMMERCE/home.html', context)
