from django.contrib import admin

from .models import *



# Register your models here.
admin.site.register(Order)
admin.site.register(Status)
admin.site.register(ProductCategory)
admin.site.register(Product)
admin.site.register(ProductInOrder)
admin.site.register(ProductImage)
admin.site.register(ProductInBasket)


