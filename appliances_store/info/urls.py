from atexit import register
from unicodedata import name
from django.urls import path, include, re_path
from .views import ProjectInfo, contacts, home, team
from . import views


urlpatterns = [
    path('', home),
    path('accounts/', include('allauth.urls')),
    path('ProjectInfo/', ProjectInfo),
    path('team/', team),
    path('contacts/', contacts),
]
