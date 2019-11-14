from django.db import models
class Dawki(models.Model):
    idDawki = models.AutoField(primary_key=True)
    nazwa = models.CharField(max_length=50)
    wartosc = models.IntegerField(max_length=100)
    sklad = models.CharField(max_length=300)
    opis = models.CharField(max_length=500)
class GrupyZywieniowe(models.Model):
    idGrupyZywieniowej = models.AutoField(primary_key=True)
    nazwa = models.CharField(max_length=50)
    opis = models.CharField(max_length=500)
    idDawki = models.ForeignKey(Dawki, on_delete=models.CASCADE)
class Krowy(models.Model):
    Numer = models.AutoField(primary_key=True)
    imie = models.CharField(max_length=50)
    DataUrodzenia = models.DateField('data urodzenia')
    rasa = models.CharField(max_length=50)
    grupa = models.ForeignKey(GrupyZywieniowe, on_delete=models.CASCADE)
    opis = models.CharField(max_length=500)
    wydajnosc = models.IntegerField(max_length=50)
    matka = models.ForeignKey('self', on_delete=models.SET_NULL)
    ojciec = models.ForeignKey('self', on_delete=models.SET_NULL)
class Krycia(models.Model):
    idKrycia = models.AutoField(primary_key=True)
    opis = models.CharField(max_length=500)
    data = models.DateField('data krycia')
    byk = models.ForeignKey(Krowy.matka, on_delete=models.CASCADE)
    krowa = models.ForeignKey(Krowy.ojciec, on_delete==models.CASCADE)

