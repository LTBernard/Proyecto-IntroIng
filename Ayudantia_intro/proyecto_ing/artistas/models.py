from django.db import models

class Artista(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    artista_nombre_artistico = models.CharField(max_length=50) 
    artista_verificado = models.BooleanField()

    def __str__(self):
        return f'{self.id}, {self.nombre}, {self.email}, {self.password}, {self.usuario_suscripcion_activa}, {self.artista_nombre_artistico}, {self.artista_verificado}, {self.tipo_de_persona}'

# Create your models here.
class Cancion(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    letra = models.CharField(max_length=300)
    fecha_composicion = models.DateField()
    id_artista =  models.ForeignKey(Artista, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.id,self.nombre,self.letra,self.fecha_composicion,self.id_artista}'



