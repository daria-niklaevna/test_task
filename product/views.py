from django.shortcuts import render
from rest_framework import mixins, viewsets
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.viewsets import GenericViewSet

from product.models import Product
from product.serializers import ProductSerializer, ProductListSerializer


class ProductViewSet(
    viewsets.ModelViewSet
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return ProductListSerializer

        return ProductSerializer




