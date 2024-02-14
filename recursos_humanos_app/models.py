from django.db import models

# Create your models here.

from django.db import models

class Direccion(models.Model):
    provincia = models.CharField(max_length=100)
    municipio = models.CharField(max_length=100)
    calle = models.CharField(max_length=255)
    numero = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.calle} {self.numero}, {self.municipio}, {self.provincia}"

class Trabajador(models.Model):
    nombre = models.CharField(max_length=100)
    carnet_identidad = models.CharField(max_length=20, unique=True)
    direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class TrabajadorNoDocente(Trabajador):
    NIVEL_ESCOLARIDAD_CHOICES = (
        ('9no', '9no grado'),
        ('Tecnico', 'Técnico Medio'),
        ('12mo', '12mo grado'),
        ('Universitario', 'Universitario'),
    )
    OCUPACION_CHOICES = (
        ('Admin', 'Administrador'),
        ('TCI', 'TCI'),
        ('AuxServicios', 'Auxiliar de Servicios'),
    )
    nivel_escolaridad = models.CharField(max_length=20, choices=NIVEL_ESCOLARIDAD_CHOICES)
    ocupacion = models.CharField(max_length=50, choices=OCUPACION_CHOICES)

class TrabajadorDocente(Trabajador):
    CATEGORIA_DOCENTE_CHOICES = (
        ('Instructor', 'Instructor'),
        ('Asistente', 'Asistente'),
        ('Auxiliar', 'Auxiliar'),
        ('Titular', 'Titular'),
    )
    CATEGORIA_CIENTIFICA_CHOICES = (
        ('Master', 'Máster'),
        ('Doctor', 'Doctor'),
    )
    categoria_docente = models.CharField(max_length=50, choices=CATEGORIA_DOCENTE_CHOICES)
    categoria_cientifica = models.CharField(max_length=50, choices=CATEGORIA_CIENTIFICA_CHOICES)
