from django.db import models

from apps.base.models import BaseModel

class CategoryFlight(BaseModel):
    """Model definition for CategoryFlight."""

    # TODO: Define fields here
    description = models.CharField('Descripcion', max_length=50,unique = True,null = False,blank = False)
    capacidad_pasajeros = models.IntegerField('Capacidad de pasajeros')
    tipo = models.CharField('Solo ida o ida-vuelta', max_length=20, blank = True, null = False)

    class Meta:
        """Meta definition for CategoryFlight."""

        verbose_name = 'Categoría de vuelo'
        verbose_name_plural = 'Categorías de vuelos'

    def __str__(self):
        """Unicode representation of CategoryFlight."""
        return self.description





class Flight(BaseModel):
    """Model definition for Flight."""

    # TODO: Define fields here
    fecha = models.DateField()
    hora = models.DateTimeField()
    origen = models.CharField('origen',max_length=20)
    destino = models.CharField('destino',max_length=20)
    tiempo_vuelo = models.CharField('tiempo_vuelo',max_length=20)
    hora_llegada = models.DateTimeField()
    costo = models.BigIntegerField()
    categoria=models.ForeignKey(CategoryFlight,on_delete=models.CASCADE, verbose_name='Categoria de vuelo', null=False)
    disponibilidad = models.BooleanField(default = True)
    image = models.ImageField('Imagen del Vuelo', upload_to='flights/', blank=True, null=True)

    

        
    class Meta:
        """Meta definition for Flight."""

        verbose_name = 'Flight'
        verbose_name_plural = 'Flights'

    #REQUIRED_FIELDS = ['destino', 'tiempo_vuelo', 'costo']

    def __str__(self):
        """Unicode representation of Flight."""
        return f'{self.origen} {self.destino}'

    


