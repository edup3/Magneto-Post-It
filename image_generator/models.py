from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator, MaxValueValidator
import os


Empleador = get_user_model() 

# Create your models here.
class Vacante(models.Model):
    def __str__(self) -> str:
        return f'{self.empleador.get_username()},id({self.id}) : {self.nombre_vacante}'
    nombre_vacante = models.CharField(max_length=255)
    descripcion = models.TextField()
    disponibles = models.IntegerField()
    salario = models.IntegerField()
    ubicacion = models.TextField()
    requisitos = models.TextField()
    imagen = models.ImageField(null=True,upload_to='images/')
    empleador = models.ForeignKey(Empleador, on_delete=models.CASCADE)

class Usuario(models.Model):
    def __str__(self) -> str:
        return f'{self.user.get_username()}'

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(null= True, upload_to='pp/', validators = [
        FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'gif'])
        ])
    colors = models.CharField(max_length=100, null=True)
