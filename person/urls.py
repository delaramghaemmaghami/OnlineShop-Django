from django.urls import path
from .views import *

urlpatterns = [
    path("", HomePage.as_view(), name="HomePage"),
    path("goods/", AllGoods.as_view(), name="AllGoods"),
    path("stores/", AllStores.as_view(), name="AllStores")
]
