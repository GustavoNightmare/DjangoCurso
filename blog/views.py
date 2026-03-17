from django.shortcuts import render
from django.http import HttpResponse, HttpRequest


def helloWorld(request, username="Invitado"):
    return HttpResponse(f'<h1>Hola, {username} , como te encuentras hoy?</h1>')


def Suma(request):
    listaNumeros = [3, 4, 7, 6, 7, 9, 4, 2, 10]
    suma = 0
    for numero in listaNumeros:
        suma += numero
    mensaje = f"<h1> El numero resultado de la suma es = {suma} </h1>"
    return HttpResponse(mensaje)


# Create your views here.
