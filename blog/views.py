from django.shortcuts import render
from django.http import HttpResponse,HttpRequest

def index(request):
    return HttpResponse("<h1>INDEX PAGINA HECHA CON DJANGO</h1>")
def helloWorld(request, Username="Papucho"):
    return HttpResponse(f'<h1>Hola mundo, digo digo , Hola {Username}</h1>')


def Suma(request, username="Usuario"):
    listaNumeros= [3,4,7,6,7,9,4,2,10]
    suma=0
    for numero in listaNumeros:
        suma+=numero
    mensaje= f"<h1> El numero resultado de la suma es = {suma} , gracias por usar el servicio {username} </h1>"
    return HttpResponse(mensaje)


# Create your views here.
