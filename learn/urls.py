from django.urls import path,include
from .views import *
urlpatterns = [
    path('<pk>/',open_jupiter_notbook ),
]
