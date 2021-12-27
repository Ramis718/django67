from django.shortcuts import render, redirect
from . import models, forms


def home_page(request):
    products = models.Product_in.objects.filter().order_by('-id')
    return render(request, 'home_page_in.html', {'product': products})