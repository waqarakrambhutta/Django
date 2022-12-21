from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product


def say_hello(request):
    product = Product.objects.filter(id=0).exists()

    return render(request, 'hello.html', {'name': 'Waqar'})
