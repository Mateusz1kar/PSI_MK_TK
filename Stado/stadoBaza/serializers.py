from rest_framework import serializers
from .models import Dawki, Krowy, Krycia, GrupyZywieniowe
class DawkiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dawki
        fields = ['idDawki', 'nazwa','wartosc','sklad','opis']


class KrowySerializer(serializers.ModelSerializer):
    class Meta:
        model = Krowy
        fields = ['Numer', 'imie', 'DataUrodzenia', 'rasa', 'grupa','opis','wydajnosc','matka','ojciec']


class KryciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Krycia
        fields = ['idKrycia', 'opis', 'data', 'byk', 'krowa']


class GrupyZywienioweSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrupyZywieniowe
        fields = ['idGrupyZywieniowej', 'nazwa', 'opis', 'idDawki']



