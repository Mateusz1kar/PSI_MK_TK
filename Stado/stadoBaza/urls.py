from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dawki/', views.dawki_list, name="dawki_list")
]