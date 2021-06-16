from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('hacker/', admin.site.urls),
    path("",include('ECOMMERCE.urls'))
]
