import os
import uuid

from django.conf import settings
from django.db import models
from django.utils.text import slugify


def product_image_file_path(instance, filename):
    _, extension = os.path.splitext(filename)
    filename = f"{slugify(instance.name)}-{uuid.uuid4()}.{extension}"

    return os.path.join("uploads/products/", filename)


class ImageProduct(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to=product_image_file_path)

    def __str__(self):
        return str(self.name)


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ManyToManyField(ImageProduct, blank=True, related_name='images')
    data = models.DateField(auto_now=True)

    def __str__(self):
        return self.name
