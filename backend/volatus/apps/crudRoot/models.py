from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from simple_history.models import HistoricalRecords


# Create your models here.
class InfoRoot(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

class UsuarioManager(BaseUserManager):
    def _create_user(self, username, DNI, nombre, password, is_staff, is_superuser, **extra_fields):
        user = self.model(
            DNI = DNI,
            username = username,
            nombre = nombre,
            is_staff = is_staff,
            is_superuser = is_superuser,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, username, DNI, nombre, password = None, **extra_fields):
        return self._create_user(username, DNI, nombre, password, is_staff = False, is_superuser = False, **extra_fields)

    def create_superuser(self, username, DNI, nombre, password = None, **extra_fields):
        return self._create_user(username, DNI, nombre, password, is_staff = True, is_superuser = True, **extra_fields)

class Usuario(AbstractBaseUser, PermissionsMixin):
    DNI = models.CharField('Identificación', unique = True, max_length=11)
    nombre = models.CharField('Nombres',max_length=100, blank = False, null = False)
    username = models.CharField('Nombre de usuario', unique = True, max_length=20)
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)
    historical = HistoricalRecords()
    objects = UsuarioManager()
    #password = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['DNI', 'nombre']

    def __str__(self):
        return self.nombre
