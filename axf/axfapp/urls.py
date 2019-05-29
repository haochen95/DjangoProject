from django.contrib import admin
from django.urls import path,include

from . import views

urlpatterns = [
    # 四个页面
    path('home/', views.home, name="home"),
    path('market/', views.market, name="market"),
    path('cart/', views.cart, name="cart"),
    path('mine/', views.mine, name="mine"),
]