from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('singup/', views.signup, name='singup'),
    path('delete/', views.delete, name='delete'),
    path('update/', views.update, name='update'),
    path('<int:user_pk>/follow/', views.follow, name='follow'),
    path('password/', views.change_password, name='change_password'),
    path('profile/<username>/', views.profile, name='profile'),
]