from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework import routers

# automatic generate urls for you
router = routers.DefaultRouter()
router.register('languages', views.LanguageView)
router.register('paradigms', views.ParadigmView)
router.register('programmers', views.ProgrammerView)

urlpatterns = [
    path('', include(router.urls))
]