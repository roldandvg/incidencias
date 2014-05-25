# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

from incidencias.apps.comun.models import TipoProcedimiento, Comision, Persona, Parroquia
from incidencias.apps.institucion.models import Estacion, Unidad


# Create your models here.
class Diagnostico(models.Model):
    nombre = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=255)

    def __unicode__(self):
        return self.nombre

    class Meta:
        ordering = ["nombre"]
        verbose_name = 'Diagnóstico'
        verbose_name_plural = 'Diagnósticos'


class PersonaAtendida(Persona):
    diagnostico = models.ManyToManyField(Diagnostico)
    lesionado = models.NullBooleanField(null=True)
    fallecido = models.NullBooleanField(null=True)


class DetallePersona(models.Model):
    posicion = models.CharField(max_length=45)
    dias_desaparecido = models.SmallIntegerField()
    causa_muerte = models.CharField(max_length=255, blank=True, null=True)
    camisa = models.CharField(max_length=45)
    pantalon = models.CharField(max_length=45)
    zapatos = models.CharField(max_length=45)
    observacion = models.CharField(max_length=255)
    persona = models.ForeignKey(PersonaAtendida)

    def __unicode__(self):
        return self.persona

    class Meta:
        ordering = ["dias_desaparecido"]
        verbose_name = "Detalle de Persona"
        verbose_name_plural = "Detalles de Personas"


class Novedad(models.Model):
    fecha = models.DateField()
    hora_salida = models.TimeField()
    hora_llegada = models.TimeField()
    hora_reporte = models.TimeField()
    lugar = models.CharField(max_length=255)
    motivo = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=255)
    procedimiento = models.CharField(max_length=255)
    alarma_infundada = models.BooleanField(default=False)
    acto_presencia = models.BooleanField(default=False)
    parroquia = models.ForeignKey(Parroquia)
    tipo_procedimiento = models.ForeignKey(TipoProcedimiento)
    usuario = models.ForeignKey(User)  # input hidden en template con value default request.username
    unidad = models.ManyToManyField(Unidad)
    comision = models.ManyToManyField(Comision)
    persona = models.ManyToManyField(PersonaAtendida)

    def __unicode__(self):
        return self.motivo

    class Meta:
        ordering = ["fecha", "lugar", "tipo_procedimiento"]
        verbose_name = 'Novedad'
        verbose_name_plural = 'Novedades'


class Cilindro(models.Model):
    color = models.CharField(max_length=45)
    kilogramo = models.DecimalField(max_digits=10, decimal_places=2)
    empresa = models.CharField(max_length=45)
    ubicacion = models.CharField(max_length=45)
    novedad = models.ForeignKey(Novedad)

    def __unicode__(self):
        return self.empresa

    class Meta:
        ordering = ["empresa", "kilogramo"]
        verbose_name = 'Cilindro'
        verbose_name_plural = 'Cilindros'


class Vehiculo(models.Model):
    placa = models.CharField(max_length=10)
    marca = models.CharField(max_length=45)
    color = models.CharField(max_length=20)
    anno = models.CharField(max_length=4)
    modelo = models.CharField(max_length=45)
    novedad = models.ForeignKey(Novedad)

    def __unicode__(self):
        return self.placa

    class Meta:
        ordering = ["marca", "modelo", "placa"]
        verbose_name = "Vehículo"
        verbose_name_plural = "Vehículos"


class VehiculoPersona(models.Model):
    tipo = models.CharField(max_length=1)
    observacion = models.CharField(max_length=255)
    vehiculo = models.ForeignKey(Vehiculo)
    persona = models.ForeignKey(Persona)

    def __unicode__(self):
        return self.tipo

    class Meta:
        ordering = ["tipo"]
        verbose_name = 'Vehículo - Persona'
        verbose_name_plural = 'Vehículos - Personas'


class Vivienda(models.Model):
    nombre = models.CharField(max_length=45)
    dannos = models.CharField(max_length=255)
    observacion = models.CharField(max_length=255)
    novedad = models.ForeignKey(Novedad)

    def __unicode__(self):
        return self.nombre

    class Meta:
        ordering = ["nombre"]
        verbose_name = 'Vivienda'
        verbose_name_plural = 'Viviendas'


class ViviendaPersona(models.Model):
    propietario = models.BooleanField(default=False)
    parentesco = models.CharField(max_length=20)
    lesionados = models.SmallIntegerField(default=0)
    fallecidos = models.SmallIntegerField(default=0)
    vivienda = models.ForeignKey(Vivienda)
    persona = models.ForeignKey(Persona)

    def __unicode__(self):
        return self.propietario

    class Meta:
        ordering = ["propietario"]
        verbose_name = 'Vivienda - Persona'
        verbose_name_plural = 'Vivienda - Personas'
