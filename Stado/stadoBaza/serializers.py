from rest_framework import serializers
from .models import Dawki, Krowy, Krycia, GrupyZywieniowe
from django.contrib.auth.models import User
class Userserializer(serializers.ModelSerializer):
    krowy = serializers.PrimaryKeyRelatedField(many=True, queryset=Krowy.objects.all())
    class Meta:
        model = User
        fields = ['id', 'username', 'krowy']
class DawkiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dawki
        fields = ['idDawki', 'nazwa','wartosc','sklad','opis']


class KrowySerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")
    class Meta:
        model = Krowy
        fields = ['Numer', 'imie', 'DataUrodzenia', 'rasa', 'grupa','opis','wydajnosc','matka','ojciec','owner']


class KryciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Krycia
        fields = ['idKrycia', 'opis', 'data', 'byk', 'krowa']


class GrupyZywienioweSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrupyZywieniowe
        fields = ['idGrupyZywieniowej', 'nazwa', 'opis', 'idDawki']



