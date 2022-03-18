from django.db import models
from django.forms import ModelForm, widgets
from gestion_usuarios.models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms.widgets import DateInput
import pytz
from datetime import datetime
GENEROS=(
    ('M','M'),
    ('F','F')
)

ciudades_capitales=[
            ('Leticia', 'Leticia'),
            ('Medellín', 'Medellín'),
            ('Arauca','Arauca'),
            ('Barranquilla', 'Barranquilla'),
            ('Cartagena de Indias','Cartagena de Indias'),
            ('Tunja','Tunja'),
            ('Manizales','Manizales'),
            ('Florencia','Florencia'),
            ('Yopal','Yopal'),
            ('Popayán','Popayán'),
            ('Valledupar','Valledupar'), 
            ('Quibdó','Quibdó'),
            ('Montería','Montería'),
            ('Bogotá','Bogotá'),
            ('Inírida','Inírida'),
            ('San José del Guaviare','San José del Guaviare'),
            ('Neiva','Neiva'),
            ('Riohacha','Riohacha'),
            ('Santa Marta','Santa Marta'),
            ('Villavicencio','Villavicencio'),
            ('Pasto','Pasto'),
            ('Cúcuta','Cúcuta'),
            ('Mocoa','Mocoa'),
            ('Armenia','Armenia'),
            ('Pereira','Pereira'),
            ('San Andrés','San Andrés'),
            ('Bucaramanga','Bucaramanga'),
            ('Sincelejo','Sincelejo'),
            ('Ibagué','Ibagué'),
            ('Cali','Cali'),
            ('Mitú','Mitú'),
            ('Puerto Carreño','Puerto Carreño'),
        ]
def has_numbers(inputString):
    return any(char.isdigit() for char in inputString)

class FormCliente(ModelForm):
    class Meta:
        model= Clientes
        fields=['DNI','genero', 'fecha_nacimiento', 'lugar_nacimiento', 'direccion']

        labels={
            'DNI':'DNI',
            'genero':'Genero',
            'fecha_nacimiento':'Fecha de nacimiento mm/dd/yy',
            'lugar_nacimiento':'Lugar de nacimiento',
            'direccion':'Direccion'
        }

        widgets={
            'genero':forms.Select(choices=GENEROS),
            'lugar_nacimiento':forms.Select(choices=ciudades_capitales),
            'fecha_nacimiento':forms.DateInput(format='%d/%m/%Y', attrs={'type': 'date'},),
        }
    
    def clean (self):
        # Los datos capturados por el formulario Erroneos o no, son limpiados.
        # Fijese en no cambiar los datos del formulario directamente desde el metodo self.
        super(FormCliente, self).clean()

        # Se optienen los diferentes campos a validar.
        DNI  = self.cleaned_data.get('DNI')
        fecha_nacimiento       = self.cleaned_data.get('fecha_nacimiento')

        # Se obtiene la longitud del DNI
        long_DNI=len(str(DNI))

        # se calcula la edad del cliente a fecha de hoy.
        years_old=datetime.now().year-fecha_nacimiento.year


        #Validaciones

        #Se valida que el DNI tenga entre 8 y 10 caracteres
        if long_DNI < 8 or long_DNI> 10:
            self._errors['DNI'] = self.error_class([
                'Longitud del DNI invalida'])

        #Se valida que el DNI tenga entre 18 y 100 años
        if years_old >= 101:
            self._errors['fecha_nacimiento'] = self.error_class([
                'Edad superior a 100 años'])
        elif years_old <18:
            self._errors['fecha_nacimiento'] = self.error_class([
                'Edad inferior a 18 años'])

        
        return self.cleaned_data
        


class FormUser(UserCreationForm):
    class Meta:
        model=User
        fields=['username','password1', 'password2', 'first_name','last_name', 'email']

        labels={
            'username':'Usuario',
            'password1':'Password1',
            'password2':'Password2',
            'first_name': 'Nombre',
            'last_name':'Apellido',
            'email':'Correo'
        }

        widgets={
            'password1':forms.PasswordInput(),
            'password2':forms.PasswordInput()
        }

    def clean (self):
        # Los datos capturados por el formulario Erroneos o no, son limpiados.
        # Fijese en no cambiar los datos del formulario directamente desde el metodo self.
        super(FormUser, self).clean()

        # Se optienen los diferentes campos a validar.
        nombre      = self.cleaned_data.get('first_name')
        apellido    = self.cleaned_data.get('last_name')

        #Validaciones

        #Se valida que el DNI tenga entre 8 y 10 caracteres
        if len(nombre)<=3:
            self._errors['first_name'] = self.error_class([
                'Nombre demasiado corto'])
        elif len (nombre)>20:
            self._errors['first_name'] = self.error_class([
                'Nombre demasiado largo'])
        
        if nombre.isnumeric():
            self._errors['first_name'] = self.error_class([
                'El nombre no pueden ser numeros'])

        if has_numbers(nombre):
            self._errors['first_name'] = self.error_class([
                'El nombre no pueden ser numeros'])

        if len(apellido)<=3:
            self._errors['last_name'] = self.error_class([
                'Apellido demasiado corto'])
        elif len (apellido)>20:
            self._errors['last_name'] = self.error_class([
                'Apellido demasiado largo'])
        
        if apellido.isnumeric():
            self._errors['last_name'] = self.error_class([
                'El apellido no pueden ser numeros'])
        
        if has_numbers(apellido):
            self._errors['last_name'] = self.error_class([
                'El apellido no pueden ser numeros'])

        
        return self.cleaned_data

        

class FormAdministrador(ModelForm):
    class Meta:
        model=Administradores
        fields=['DNI','genero', 'fecha_nacimiento', 'lugar_nacimiento']

        labels={
            'DNI':'DNI',
            'genero':'Genero',
            'fecha_nacimiento':'Fecha de nacimienton mm/dd/yy',
            'lugar_nacimiento':'Lugar de nacimiento',
        }

        widgets={
            'genero':forms.Select(choices=GENEROS),
            'lugar_nacimiento':forms.Select(choices=ciudades_capitales),
            'fecha_nacimiento':DateInput()
        }
            
        