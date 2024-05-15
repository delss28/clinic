from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout, name='logout'),
    path('login/', views.login, name='login'),
]
