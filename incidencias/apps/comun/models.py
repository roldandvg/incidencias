# -*- coding: utf-8 -*-
from django.db import models


# Create your models here.
class Zona(models.Model):
    nombre = models.CharField(max_length=150)

    def __unicode__(self):
        if self.nombre.__len__() > 50:
            return self.nombre[:50] + "..."
        else:
            return self.nombre

    class Meta:
        ordering = ["nombre"]
        verbose_name = 'Zona'
        verbose_name_plural = 'Zonas'


class Municipio(models.Model):
    nombre = models.CharField(max_length=45)
    zona = models.ForeignKey(Zona)

    def __unicode__(self):
        return self.nombre

    class Meta:
        ordering = ["nombre"]
        verbose_name = 'Municipio'
        verbose_name_plural = 'Municipios'


class Parroquia(models.Model):
    nombre = models.CharField(max_length=45)
    municipio = models.ForeignKey(Municipio)

    def __unicode__(self):
        return self.nombre

    class Meta:
        ordering = ["nombre"]
        verbose_name = 'Parroquia'
        verbose_name_plural = 'Parroquias'


class Procedimiento(models.Model):
    nombre = models.CharField(max_length=45)

    def __unicode__(self):
        return self.nombre

    class Meta:
        ordering = ["nombre"]
        verbose_name = 'Procedimiento'
        verbose_name_plural = 'Procedimientos'


class TipoProcedimiento(models.Model):
    nombre = models.CharField(max_length=45)
    procedimiento = models.ForeignKey(Procedimiento)

    def __unicode__(self):
        return self.nombre

    class Meta:
        ordering = ["nombre"]
        verbose_name = 'Tipo de Procedimiento'
        verbose_name_plural = 'Tipos de Procedimientos'


class DetalleTipoProcedimiento(models.Model):
    nombre = models.CharField(max_length=45)
    tipo_procedimiento = models.ForeignKey(TipoProcedimiento)

    def __unicode__(self):
        return self.nombre

    class Meta:
        ordering = ["nombre"]
        verbose_name = 'Detalle de Tipo de Procedimiento'
        verbose_name_plural = 'Detalles de Tipos de Procedimientos'


class Comision(models.Model):
    nombre = models.CharField(max_length=45)

    def __unicode__(self):
        return self.nombre

    class Meta:
        ordering = ["nombre"]
        verbose_name = 'Comisión'
        verbose_name_plural = 'Comisiones'


class Diagnostico(models.Model):
    nombre = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=255)
    lesionado = models.NullBooleanField(null=True)
    fallecido = models.NullBooleanField(null=True)

    def __unicode__(self):
        return self.nombre

    class Meta:
        ordering = ["nombre"]
        verbose_name = 'Diagnóstico'
        verbose_name_plural = 'Diagnósticos'


class Persona(models.Model):
    nombre = models.CharField(max_length=80)
    cedula = models.CharField(max_length=10, unique=True)
    edad = models.SmallIntegerField()
    sexo = models.CharField(max_length=1, choices=[('M', 'Masculino'), ('F', 'Femenino')])

    def __unicode__(self):
        return self.nombre

    class Meta:
        ordering = ["cedula", "nombre"]
        verbose_name = "Persona"
        verbose_name_plural = "Personas"


class PersonaAtendida(Persona):
    diagnostico = models.ManyToManyField(Diagnostico)


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
