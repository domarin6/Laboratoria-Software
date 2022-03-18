from django import forms
from django.forms import widgets
from gestion_vuelos.models import *
from django.forms.widgets import  DateTimeInput, Select
tipo=(
    ('internacional', 'internacional'),
    ('nacional', 'nacional'),
)

ciudades_capitalesN=(
    ('', ''),
    ('Capitales nacionales' ,(
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
    )),
)

ciudades_capitales=(
    ('', ''),
    ('Capitales nacionales' ,(
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
        ('Bogota','Bogota'),
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
    )),
    ('Capitales Internacionales' ,(
        ('Madrid', 'Madrid'),
        ('Londres', 'Londres'),
        ('New York','New York'),
        ('Buenos Aires','Buenos Aires'),

    )),
)

class FormBusqueda(forms.Form):
    tipo_vuelo = forms.CharField(max_length=20, widget=forms.Select(choices=tipo))
    fecha_vuelo= forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type':'datetime-local'}, format="%Y-%m-%d %H:%M"),)
    origen=forms.CharField(max_length=20, widget=forms.Select(choices=ciudades_capitalesN))
    destino=forms.CharField(max_length=20, widget=forms.Select(choices=ciudades_capitales))
    tiempo_Vuelo=forms.TimeField(widget=forms.TimeInput(attrs={'type':'time'}))
    fecha_llegada=forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type':'datetime-local'}, format="%Y-%m-%d %H:%M"))
    costo=forms.FloatField()
    capacidad=forms.IntegerField()
    
    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)
        self.fields['tipo_vuelo'].required = False
        self.fields['fecha_vuelo'].required = False
        self.fields['origen'].required = False
        self.fields['destino'].required = False
        self.fields['tiempo_Vuelo'].required = False
        self.fields['fecha_llegada'].required = False
        self.fields['costo'].required = False
        self.fields['capacidad'].required = False
    
