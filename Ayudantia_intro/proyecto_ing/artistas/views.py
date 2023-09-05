from django.shortcuts import render
from .models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader


def index(request):
    return render(request,"ind.html")

def getArtista(request,id=0):
    if (id>0):
        artistas = list(Artista.objects.filter(id=id).values())
        return render(request,"Principal.html",{"artistas":artistas})
    else:
        artistas = list(Artista.objects.values())
        return render(request,"Principal.html",{"artistas":artistas})
    
#Insertar artistas
def input(request):
    plantilla = loader.get_template('Crear_registro.html')
    return HttpResponse(plantilla.render({}, request))

def postArtista(request):
    nombre = request.POST['nombre']
    email = request.POST['email']
    password = request.POST['password']
    artista_nombre_artistico = request.POST['artista_nombre_artistico']
    #artista_verificado = request.POST['artista_verificado']
    artista = Artista(nombre=nombre,email=email,password=password,artista_nombre_artistico=artista_nombre_artistico,artista_verificado=True)
    artista.save()
    return HttpResponseRedirect(reverse('getArtista'))

#Actualizar datos de artista 
def putArtista(request,id):
    artista = Artista.objects.get(id=id)
    plantilla = loader.get_template('Cambiar_registro.html')
    context = {
        'artista' : artista,
    }
    return HttpResponse(plantilla.render(context, request))

def putRegistroArtista(request,id):
    nombre = request.POST['nombre']
    email = request.POST['email']
    nombre_artistico = request.POST['artista_nombre_artistico']
    artista = Artista.objects.get(id=id)
    artista.nombre = nombre
    artista.email = email
    artista.artista_nombre_artistico = nombre_artistico
    artista.save()
    return HttpResponseRedirect(reverse('getArtista'))

def deleteArtista(request,id):
    artista = Artista.objects.get(id=id)
    artista.delete()
    return HttpResponseRedirect(reverse('getArtista'))


def getCanciones(request,id=0):
    if (id>0):
        canciones = list(Cancion.objects.filter(id=id).values())
        return render(request,"Principal_canciones.html",{"canciones":canciones})
    else:
        canciones = list(Cancion.objects.values())
        return render(request,"Principal_canciones.html",{"canciones":canciones})

def inputCanciones(request):
    plantilla = loader.get_template('Crear_registro_cancion.html')
    return HttpResponse(plantilla.render({}, request))
    
def postCancion(request):
    nombre = request.POST['nombre']
    letra = request.POST['letra']
    fecha_composicion = request.POST['fecha_composicion']
    id_artista = request.POST['id_artista']
    cancion = Cancion(nombre=nombre,letra=letra,fecha_composicion=fecha_composicion,id_artista_id=id_artista)
    cancion.save()
    return HttpResponseRedirect(reverse('getCanciones'))

def putCancion(request,id):
    cancion = Cancion.objects.get(id=id)
    plantilla = loader.get_template('Cambiar_registro_cancion.html')
    context = {
        'cancion' : cancion,
    }
    return HttpResponse(plantilla.render(context, request))

def putRegistroCancion(request,id):
    nombre = request.POST['nombre']
    letra = request.POST['letra']
    fecha_composicion = request.POST['fecha_composicion']
    id_artista = request.POST['id_artista']
    cancion = Cancion.objects.get(id=id)
    cancion.nombre = nombre
    cancion.letra = letra
    cancion.fecha_composicion = fecha_composicion
    cancion.id_artista_id = id_artista
    cancion.save()
    return HttpResponseRedirect(reverse('getCanciones'))

def deleteCancion(request,id):
    cancion = Cancion.objects.get(id=id)
    cancion.delete()
    return HttpResponseRedirect(reverse('getCanciones'))
