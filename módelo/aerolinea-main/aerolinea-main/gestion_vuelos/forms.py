#from django.utils import timezone
from django import forms
from django.forms import ModelForm
from django.forms.widgets import  DateTimeInput, Select
from datetime import datetime
import pytz

from gestion_vuelos.models import Vuelos
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

ciudades_capitales_col=[
    ('Medellín', 'Medellín'),
    ('Cartagena de Indias','Cartagena de Indias'),
    ('Bogotá','Bogotá'),
    ('Pereira','Pereira'),
    ('Cali','Cali'),
]

ciudades_capitales_ext=[
    ('Madrid', 'Madrid'),
    ('Londres', 'Londres'),
    ('New York','New York'),
    ('Buenos Aires','Buenos Aires'),
]

class FormVueloNacional(ModelForm):
    class Meta:
        model   = Vuelos
        fields  = ['tipo_vuelo','fecha_vuelo', 'origen', 'destino', 'tiempo_Vuelo', 'costo']
        widgets = {
            'tipo_vuelo': Select(choices=
                [
                    ('nacional','nacional')
                ]
            ),

            'fecha_vuelo'   : forms.DateTimeInput(attrs={'type':'datetime-local'}, format="%Y-%m-%d %H:%M"),

            'origen'        : Select(choices=ciudades_capitales),
            'destino'       : Select(choices=ciudades_capitales),
            'tiempo_Vuelo'  : forms.TimeInput(attrs={'type':'time'})
            }

    def clean(self):

        # Los datos capturados por el formulario Erroneos o no, son limpiados.
        # Fijese en no cambiar los datos del formulario directamente desde el metodo self.
        super(FormVueloNacional, self).clean()

        # Se optienen los diferentes campos a validar.
        fecha_form  = self.cleaned_data.get('fecha_vuelo')
        costo       = self.cleaned_data.get('costo')
        origen      = self.cleaned_data.get('origen')
        destino     = self.cleaned_data.get('destino')

        # se optiene la fecha actual.
        fecha_now   = datetime.now()
        
        # Para hacer operaciones de comparacion, se formatean las fechas de igual manera.
        form_fecha  = fecha_form.replace(tzinfo=pytz.UTC)
        today       = fecha_now.replace(tzinfo=pytz.UTC)

        error_date  = datetime.now().strftime("%Y-%m-%d %H:%M")
        mensaje     ="una fecha mayor o igual a {}".format(error_date)

        # Si la fecha ingresada es menor a la fecha actual, crear un error.
        if form_fecha < today :
            self._errors['fecha_vuelo'] = self.error_class([
                mensaje])

        # Si el costo es menor o igual a cero, se crea un error.
        if costo <= 0 :
            self._errors['costo'] = self.error_class([
                'El valor no puede ser cero o menor'
            ])

        # Si el origen y el destino son iguales, se crea un error
        if origen == destino:
            self._errors['origen'] = self.error_class([
                'El origen no puede ser igual al destino'
            ])

        # Se retorna el formulario con los datos ingresados por el usuario
        # y los errores resultados de la validacion
        return self.cleaned_data



class FormVueloInternacional(ModelForm):
    class Meta:
        model   = Vuelos
        fields  = ['tipo_vuelo','fecha_vuelo', 'origen', 'destino', 'tiempo_Vuelo', 'costo']
        widgets = {
            'tipo_vuelo': Select(choices=
                [
                    ('internacional','internacional')
                ]
            ),

            'fecha_vuelo'   : forms.DateTimeInput(attrs={'type':'datetime-local'},format="%Y-%m-%d %H:%M"),

            'origen'        : Select(choices=ciudades_capitales_col),
            'destino'       : Select(choices=ciudades_capitales_ext),
            'tiempo_Vuelo'  : forms.TimeInput(attrs={'type':'time'})
            }

    def clean(self):

        # Los datos capturados por el formulario Erroneos o no, son limpiados.
        # Fijese en no cambiar los datos del formulario directamente desde el metodo self.
        super(FormVueloInternacional, self).clean()

        # Se optienen los diferentes campos a validar.
        fecha_form  = self.cleaned_data.get('fecha_vuelo')
        costo       = self.cleaned_data.get('costo')
        


        # se optiene la fecha actual.
        fecha_now   = datetime.now()
        
        # Para hacer operaciones de comparacion, se formatean las fechas de igual manera.
        form_fecha  = fecha_form.replace(tzinfo=pytz.UTC)
        today       = fecha_now.replace(tzinfo=pytz.UTC)

        error_date  = datetime.now().strftime("%Y-%m-%d %H:%M")
        mensaje     ="una fecha mayor o igual a {}".format(error_date)

        # Si la fecha ingresada es menor a la fecha actual, crear un error.
        if form_fecha < today :
            self._errors['fecha_vuelo'] = self.error_class([
                mensaje])

        # Si el costo es menor o igual a cero, se crea un error.
        if costo <= 0 :
            self._errors['costo'] = self.error_class([
                'El valor no puede ser cero o menor'
            ])


        # Se retorna el formulario con los datos ingresados por el usuario
        # y los errores resultados de la validacion
        return self.cleaned_data

class FormEdit(ModelForm):

    fecha_vuelo = forms.DateTimeField(widget=DateTimeInput(attrs={'type':'datetime-local'}),required=False)
    class Meta:
        model   =   Vuelos
        fields  =   ['tiempo_Vuelo', 'costo']
        widgets =   {
            'tiempo_Vuelo'  : forms.TimeInput(attrs={'type':'time'})
        }

    def clean(self):

        # Los datos capturados por el formulario Erroneos o no, son limpiados.
        # Fijese en no cambiar los datos del formulario directamente desde el metodo self.
        super(FormEdit, self).clean()

        # Se optienen los diferentes campos a validar.
        fecha_form  = self.cleaned_data.get('fecha_vuelo')
        costo       = self.cleaned_data.get('costo')


        # se optiene la fecha actual.
        fecha_now   = datetime.now()
        
        # Para hacer operaciones de comparacion, se formatean las fechas de igual manera
        # Aqui se valida si el usuario digito una fecha o no.
        # si no digito una fecha es porque desea conservar la fecha actual.
        if fecha_form != None:
            form_fecha  = fecha_form.replace(tzinfo=pytz.UTC)
            today       = fecha_now.replace(tzinfo=pytz.UTC)

            error_date  = datetime.now().strftime("%Y-%m-%d %H:%M")
            mensaje     ="una fecha mayor o igual a {}".format(error_date)

            # Si la fecha ingresada es menor a la fecha actual, crear un error.

            if form_fecha < today :
                self._errors['fecha_vuelo'] = self.error_class([
                    mensaje])


        # Si el costo es menor o igual a cero, se crea un error.
        if costo <= 0 :
            self._errors['costo'] = self.error_class([
                'El valor no puede ser cero o menor'
            ])

        # Se retorna el formulario con los datos ingresados por el usuario
        # y los errores resultados de la validacion
        return self.cleaned_data

