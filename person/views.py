from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import *


class HomePage(TemplateView):
    template_name = "home_page.html"


class AllGoods(ListView):
    model = Good
    template_name = "goods_list.html"


class AllStores(ListView):
    model = Store
    template_name = "store_list.html"
