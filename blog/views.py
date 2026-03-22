from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, JsonResponse
from .models import Project
from .models import Task
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
import json


def index(request):
    title = "Bienvenidos a mi blog"
    pie = "Copyright 2024 Gustavo"
    return render(request, 'index.html', {
        'title': title,
        'pie': pie
    })


def helloWorld(request, Username="Papucho", id=0):
    return HttpResponse(f'<h1>Hola mundo, digo digo , Hola {Username}, veo que tu id es {id} </h1>')


def Suma(request, username="Usuario"):
    listaNumeros = [3, 4, 7, 6, 7, 9, 4, 2, 10]
    suma = 0
    for numero in listaNumeros:
        suma += numero
    mensaje = f"<h1> El numero resultado de la suma es = {suma} , gracias por usar el servicio {username} </h1>"
    return HttpResponse(mensaje)


def projects(request):
   # proyecto = list(Project.objects.values())
    projects = Project.objects.all()
    return render(request, "project.html", {
        'projects': projects
    })
    # return JsonResponse(proyecto, safe=False)


def tasks(request):
    # task=Task.objects.get(id=id)
  # task = get_object_or_404(Task, id=id)
    tasks = Task.objects.all()
    return render(request, "task.html", {
        'tasks': tasks
    })
    # return HttpResponse(f"La tarea que se selecionó es : {task.title }, con descripcion : {task.description}, y proyecto : {task.projects}")
# Create your views here.


def about(request, username="Gustavo"):
    return render(request, "about.html")


@csrf_exempt
def toggle_task(request, task_id):
    if request.method == 'POST':
        task = get_object_or_404(Task, id=task_id)
        task.done = not task.done
        task.save()
        return JsonResponse({'done': task.done})
    return JsonResponse({'error': 'Invalid request'}, status=400)


@csrf_exempt
def delete_task(request, task_id):
    if request.method == 'POST':
        task = get_object_or_404(Task, id=task_id)
        task.delete()
        return JsonResponse({'deleted': True})
    return JsonResponse({'error': 'Invalid request'}, status=400)
