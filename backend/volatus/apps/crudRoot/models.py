from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from simple_history.models import HistoricalRecords


# Create your models here.
class InfoRoot(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

class UsuarioManager(BaseUserManager):
    def _create_user(self, username, DNI, nombre, apellido, password, fecha_de_nacimiento, lugar_de_nacimiento, direccion_de_facturacion, genero, correo_electronico, imagen_de_usuario, is_active, is_staff, is_superuser, **extra_fields):
        user = self.model(
            DNI = DNI,
            username = username,
            nombre = nombre,
            apellido = apellido,
            fecha_de_nacimiento = fecha_de_nacimiento,
            lugar_de_nacimiento = lugar_de_nacimiento,
            direccion_de_facturacion = direccion_de_facturacion,
            genero = genero,
            correo_electronico = correo_electronico,
            imagen_de_usuario = imagen_de_usuario,
            is_active = is_active,
            is_staff = is_staff,
            is_superuser = is_superuser,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, username, DNI, nombre, apellido, fecha_de_nacimiento = None, lugar_de_nacimiento = None, direccion_de_facturacion = None, genero = None, correo_electronico = None, imagen_de_usuario = None, password = None, **extra_fields):
        return self._create_user(username, DNI, nombre, apellido, password, fecha_de_nacimiento, lugar_de_nacimiento, direccion_de_facturacion, genero, correo_electronico, imagen_de_usuario, is_active = True, is_staff = False, is_superuser = False, **extra_fields)

    def create_superuser(self, username, DNI, nombre, apellido, password = None, **extra_fields):
        return self._create_user(username, DNI, nombre, apellido, password, fecha_de_nacimiento = None, lugar_de_nacimiento = None, direccion_de_facturacion = None, genero = None, correo_electronico = None, imagen_de_usuario = None, is_active = True, is_staff = True, is_superuser = True, **extra_fields)

class Usuario(AbstractBaseUser, PermissionsMixin):
    DNI = models.CharField('Identificación',primary_key=True, unique = True, max_length=11)
    nombre = models.CharField('Nombres',max_length=100, blank = False, null = False)
    apellido = models.CharField('Apellidos',max_length=100, blank = False, null = False)
    username = models.CharField('Nombre de usuario', unique = True, max_length=20)
    #Usuario cliente
    fecha_de_nacimiento = models.DateField('Fecha de nacimiento', auto_now=False, auto_now_add=False, blank = False, null = True)
    lugar_de_nacimiento = models.CharField('Lugar de nacimiento',max_length=50, blank = False, null = True)
    direccion_de_facturacion = models.CharField('Dirección de facturación',max_length=50, blank = False, null = True)
    genero = models.CharField('Género',max_length=20, blank = False, null = True)
    correo_electronico = models.EmailField(blank = False, null = True)
    imagen_de_usuario = models.ImageField('Imagen del usuario', upload_to='crudRoot/', blank = True, null = True)

    #Info general

    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)
    historical = HistoricalRecords()
    objects = UsuarioManager()




    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['DNI', 'nombre', 'apellido']

    def __str__(self):
        return f'{self.nombre} {self.apellido}'


class Cliente(Usuario):
    rol = models.CharField('Rol',max_length=20, default = 'Cliente')

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return f'{self.nombre} {self.apellido}'

class Administrador(Usuario):
    rol = models.CharField('Rol',max_length=20, default = 'Administrador')

    class Meta:
        verbose_name = 'Administrador'
        verbose_name_plural = 'Administradores'

    def __str__(self):
        return f'{self.nombre} {self.apellido}'
