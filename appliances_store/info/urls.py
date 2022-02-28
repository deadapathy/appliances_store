from atexit import register
from django.urls import path, include
from .views import ProjectInfo, contacts, home, team
from . import views

urlpatterns = [
    path('', home),
    path('accounts/', include('allauth.urls')),
    path('ProjectInfo/', ProjectInfo),
    path('team/', team),
    path('contacts/', contacts),
    path(r'^', include('shop.urls', namespace='shop')),
    path(r'^$', views.product_list, name='product_list'),
    path(r'^(?P<category_slug>[-\w]+)/$',
        views.product_list,
        name='product_list_by_category'),
    path(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$',
        views.product_detail,
        name='product_detail'),
]
