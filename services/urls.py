from django.urls import path
from . import views

app_name = 'services'

urlpatterns = [
    path('', views.services, name='index'),
    path('service/<slug:service_slug>/', views.service, name='service'),
]