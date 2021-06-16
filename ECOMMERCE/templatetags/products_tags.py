from django import template
from math import ceil
from ECOMMERCE.models import Product,Products_images,Social_links

register = template.Library()

@register.simple_tag
def cal_discount(price,discount):
    if discount is None or discount == 0:
        return price
    else:
        discount_price = price - (price * discount * 0.01)
        return ceil(discount_price)

@register.simple_tag
def quantity_func(cart,id):
    product_quantity = cart[str(id)]['quantity']
    return product_quantity

@register.simple_tag
def total(request):
    ids = list(request.session.get('cart').keys())
    products = Product.get_products_by_id(ids)
    sum=0
    for product in products:
        discount_price = ceil(product.price - (product.price * product.discount * 0.01))
        product_quantity = request.session.get('cart')[str(product.id)]['quantity']
        sum +=int(discount_price)*int(product_quantity)
    return sum

@register.filter
def product_pics(product):
    images = Products_images.objects.filter(product=product)[0:2]
    return images

# ===============    FOOTER     =====================
@register.filter
def footer_products(p):
    footer_items = Product.objects.filter(ranking=5)[:5]
    return footer_items

@register.filter
def social_links(p):
    links = Social_links.objects.all()
    return links



@register.filter
def product_pics4(product):
    images = Products_images.objects.filter(product=product)[0:4]
    return images

@register.filter
def product_pics1(product):
    images = Products_images.objects.filter(product=product)[0:1]
    return images


@register.filter
def rupees(price):
    return f"₨.{price}"

@register.simple_tag
def subtotal_func(price,quantity):
    return int(price)*int(quantity)

@register.filter(name='times')
def times(number):
    return range(number)

@register.filter()
def addSum(i):
    return i+499


@register.filter
def get_quantity(id, cart):
    if str(id) in cart:
        return cart[str(id)]['quantity']
    else:
        return 1