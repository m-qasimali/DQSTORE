from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=50,null=False)
    picture = models.ImageField(upload_to='upload_data/category_pics')
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.category_name