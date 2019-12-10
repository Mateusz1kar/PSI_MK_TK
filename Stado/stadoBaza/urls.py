from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dawki/', views.dawki_list, name="dawki_list"),
    path('dawki/<int:pk>/',views.dawki_detail, name='dawki_show'),

    path('grupyZywieniowe/', views.grupyZywieniowe_list, name="grupyZywieniowe_list"),
    path('grupyZywieniowe/<int:pk>/', views.grupyZywieniowe_detail, name='grupyZywieniowe_show'),

    path('krowy/', views.krowy_list, name="krowy_list"),
    path('krowy/<int:pk>/', views.krowy_detail, name='krowy_show'),

    path('krycia/', views.krycia_list, name="krycia_list"),
    path('krycia/<int:pk>/', views.krycia_detail, name='krycia_show'),
]