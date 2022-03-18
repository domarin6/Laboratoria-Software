from django import forms
from django.db.models import fields
from django.forms import widgets
from django.forms.models import ModelForm
from compras_reservas.models import Viajero
from gestion_vuelos.models import *
from django.forms.widgets import  *
from datetime import datetime

GENEROS=(
    ('M','M'),
    ('F','F')
)

CLASE=(
    ('1','Ejecutiva'),
    ('0','Primera clase')
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


class ReservaForm(ModelForm):
    class Meta:
        model=Viajero
        exclude = ['silla','check_in']

        widgets={
            'genero':forms.Select(choices=GENEROS),
            'fecha_nacimiento':forms.DateInput(format='%d/%m/%Y', attrs={'type': 'date'},),
            'lugar_nacimiento':forms.Select(choices=ciudades_capitales),
            'clase':forms.Select(choices=CLASE)
        }

    def clean (self):
        # Los datos capturados por el formulario Erroneos o no, son limpiados.
        # Fijese en no cambiar los datos del formulario directamente desde el metodo self.
        super(ReservaForm, self).clean()

        # Se optienen los diferentes campos a validar.
        DNI=self.cleaned_data.get('DNI')
        direccion=self.cleaned_data.get('direccion')
        fecha_nacimiento=self.cleaned_data.get('fecha_nacimiento')
        nombre_contacto=self.cleaned_data.get('nombre_contacto')
        telefono_contacto=self.cleaned_data.get('telefono_contacto')
        acompañante=self.cleaned_data.get('acompañante')

        # Se obtiene la longitud del DNI
        long_DNI=len(str(DNI))
        long_direccion=len(str(direccion))
        long_nombre_contacto=len(nombre_contacto)
        long_telefono_contacto=len(telefono_contacto)

        # se calcula la edad del cliente a fecha de hoy.
        years_old=datetime.now().year-fecha_nacimiento.year


        #Validaciones

        #Se valida que el DNI tenga entre 8 y 10 caracteres
        #se valida la longitud del nombre
        #se valida la longitud del telefono o celular
        if long_direccion < 5 or long_direccion> 150:
            #self.add_error('direccion','Longitud de la direccion invalida' )
            self._errors['direccion'] = self.error_class([
                'Longitud de la direccion invalida'])


        if long_DNI < 8 or long_DNI> 10:
            #self.add_error('DNI','Longitud del DNI invalida' )
            self._errors['DNI'] = self.error_class([
                'Longitud del DNI invalida'])

        if long_nombre_contacto < 4 or long_nombre_contacto> 20:
            #self.add_error('nombre_contacto','Longitud del nombre invalida' )
            self._errors['nombre_contacto'] = self.error_class([
                'Longitud del nombre invalida'])
        
        if long_telefono_contacto < 7 or long_telefono_contacto > 12:
            #self.add_error('telefono_contacto','Longitud del Telefono invalida' )
            self._errors['telefono_contacto'] = self.error_class([
                'Longitud del Telefono invalida'])

        #Se valida que los años tengan entre 18 y 100 años
        if years_old >= 101:
            #self.add_error('fecha_nacimiento','Edad superior a 100 años' )
            self._errors['fecha_nacimiento'] = self.error_class([
                'Edad superior a 100 años'])

        elif years_old <18 and acompañante is None :
            #self.add_error('fecha_nacimiento','Edad inferior a 18 años')
            self._errors['acompañante'] = self.error_class([
                'Ingresar la cedula del acompañante'])

        #valida que es mayor de edad, sino le pide obligatoriamente el campo acompañante
      
        return self.cleaned_data

