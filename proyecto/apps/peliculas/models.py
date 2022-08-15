from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Pelicula(models.Model):
    title = models.CharField(max_length=25)
    url_img = models.CharField(max_length=100)
    description = models.TextField()
    video = models.CharField(max_length=1050,null="true")

    
    def __str__(self):
        return self.title

class Comentario(models.Model):
    usuario = models.CharField(max_length=50)
    pelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE)
    comentario = models.CharField(max_length=250)

    def __str__(self):
        return self.usuario+","+str(self.pelicula)+","+self.comentario

    