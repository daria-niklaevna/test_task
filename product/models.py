import os
import uuid

from django.conf import settings
from django.db import models


def product_image_file_path(instance, filename):
    _, extension = os.path.splitext(filename)
    filename = f"{uuid.uuid4()}.{extension}"

    return os.path.join("uploads/products/", filename)


class Product(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    creation_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

    def save(
        self, *args, **kwargs
    ):
        super(Product, self).save(*args, **kwargs)


class ImageProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to=product_image_file_path)

