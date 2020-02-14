from django.shortcuts import render


def home(request):
    return render(request, 'index.html')

def pro(request):
    return render(request, 'products.html')