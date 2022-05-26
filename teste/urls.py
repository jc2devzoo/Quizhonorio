from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('' , home, name = "home"),
    path('<id>' , get_quiz , name="get_quiz"),
    path('api/<id>' , api_perg , name="api_perg")
]