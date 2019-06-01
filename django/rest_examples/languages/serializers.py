from rest_framework import serializers
from .models import Language, Paradigm, Programmer

# compose json objects
# ModelSerializer: show information relating to your model
class LanguageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Language
        fields = ('id', 'url', 'name', 'paradigm')  # I want to show this information

class ParadigmSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Paradigm
        fields = ('id', 'url', 'name')

class ProgrammerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Programmer
        fields = ('id', 'url', 'name', 'languages')