from django.shortcuts import render

# Create your views here.
from .models import Wheel,Nav,Mustbuy,shop, MainShow


def home(request):
    wheels = Wheel.objects.all()
    nList = Nav.objects.all()
    mList = Mustbuy.objects.all()
    shops = shop.objects.all()
    mainL = MainShow.objects.all()
    return render(request, 'axfapp/home.html', {"wList":wheels,"navList":nList,
                                                "mustbuyList":mList,"title": "Home",
                                                "mainshops":shops, "mainshows":mainL})

def market(request):
    return render(request, 'axfapp/market.html', {"title": "Market"})

def cart(request):
    return render(request, 'axfapp/cart.html', {"title": "Cart"})

def mine(request):
    return render(request, 'axfapp/mine.html', {"title": "Mine"})
