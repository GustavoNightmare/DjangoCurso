
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index ),
    path("saludo/<str:Username>/<int:id>", views.helloWorld),
    path('about/<str:username>/', views.about ),
    path('projects/', views.projects ),
    path('tasks/<int:id>', views.tasks ),
]