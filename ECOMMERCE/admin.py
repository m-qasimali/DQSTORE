from django.contrib import admin
from ECOMMERCE.models import Category,Product,Products_images,Order,Ordered_product,Contact,Social_links,CustomerReview,CustomerOrder
from django.utils.html import format_html
from account.models import Account
from django.db import models
from django.forms import Textarea
# Register your models here.




# =========   ORDERED PRODUCTS        =================


@admin.register(Ordered_product)
class Ordered_productAdmin(admin.ModelAdmin):
    list_display = ['order','product','quantity','total_price']
    list_editable = ['quantity']

    def total_price(self,order):
        price = Product.objects.get(product_name=order).price*order.quantity
        order_obj = Ordered_product.objects.filter(id=order.id)
        for item in order_obj:
            obj=item
            obj.price=price
            obj.save()
        return price


# ============       ORDERED PRODUCTS END            ================

# ===============     PRODUCTS         ======================

class Products_imagesAdmin(admin.TabularInline):
    model = Products_images

@admin.register(Product)
class ProductsAdmin(admin.ModelAdmin):
    inlines = [Products_imagesAdmin]
    list_display = ['id','product_name', 'get_category', 'price', 'discount', 'sale']
    list_filter = ['price', 'categoryID','sale']
    list_editable = ['price', 'discount','sale']
    list_per_page = 20
    ordering = ['id']
    search_fields = ['product_name','price', 'discount']

    def get_category(self,product):
        category = Product.objects.get(product_name=product).categoryID
        return format_html(f"<a href='/admin/ECOMMERCE/category/{category.id}/change/'>{category}</a>")

    get_category.short_description = 'Category'


# ===============    product END                  ===========================

# =============      Contact form        ==========================

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id','first_name','last_name','email']
    list_filter = ['email']
    list_display_links = ['first_name','last_name','email']
    search_fields = ['email','first_name','last_name']
    ordering = ['-id']

# =============      Contact form  ENDS      ==========================


# ===================        Category filtering         =========================

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','category_name','total_items','active']
    list_editable = ['active']
    list_per_page = 10
    list_display_links = ['category_name']
    list_filter = ['category_name','active']
    ordering = ['id']
    search_fields = ['category_name']

    def total_items(self, category):
        products = Product.objects.filter(categoryID=category)
        total = 0
        for product in products:
            total += 1
        return total



# ===================        Category filtering  ENDS        =========================


# =============     products images       ============

@admin.register(Products_images)
class Products_imagesAdmin(admin.ModelAdmin):
    list_display = ['id','product','pic']
    list_editable = ['product','pic']
    ordering = ['product']
    list_filter = ['product']
    search_fields = ['product']


# =============     products images end     ==============


@admin.register(CustomerReview)
class CustomerReviewAmin(admin.ModelAdmin):
    list_display = ['id','customer_name','rating']
    list_display_links = ['customer_name']
    list_editable = ['rating']


class Order_productsAdmin(admin.TabularInline):
    model = Ordered_product




@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [Order_productsAdmin]
    list_display = ['id','user_name','customer_email','order_id','order_date']
    list_filter = ['order_date','delivered']
    ordering = ['-order_date']

    def user_name(self, order):

        return format_html(f"<a href='/admin/account/account/{Account.objects.get(email=order.customer_ID).id}/change/'>{Account.objects.get(email=order.customer_ID).username}</a>")

    def customer_email(self,order):
        return format_html(f"<a href='/admin/ECOMMERCE/order/{order.id}/change/?_changelist_filters=o%3D-4'>{Account.objects.get(email=order.customer_ID)}</a>")




    # list_filter = ['price', 'categoryID']



# ===============    Social links          =======================
@admin.register(Social_links)
class Social_linksAdmin(admin.ModelAdmin):
    list_display = ['id','facebook','whatsapp','instagram','github']
    list_editable = ['facebook','whatsapp','instagram','github']
    list_display_links = ['id']






# ===========   CUSTOMER ORDER         ====================

@admin.register(CustomerOrder)
class CustomerOrderAdmin(admin.ModelAdmin):
    list_display = ['id','get_user','view_order','date']
    list_filter = ['date']
    list_per_page = 20
    ordering = ['-date']
    search_fields = ['user','date']

    def get_user(self, user):
        return format_html(f"<a href='/admin/account/account/{Account.objects.get(username=user).id}/change/'>{user}</a>")

    def view_order(self, user):
        return format_html(f"<a href='/admin/ECOMMERCE/order/{user.ordered.id}/change/'>{user.ordered}</a>")

# ===========    CUSTOMER ORDER END    ===================