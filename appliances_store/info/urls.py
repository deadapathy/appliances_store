from django.urls import path
from .views import ProjectInfo, contacts, home, team

urlpatterns = [
    path('', home),
    path('ProjectInfo/', ProjectInfo),
    path('team/', team),
    path('contacts/', contacts)

]
