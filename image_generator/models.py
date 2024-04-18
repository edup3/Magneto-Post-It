from django.db import models
from django.contrib.auth import get_user_model

Empleador = get_user_model() 

# Create your models here.
class Vacante(models.Model):
    def __str__(self) -> str:
        return f'{self.empleador.get_username()}: {self.nombre_vacante}'
    nombre_vacante = models.CharField(max_length=255)
    descripcion = models.TextField()
    disponibles = models.IntegerField()
    salario = models.IntegerField()
    ubicacion = models.TextField()
    requisitos = models.TextField()
    imagen = models.ImageField(null=True,upload_to='images/')
    empleador = models.ForeignKey(Empleador, on_delete=models.CASCADE)


