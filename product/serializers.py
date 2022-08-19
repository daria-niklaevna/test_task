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
        fields = ('id', 'name', 'image')


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'user', 'image', 'data')


class ProductListSerializer(ProductSerializer):
    image = ImageSerializer(many=True, read_only=True)
    user = UserSerializer(many=False, read_only=True)
