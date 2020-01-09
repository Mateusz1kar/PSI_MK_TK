from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dawki/', views.dawki_list.as_view(), name="dawki_list"),
    path('dawki/<int:pk>/',views.dawki_detail.as_view(), name='dawki_show'),

    path('grupyZywieniowe/', views.grupyZywieniowe_list.as_view(), name="grupyZywieniowe_list"),
    path('grupyZywieniowe/<int:pk>/', views.grupyZywieniowe_detail.as_view(), name='grupyZywieniowe_show'),

    path('krowy/', views.krowy_list.as_view(), name="krowy_list"),
    path('krowy/<int:pk>/', views.krowy_detail.as_view(), name='krowy_show'),

    path('krycia/', views.krycia_list.as_view(), name="krycia_list"),
    path('krycia/<int:pk>/', views.krycia_detail.as_view(), name='krycia_show'),

    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('api-auth/', include('rest_framework.urls'))
]