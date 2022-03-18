from django import forms
from django.db.models.fields import IntegerField
from django.forms import ModelForm, fields
from django.forms.widgets import  DateTimeInput, HiddenInput, Select, SelectDateWidget
from datetime import datetime
import pytz

from modulo_financiero.models import TarjetaDebito, TarjetaCredito

def has_numbers(inputString):
    return any(char.isdigit() for char in inputString)

class TarjetaDebitoForm(ModelForm):
    class Meta:
        model   =   TarjetaDebito
        fields  =   ['numero', 'nombre', 'apellido', 'direccion', 'saldo']

    def clean(self):

        # Los datos capturados por el formulario Erroneos o no, son limpiados.
        # Fijese en no cambiar los datos del formulario directamente desde el metodo self.
        super(TarjetaDebitoForm, self).clean()

        # Se optienen los diferentes campos a validar.
        numero      = self.cleaned_data.get('numero')
        nombre      = self.cleaned_data.get('nombre')
        apellido    = self.cleaned_data.get('apellido')
        direccion   = self.cleaned_data.get('direccion')
        saldo       = self.cleaned_data.get('saldo')


        # Validacion del numero
        tam_numero  = len(numero)
        if not numero.isnumeric():
            self._errors['numero'] = self.error_class(
                ['Esto no es un numero']
            )
        if numero.isnumeric():
            if tam_numero != 16:
                self._errors['numero'] = self.error_class(
                    ['Son necesarios 16 digitos.']
                )

        # Validar el nombre
        tam_nombre  = len(nombre)

        if tam_nombre<=3:
            self._errors['nombre'] = self.error_class([
                'Nombre demasiado corto'])
        elif tam_nombre >20:
            self._errors['nombre'] = self.error_class([
                'Nombre demasiado largo'])
        
        if nombre.isnumeric():
            self._errors['nombre'] = self.error_class([
                'El nombre no pueden ser numeros'])

        if has_numbers(nombre):
            self._errors['nombre'] = self.error_class([
                'El nombre no pueden ser numeros'])

        # Validar apellido

        tam_apellido  = len(apellido)

        if tam_apellido<=3:
            self._errors['apellido'] = self.error_class([
                'Nombre demasiado corto'])
        elif tam_apellido >20:
            self._errors['apellido'] = self.error_class([
                'Nombre demasiado largo'])
        
        if apellido.isnumeric():
            self._errors['apellido'] = self.error_class([
                'El nombre no pueden ser numeros'])

        if has_numbers(apellido):
            self._errors['apellido'] = self.error_class([
                'El nombre no pueden ser numeros'])

        #Direccion.

        tam_direccion  = len(direccion)

        if tam_direccion<=25:
            self._errors['direccion'] = self.error_class([
                'Direccion demasiado corta'])
        elif tam_direccion >100:
            self._errors['direccion'] = self.error_class([
                'Direccion demasiado larga'])



        # Si el saldo es menor o igual a cero, se crea un error.
        if saldo < 0 :
            self._errors['saldo'] = self.error_class([
                'El valor no puede ser menor a cero'
            ])

        # Se retorna el formulario con los datos ingresados por el usuario
        # y los errores resultados de la validacion
        return self.cleaned_data


class TarjetaCreditoForm(ModelForm):
    class Meta:
        model   =   TarjetaCredito
        fields  =   ['numero', 'nombre', 'apellido', 'direccion', 'cupo', 'cvv']

    def clean(self):

        # Los datos capturados por el formulario Erroneos o no, son limpiados.
        # Fijese en no cambiar los datos del formulario directamente desde el metodo self.
        super(TarjetaCreditoForm, self).clean()

        # Se optienen los diferentes campos a validar.
        numero      = self.cleaned_data.get('numero')
        nombre      = self.cleaned_data.get('nombre')
        apellido    = self.cleaned_data.get('apellido')
        direccion   = self.cleaned_data.get('direccion')
        cupo        = self.cleaned_data.get('cupo')
        cvv         = self.cleaned_data.get('cvv')


        # Validacion del numero
        tam_numero  = len(numero)
        if not numero.isnumeric():
            self._errors['numero'] = self.error_class(
                ['Esto no es un numero']
            )
        if numero.isnumeric():
            if tam_numero != 16:
                self._errors['numero'] = self.error_class(
                    ['Son necesarios 16 digitos.']
                )

        # Validar el nombre
        tam_nombre  = len(nombre)

        if tam_nombre<=3:
            self._errors['nombre'] = self.error_class([
                'Nombre demasiado corto'])
        elif tam_nombre >20:
            self._errors['nombre'] = self.error_class([
                'Nombre demasiado largo'])
        
        if nombre.isnumeric():
            self._errors['nombre'] = self.error_class([
                'El nombre no pueden ser numeros'])

        if has_numbers(nombre):
            self._errors['nombre'] = self.error_class([
                'El nombre no pueden ser numeros'])

        # Validar apellido

        tam_apellido  = len(apellido)

        if tam_apellido<=3:
            self._errors['apellido'] = self.error_class([
                'Nombre demasiado corto'])
        elif tam_apellido >20:
            self._errors['apellido'] = self.error_class([
                'Nombre demasiado largo'])
        
        if apellido.isnumeric():
            self._errors['apellido'] = self.error_class([
                'El nombre no pueden ser numeros'])

        if has_numbers(apellido):
            self._errors['apellido'] = self.error_class([
                'El nombre no pueden ser numeros'])

        #Direccion.

        tam_direccion  = len(direccion)

        if tam_direccion<=25:
            self._errors['direccion'] = self.error_class([
                'Direccion demasiado corta'])
        elif tam_direccion >100:
            self._errors['direccion'] = self.error_class([
                'Direccion demasiado larga'])

        #validar CVV
        tam_cvv = len(str(cvv))
        if tam_cvv != 3: 
            self._errors['cvv'] = self.error_class([
                'Codigo no valido, son 3 digitos'])

        # Si el saldo es menor o igual a cero, se crea un error.
        if cupo < 0 :
            self._errors['cupo'] = self.error_class([
                'El valor no puede ser menor a cero'
            ])

        # Se retorna el formulario con los datos ingresados por el usuario
        # y los errores resultados de la validacion
        return self.cleaned_data

class EditDebitForm (ModelForm):
    class Meta:
        model   =   TarjetaDebito
        fields  =   ['numero', 'nombre', 'apellido', 'direccion', 'saldo']