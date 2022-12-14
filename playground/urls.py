from django.urls import path
from . import views

urlpattrens=[
    path('hello/',views.say_hello)
]