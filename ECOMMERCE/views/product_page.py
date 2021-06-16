from ECOMMERCE.models import Product,Products_images,Category
from django.shortcuts import render
from django.core.paginator import Paginator

def products(request):
    cat = False
    category_id = request.GET.get('category')
    # ============     CART START        ===============
    product_id = request.GET.get('product')
    Range = range(1,10000,500)
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
    # ===================   CART END          ======================
    if request.method == 'POST' or request.is_ajax():
        cat1=request.POST.get('category')
        price = request.POST.get('price')
        # ================       SEARCH BAR          ==========================
        if price is not None and cat1 is not None:
            p1,p2 = price.split("-")
            p1 = int(p1)
            p2 = int(p2)
            cat=Category.objects.get(id=cat1)
            products = Product.objects.filter(price__range=(p1,p2),categoryID=cat1).order_by('-id')
        elif price is not None:
            p1,p2 = price.split("-")
            p1 = int(p1)
            p2 = int(p2)
            products = Product.objects.filter(price__range=(p1,p2)).order_by('-id')
        elif cat1 is not None:
            products = Product.objects.filter(categoryID=cat1).order_by('-id')
            cat=Category.objects.get(id=cat1)
        else:
            products = Product.objects.all().order_by('-id')
    else:
        if category_id is not None:
            products = Product.objects.filter(categoryID=category_id).order_by('-id')
        else:
            products = Product.objects.all().order_by('-id')

    categories = Category.objects.filter(active=True)
    # ==================       PAGINATION             =====================
    paginator = Paginator(products,20)
    try:
        page_number = int(request.GET.get('page', '1'))
    except:
        page_number = 1
    page_obj = paginator.get_page(page_number)
    context = {'categories':categories,'page':page_obj,'paginator':paginator,'cat':cat,'range':Range}
    return render(request,'ECOMMERCE/all_products.html',context)
