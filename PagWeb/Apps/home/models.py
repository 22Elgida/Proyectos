from django.db import models

# Create your models here.

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    creacion = models.DateField(auto_now_add=True)

    def __str__(self):
        return '%s %s' % (self.nombre, self.apellido)


class Administrador(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    creacion = models.DateField(auto_now_add=True)
    Estudiante = models.ManyToManyField(Estudiante)

    def __str__(self):
        return '%s %s' % (self.nombre, self.apellido)