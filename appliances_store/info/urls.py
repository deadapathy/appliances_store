from atexit import register
from unicodedata import name
from django.urls import path, include, re_path
from .views import *
from . import views



urlpatterns = [
    path('', home),
    path('accounts/', include('allauth.urls')),
    re_path(r'^product/(?P<product_id>\w+)/$', views.product, name='product'),
    re_path(r'^basket_adding/$', views.basket_adding, name='basket_adding'),
    re_path(r'^checkout/$', views.checkout, name='checkout'),
    path('category/', views.category, name= 'category'),
    path('for-kitchen/', views.for_kitchen, name='for-kitchen'),
    path('dishes', views.dishes, name='dishes'),
    path('tec-for-home', views.tec_for_home, name='tec-for-home'),
    path('health-and-beauty', views.health_and_beauty, name='health-and-beauty'),
    path('instruments', views.instruments, name="instruments"),
    path('other', views.other, name="other"),
    path('delivery', views.delivery, name="delivery"),
    path('payment', views.payment, name="payment"),
    path('graph-work', views.grap_work, name="graph-work"),
    path('refrigerators', views.refrigerators, name="refrigerators"),
    path('plates', views.plates, name="plates"),
    path('microwave', views.microwave, name="microwave"),
    path('teapot', views.teapot, name="teapot"),
    path('coffeMachine', views.coffeMachine, name="coffeMachine"),
    path('pans', views.pans, name="pans"),
    path('pots', views.pots, name="pots"),
    path('serving', views.serving, name="serving"),
    path('kitchenware', views.kitchenware, name="kitchenware"),
    path('vacuum', views.vacuum, name="vacuum"),
    path('washing_machines', views.washing_machines, name="washing_machines"),
    path('irons', views.irons, name="irons"),
    path('telephones', views.telephones, name="telephones"),
    path('scales', views.scales, name="scales"),
    path('electric_shaver', views.electric_shaver, name="electric_shaver"),
    path('hairdryers', views.hairdryers, name="hairdryers"),
    path('trimmers', views.trimmers, name="trimmers"),
]
