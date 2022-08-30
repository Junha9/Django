from django.urls import path
from . import views
urlpatterns = [
    path('index/', views.index, name='index'),
    path('meat/', views.meat, name='meat'),
    path('dtl/', views.dtl, name='dtl'),
    path('throw/', views.throw, name='throw'),
    path('catch/', views.catch, name = 'catch'),
    path('hello/<str:name>/', views.hello, name = 'hello')
]