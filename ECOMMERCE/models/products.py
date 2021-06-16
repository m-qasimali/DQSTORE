from django.db import models
from ECOMMERCE.models.category import Category

class Product(models.Model):
    product_name = models.CharField(max_length=50,null=False)
    desc = models.CharField(max_length=400)
    categoryID = models.ForeignKey(Category,on_delete=models.CASCADE)
    price = models.IntegerField()
    discount = models.IntegerField()
    sale = models.BooleanField(default=False)
    ranking = models.IntegerField()

    def __str__(self):
        return self.product_name

    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(id__in=ids)


class Products_images(models.Model):
    product = models.ForeignKey(Product,null=False,on_delete=models.CASCADE)
    pic = models.ImageField(upload_to='upload_data/product_image')

    def __str__(self):
        return str(f"{self.product}")

