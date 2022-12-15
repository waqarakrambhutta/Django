from django.shortcuts import render
from django.http import HttpResponse

def say_hello(request):
    return HttpResponse('This is my first django project.')

# Create your views here.
