from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from .models import Product


class ProductList(ListView):
    model = Product
    template_name = 'product.html'
    context_object_name = 'product_list'