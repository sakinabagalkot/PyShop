from django.http import HttpResponse
from django.shortcuts import render
from .models import Products


def index(request):
    prod=Products.objects.all()
    return render(request,'index.html',
                  {'item':prod})


def second(request):
    return HttpResponse("New Products")