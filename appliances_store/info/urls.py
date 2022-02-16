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
]
