from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from Ecommerce_website.settings import STATIC_URL,STATIC_ROOT,MEDIA_ROOT,MEDIA_URL
from django.conf.urls.static import static
from ECOMMERCE import views
from . import views

urlpatterns = [
    path('',views.home_view,name='home'),
    path('contacts/',views.contact_form,name='contactus'),
    path('products/', views.products, name='products'),
    path('login/<int:id>', views.login_form, name='login'),
    path('logout/', views.logout_form, name='logout'),
    path('registration/', views.register, name='registration'),
    path('each/<int:id>', views.quick_view, name='each_product'),
    path('cart/', views.cart, name='cart'),
    path('verify/', views.verify_payment, name='verify_payment'),
    path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
]
urlpatterns += static(STATIC_URL, document_root=STATIC_ROOT)
urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)