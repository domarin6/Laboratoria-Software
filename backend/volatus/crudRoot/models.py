from django.db import models

# Create your models here.


class Administradores(models.Model):
    DNI = models.CharField(max_length=11)
    nombre = models.CharField(max_length=100)
    NombreDeUsuario = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.title
