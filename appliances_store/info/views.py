from datetime import date
from email import header
from math import prod
from re import template
from threading import local
from urllib import request
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login
from .models import *


def home(request):
    products_images = ProductImage.objects.filter(product__category__id=1)
    products_images2 = ProductImage.objects.filter(product__category__id=2)
    # products_images_plates = products_images.filter(product__category__id=1)
    return render(request, 'info/index.html', locals())

def category(request):
    return render(request, 'products/category.html', locals())

def for_kitchen(request):
    return render(request, 'category/for-kitchen.html', locals())

def dishes(request):
    return render(request, 'category/dishes.html', locals())

def tec_for_home(request):
    return render(request, 'category/tec-for-home.html', locals())

def health_and_beauty(request):
    return render(request, 'category/health-and-beauty.html', locals())

def instruments(request):
    return render(request, 'category/instruments.html', locals())

def other(request):
    return render(request, 'category/other.html', locals())

def delivery(request):
    return render(request, 'info/delivery.html', locals())

def payment(request):
    return render(request, 'info/payment.html', locals())

def grap_work(request):
    return render(request, 'info/grap-work.html', locals())

def product(request, product_id):
    product = Product.objects.get(id=product_id)

    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()
    print(request.session.session_key)

    return render(request, 'products/product.html', locals())


def basket_adding(request):
    
    return_dict = dict()
    session_key = request.session.session_key
    print (request.POST)
    data = request.POST
    product_id = data.get("product_id")
    nmb = data.get("nmb")
    is_delete = data.get("is_delete")

    if is_delete == 'true':
        ProductInBasket.objects.filter(id=product_id).update(is_active=False)
    else:
        new_product, created = ProductInBasket.objects.get_or_create(session_key=session_key, product_id=product_id,
                                                                     is_active=True, defaults={"nmb": nmb})
        if not created:
            print ("not created")
            new_product.nmb += int(nmb)
            new_product.save(force_update=True)

    #common code for 2 cases
    products_in_basket = ProductInBasket.objects.filter(session_key=session_key, is_active=True, order__isnull=True)
    products_total_nmb = products_in_basket.count()
    
    return_dict["products_total_nmb"] = products_total_nmb

    return_dict["products"] = list()

    for item in  products_in_basket:
        product_dict = dict()
        product_dict["id"] = item.id
        product_dict["name"] = item.product.name
        product_dict["price_per_item"] = item.price_per_item
        product_dict["nmb"] = item.nmb
        return_dict["products"].append(product_dict)

    return JsonResponse(return_dict)

def checkout(request):
    session_key = request.session.session_key
    products_in_basket = ProductInBasket.objects.filter(session_key=session_key, is_active=True)
    return render(request, 'products/checkout.html', locals())

def refrigerators(request):
    products_images_refrigerators = ProductImage.objects.filter(product__category__id=3)
    return render(request, 'subcategory/tec-for-kitchen/refrigerators.html', locals())

def plates(request):
    products_images_plates = ProductImage.objects.filter(product__category__id=4)
    return render(request, 'subcategory/tec-for-kitchen/plates.html', locals())

def microwave(request):
    products_images_microwave = ProductImage.objects.filter(product__category__id=5)
    return render(request, 'subcategory/tec-for-kitchen/microwave.html', locals())

def teapot(request):
    products_images_teapot = ProductImage.objects.filter(product__category__id=6)
    return render(request, 'subcategory/tec-for-kitchen/teapot.html', locals())

def coffeMachine(request):
    products_images_coffeMachine = ProductImage.objects.filter(product__category__id=7)
    return render(request, 'subcategory/tec-for-kitchen/coffeMachine.html', locals())

def pans(request):
    products_images_pans = ProductImage.objects.filter(product__category__id=8)
    return render(request, 'subcategory/dishes/pans.html', locals())

def pots(request):
    products_images_pots = ProductImage.objects.filter(product__category__id=9)
    return render(request, 'subcategory/dishes/pots.html', locals())

def serving(request):
    products_images_serving = ProductImage.objects.filter(product__category__id=10)
    return render(request, 'subcategory/dishes/serving.html', locals())

def kitchenware(request):
    products_images_kitchenware = ProductImage.objects.filter(product__category__id=11)
    return render(request, 'subcategory/dishes/kitchenware.html', locals())

def vacuum(request):
    products_images_vacuum = ProductImage.objects.filter(product__category__id=12)
    return render(request, 'subcategory/tec-for-home/vacuum.html', locals())

def washing_machines(request):
    products_images_washing_machines = ProductImage.objects.filter(product__category__id=13)
    return render(request, 'subcategory/tec-for-home/washing_machines.html', locals())

def irons(request):
    products_images_irons = ProductImage.objects.filter(product__category__id=14)
    return render(request, 'subcategory/tec-for-home/irons.html', locals())

def telephones(request):
    products_images_telephones = ProductImage.objects.filter(product__category__id=15)
    return render(request, 'subcategory/tec-for-home/telephones.html', locals())