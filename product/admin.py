from django.contrib import admin


from product.models import Product, ImageProduct

admin.site.register(ImageProduct)
admin.site.register(Product)
