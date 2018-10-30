from django.db import models

# Create your models here.
from django.urls import reverse


class Products(models.Model):
    product_title = models.CharField(max_length=200)
    product_price = models.CharField(max_length=50)
    product_description = models.CharField(max_length=250)

    def get_absolute_url(self):
        return reverse('blog:index')
