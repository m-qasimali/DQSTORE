from django.db import models


class CustomerReview(models.Model):
    customer_name = models.CharField(max_length=50, null=False)
    customer_picture = models.ImageField(upload_to='upload_data/customer_pics')
    review = models.TextField(null=False)
    rating = models.IntegerField()

    def __str__(self):
        return self.customer_name
