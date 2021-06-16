from django.db import models


class Contact(models.Model):
    first_name = models.CharField(max_length=20, null=False)
    last_name = models.CharField(max_length=20, null=False)
    email = models.EmailField(null=False)
    message = models.TextField(max_length=700)
