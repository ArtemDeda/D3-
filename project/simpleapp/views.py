from django.views.generic import ListView, DetailView
from .models import Product
from django.shortcuts import render


def index(request):
    return render(request, 'index.htm;')


class ProductsList(ListView):
    model = Product
    ordering = 'name'
    template_name = 'products.html'
    context_object_name = 'products'


class ProductDetail(DetailView):
    model = Product
    template_name = 'product.html'
    context_object_name = 'product'




