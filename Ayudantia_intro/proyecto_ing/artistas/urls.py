from django.urls import path
from .views import *

urlpatterns = [
    path('', index ,name='index'),
    #Ver todas las personas
    path('artistas/', getArtista,name='getArtista'),
    #Ver persona por id 
    path('artistas/<int:id>', getArtista,name='getArtista'),
    #Crear Persona
    path('artistas/crear/', input ,name='inputArtista'),
    #Redireccionar
    path('artistas/crear/redirect/', postArtista, name='postArtista'),
    #Cambiar una persona
    path('artistas/cambiar/<int:id>', putArtista, name='updateArtista'),

    path('artistas/cambiar/cambiar_registro/<int:id>', putRegistroArtista, name='updateRegistro'),

    path('artistas/borrar/<int:id>', deleteArtista, name='deleteArtista'),

    path('canciones/', getCanciones, name='getCanciones'),

    path('canciones/crear/', inputCanciones, name='inputCanciones'),
    
    path('canciones/crear/redirect/', postCancion, name='postCancion'),

     path('canciones/cambiar/<int:id>', putCancion, name='updateCancion'),

    path('canciones/cambiar/cambiar_registro/<int:id>', putRegistroCancion, name='updateRegistroCancion'),

    path('canciones/borrar/<int:id>', deleteCancion, name='deleteCancion'),
]