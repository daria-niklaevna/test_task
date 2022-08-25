from django.db import transaction
from rest_framework import serializers

from product.models import Product, ImageProduct
from user.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username',)


class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ImageProduct
        fields = ('image',)


class ProductSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=False, allow_empty=False)
    author = UserSerializer(many=False, read_only=True)
    class Meta:
        model = Product
        fields = ('id', 'title', 'price', 'author', 'images', 'creation_date')

    def create(self, validated_data):
        with transaction.atomic():
            images = validated_data.pop("images")
            product = Product.objects.create(**validated_data)
            for image in images:
                ImageProduct.objects.create(product=product, **image)
            return product

class ProductListSerializer(ProductSerializer):
    images = ImageSerializer(many=True, read_only=True)

