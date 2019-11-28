from django.contrib import admin
from .models import Dawki, GrupyZywieniowe, Krycia, Krowy

# Register your models here.
admin.site.register(Dawki)
admin.site.register(GrupyZywieniowe)
admin.site.register(Krycia)
admin.site.register(Krowy)