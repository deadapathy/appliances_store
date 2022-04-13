from dataclasses import field
from django.contrib import admin

from .models import *



# Register your models here.
admin.site.register(Order)
admin.site.register(Status)
admin.site.register(ProductInOrder)
admin.site.register(ProductInBasket)

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 0


class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductCategory._meta.fields]
    class Meta:
        model = ProductCategory

admin.site.register(ProductCategory, ProductCategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Product._meta.fields]
    inlines = [ProductImageInline]
    search_fields = ('name', 'price')
    class Meta:
        model = Product

admin.site.register(Product, ProductAdmin)


class ProductImageAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductImage._meta.fields]
    list_filter = ('is_active', 'is_main')
    class Meta:
        model = ProductImage

admin.site.register(ProductImage, ProductImageAdmin)