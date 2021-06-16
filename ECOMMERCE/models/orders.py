from django.db import models
from ECOMMERCE.models import Product
from django.contrib.auth.models import User
import time
from Ecommerce_website import settings

class Order(models.Model):
    customer_ID = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    order_id = models.CharField(max_length=50,null=False)
    address = models.CharField(max_length=200,null=False)
    phone = models.CharField(max_length=13,null=False)
    total_bill = models.IntegerField()
    Payment_ID = models.CharField(max_length=100)
    order_date = models.DateTimeField(auto_now_add=True)
    delivered = models.BooleanField(default=False)

    def __str__(self):
        return str(self.order_id)


class Ordered_product(models.Model):
    order = models.ForeignKey(Order,null=True,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.CharField(max_length=50,null=False)

    def __str__(self):
        return str(self.product)
