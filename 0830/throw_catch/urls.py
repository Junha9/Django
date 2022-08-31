from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'throw_catch'
urlpatterns = [
    path('first/', views.first, name = 'first'),
    path('second/', views.second, name = 'second'),
]
