from django.urls import path
from . import views

urlpatterns = [
    path('', views.Main, name='main'),
    path('home/', views.Main, name='main'),
    path('manipulator/', views.manipulator, name='manipulator'),
]
