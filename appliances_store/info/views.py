from email import header
from re import template
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login
from .models import *


def home(request):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True)
    # products_images_plates = products_images.filter(product__category__id=1)
    return render(request, 'info/index.html', locals())


def ProjectInfo(request):
    return render(request, 'info/infoProject.html')

# def Registration(request):
 #   return render(request, 'info/registration.html')


def team(request):
    header = "Информация о команде"
    user = {"name": "Максим", "age": 20}
    addr = ("Ахтанова", 55)
    data = {"header": header, "user": user, "address": addr}
    return render(request, "info/team.html", context=data)


def contacts(request):
    header = "Контакты разработчиков"
    user = {"telephone": 77081647680, "Email": "maksvaskov01@gmial.com"}
    time = {"worktime": "24/7"}
    data = {"header": header, "user": user, "time": time}
    return render(request, 'info/contacts.html', context=data)


def cart(request):
    return render(request, 'info/cart.html')


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
    print(request.POST)
    data = request.POST
    product_id = data.get("product_id")
    nmb = data.get("nmb")

    new_product, created = ProductInBasket.objects.get_or_create(session_key=session_key, product_id=product_id, defaults={"nmb": nmb})

    if not created:
        print("not created")
        new_product.nmb += int(nmb)
        new_product.save(force_update=True)

    products_in_basket = ProductInBasket.objects.filter(session_key=session_key, is_active=True)
    products_total_nmb = products_in_basket.count()
    return_dict["products_total_nmb"] = products_total_nmb

    return_dict["products"] = list()

    for item in products_in_basket:
        product_dict = dict()
        product_dict["name"] = item.product.name
        product_dict["price_per_item"] = item.price_per_item
        product_dict["nmb"] = item.nmb
        return_dict["products"].append(product_dict)
    return JsonResponse(return_dict)
