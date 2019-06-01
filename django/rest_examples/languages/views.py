from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Language, Paradigm, Programmer
from .serializers import LanguageSerializer, ParadigmSerializer, ProgrammerSerializer

# Create your views here.

class LanguageView(viewsets.ModelViewSet):
    # handle different solutions in post and get method
    queryset = Language.objects.all()   # return all the data
    serializer_class = LanguageSerializer
    # only login user can edit the language
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )

class ParadigmView(viewsets.ModelViewSet):
    # handle different solutions in post and get method
    queryset = Paradigm.objects.all()   # return all the data
    serializer_class = ParadigmSerializer

class ProgrammerView(viewsets.ModelViewSet):
    # handle different solutions in post and get method
    queryset = Programmer.objects.all()   # return all the data
    serializer_class = ProgrammerSerializer