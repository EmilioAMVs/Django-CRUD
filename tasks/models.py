from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    completado = models.BooleanField(default=False)
    creado = models.DateTimeField(auto_now_add=True)
    fechacompletado = models.DateTimeField(null=True, blank=True)
    importante = models.BooleanField(default=False)
    usuario = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.titulo + ' by ' + str(self.usuario)