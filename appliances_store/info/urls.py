from atexit import register
from django.urls import path
from .views import ProjectInfo, contacts, home, team
from . import views

urlpatterns = [
    path('', home),
    path('ProjectInfo/', ProjectInfo),
    path('team/', team),
    path('contacts/', contacts),
    path('register/', views.register, name='register'),
]
