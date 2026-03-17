
from django.urls import path
from . import views

urlpatterns = [
    path('', views.helloWorld),
    path('about/', views.Suma),
    path('hello/<str:username>/', views.helloWorld),
]
