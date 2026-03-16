
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index ),
    path("saludo/<str:Username>/", views.helloWorld),
    path('about/<str:username>/', views.Suma ),
]