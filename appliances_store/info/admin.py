from django.contrib import admin

from .models import Order, Product, ProductCategory, ProductImage, ProductInOrder, Status



# Register your models here.
admin.site.register(Order)
admin.site.register(Status)
admin.site.register(ProductCategory)
admin.site.register(Product)
admin.site.register(ProductInOrder)
admin.site.register(ProductImage)


