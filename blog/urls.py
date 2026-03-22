
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path("saludo/<str:Username>/<int:id>", views.helloWorld),
    path('about/<str:username>/', views.about),
    path('projects/', views.projects),
    path('tasks/', views.tasks),
    path('toggle_task/<int:task_id>/', views.toggle_task, name='toggle_task'),
    path('delete_task/<int:task_id>/', views.delete_task, name='delete_task'),
]
