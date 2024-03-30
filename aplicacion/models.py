from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Perro(models.Model):
    sexo_opciones = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    )

    nombre = models.CharField(max_length=100)
    raza = models.CharField(max_length=100)
    sexo = models.CharField(max_length=1, choices=sexo_opciones)
    fecha_de_desaparicion = models.DateTimeField(help_text="Ingrese la fecha en el formato dd/mm/aaaa hh:mm")
    lugar_de_desaparicion = models.CharField(max_length=100)
    imagen = models.ImageField(null=True, blank= True, upload_to='imagenes_perro/')

class Celular(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    fecha_de_perdida = models.DateTimeField(help_text="Ingrese la fecha en el formato dd/mm/aaaa hh:mm")
    lugar_de_perdida = models.CharField(max_length=100)

class Zapatilla(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    talla = models.CharField(max_length=100)
    fecha_de_desaparicion = models.DateTimeField(help_text="Ingrese la fecha en el formato dd/mm/aaaa hh:mm")
    lugar_de_desaparicion = models.CharField(max_length=100)

class Auto(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    placa = models.CharField(max_length=100)
    fecha_de_desaparicion = models.DateTimeField(help_text="Ingrese la fecha en el formato dd/mm/aaaa hh:mm")
    lugar_de_desaparicion = models.CharField(max_length=100)

class Avatar(models.Model):
    imagen = models.ImageField(upload_to="avatares")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

