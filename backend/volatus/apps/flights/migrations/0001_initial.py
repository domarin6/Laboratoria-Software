# Generated by Django 4.0.3 on 2022-05-26 01:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryFlight',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('modified_date', models.DateField(auto_now=True, verbose_name='Fecha de Modificación')),
                ('deleted_date', models.DateField(auto_now=True, verbose_name='Fecha de Eliminación')),
                ('description', models.CharField(max_length=50, unique=True, verbose_name='Descripcion')),
                ('capacidad_pasajeros', models.IntegerField(verbose_name='Capacidad de pasajeros')),
                ('tipo', models.CharField(blank=True, max_length=20, verbose_name='Solo ida o ida-vuelta')),
            ],
            options={
                'verbose_name': 'Categoría de vuelo',
                'verbose_name_plural': 'Categorías de vuelos',
            },
        ),
        migrations.CreateModel(
            name='HistoricalFlight',
            fields=[
                ('id', models.BigIntegerField(blank=True, db_index=True)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de Creación')),
                ('modified_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de Modificación')),
                ('deleted_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de Eliminación')),
                ('fecha', models.DateField()),
                ('hora', models.DateTimeField()),
                ('origen', models.CharField(max_length=20, verbose_name='origen')),
                ('destino', models.CharField(max_length=20, verbose_name='destino')),
                ('tiempo_vuelo', models.CharField(max_length=20, verbose_name='tiempo_vuelo')),
                ('hora_llegada', models.DateTimeField()),
                ('costo', models.BigIntegerField()),
                ('disponibilidad', models.BooleanField(default=True)),
                ('image', models.TextField(blank=True, max_length=100, null=True, verbose_name='Imagen del Vuelo')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('categoria', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='flights.categoryflight', verbose_name='Categoria de vuelo')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Flight',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalCategoryFlight',
            fields=[
                ('id', models.BigIntegerField(blank=True, db_index=True)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de Creación')),
                ('modified_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de Modificación')),
                ('deleted_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de Eliminación')),
                ('description', models.CharField(db_index=True, max_length=50, verbose_name='Descripcion')),
                ('capacidad_pasajeros', models.IntegerField(verbose_name='Capacidad de pasajeros')),
                ('tipo', models.CharField(blank=True, max_length=20, verbose_name='Solo ida o ida-vuelta')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Categoría de vuelo',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('modified_date', models.DateField(auto_now=True, verbose_name='Fecha de Modificación')),
                ('deleted_date', models.DateField(auto_now=True, verbose_name='Fecha de Eliminación')),
                ('fecha', models.DateField()),
                ('hora', models.DateTimeField()),
                ('origen', models.CharField(max_length=20, verbose_name='origen')),
                ('destino', models.CharField(max_length=20, verbose_name='destino')),
                ('tiempo_vuelo', models.CharField(max_length=20, verbose_name='tiempo_vuelo')),
                ('hora_llegada', models.DateTimeField()),
                ('costo', models.BigIntegerField()),
                ('disponibilidad', models.BooleanField(default=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='flights/', verbose_name='Imagen del Vuelo')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flights.categoryflight', verbose_name='Categoria de vuelo')),
            ],
            options={
                'verbose_name': 'Flight',
                'verbose_name_plural': 'Flights',
            },
        ),
    ]
