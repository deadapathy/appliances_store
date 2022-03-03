from email import header
from re import template
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login


def home(request):
    return render(request, 'info/index.html')

def ProjectInfo(request):
    return render(request, 'info/infoProject.html')

#def Registration(request):
 #   return render(request, 'info/registration.html')


def team(request):
    header = "Информация о команде"   
    user ={"name" : "Максим", "age" : 20}         
    addr = ("Ахтанова", 55)
    data = {"header": header, "user": user, "address": addr}
    return render(request, "info/team.html", context=data)          

def contacts(request):
    header = "Контакты разработчиков"
    user = {"telephone" : 77081647680, "Email" : "maksvaskov01@gmial.com" }
    time = {"worktime" : "24/7"}
    data = {"header": header, "user": user, "time": time}
    return render(request, 'info/contacts.html', context=data)

def cart(request):
    return render(request, 'info/cart.html')