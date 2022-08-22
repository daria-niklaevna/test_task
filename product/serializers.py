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
        fields = ('id', 'title', 'image')


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('id', 'title', 'price', 'author', 'image', 'creation_date')


class ProductListSerializer(ProductSerializer):
    image = ImageSerializer(many=True, read_only=True)
    author = UserSerializer(many=False, read_only=True)
