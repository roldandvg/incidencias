# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from incidencias.apps.comun.models import Parroquia, Persona


class Cargo(models.Model):
    cargo = models.CharField(max_length=30)

    def __unicode__(self):
        return self.cargo

    class Meta:
        ordering = ["cargo"]
        verbose_name = "Cargo"
        verbose_name_plural = "Cargos"


class Rango(models.Model):
    rango = models.CharField(max_length=30)

    def __unicode__(self):
        return self.rango

    class Meta:
        ordering = ["rango"]
        verbose_name = "Rango"
        verbose_name_plural = "Rangos"


class Estacion(models.Model):
    nombre = models.CharField(max_length=60)
    detalle = models.CharField(max_length=120)
    telefono = models.CharField(max_length=15)
    jefe = models.CharField(max_length=45)
    direccion = models.CharField(max_length=255, blank=True)
    parroquia = models.ForeignKey(Parroquia)

    def __unicode__(self):
        return self.nombre

    class Meta:
        ordering = ["nombre"]
        verbose_name = 'Estación'
        verbose_name_plural = 'Estaciones'


class Trabajador(models.Model):
    persona = models.ForeignKey(Persona)
    cargo = models.ForeignKey(Cargo)
    rango = models.ForeignKey(Rango, null=True)
    estacion = models.ForeignKey(Estacion)
    usuario = models.ForeignKey(User, null=True)

    def __unicode__(self):
        return self.persona

    class Meta:
        ordering = ["estacion", "cargo", "persona"]
        verbose_name = "Trabajador"
        verbose_name_plural = "Trabajadores"


class Unidad(models.Model):
    numero = models.CharField(max_length=10)
    modelo = models.CharField(max_length=45)

    def __unicode__(self):
        return self.numero + ' ' + self.modelo

    class Meta:
        ordering = ["numero", "modelo"]
        verbose_name = 'Unidad'
        verbose_name_plural = 'Unidades'