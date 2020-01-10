from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from django.views.generic.edit import FormView


from .models import Product
from .forms import RegisterFrom


class ProductList(ListView):
    model = Product
    template_name = 'product.html'
    context_object_name = 'product_list'


class ProductCreate(FormView):
    model = Product
    template_name = 'register_product.html'
    form_class = RegisterFrom
    success_url = '/product/'
