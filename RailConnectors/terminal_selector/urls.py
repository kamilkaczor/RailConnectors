from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search_terminal/', views.search_terminal, name='search_terminal'),
    path('add_terminal/', views.add_terminal, name='add_terminal'),
    path('terminals/', views.terminals, name='terminals'),
    path('no_insert/', views.no_insert, name='no_insert'),
    path('list_all_inserts/', views.list_all_inserts, name='list_all_inserts'),
    path('add_success/', views.add_success, name='add_success'),
    path('about/', views.about, name='about'),
]