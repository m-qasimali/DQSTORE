from django.db import models


class Social_links(models.Model):
    facebook = models.URLField(max_length=400, null=False)
    whatsapp = models.URLField(max_length=400, null=False)
    github = models.URLField(max_length=400, null=False)
    instagram = models.URLField(max_length=400, null=False)

    def __str__(self):
        return 'Social Link'
