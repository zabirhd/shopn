from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
# Create your views here.

def prod (request):
    products = Product.objects.all()
    return render(request,'products.html',{'products':products})



def index(request):
    return render(request,'index.html')


