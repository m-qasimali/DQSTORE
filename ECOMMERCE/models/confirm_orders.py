from django.db import models
from ECOMMERCE.models import Order
from Ecommerce_website import settings


class CustomerOrder(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, max_length=100, null=False,on_delete=models.CASCADE)
    ordered = models.ForeignKey(Order, on_delete=models.CASCADE, null=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}"