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
        ordering = ["zona", "nombre"]
        verbose_name = 'Municipio'
        verbose_name_plural = 'Municipios'


class Parroquia(models.Model):
    nombre = models.CharField(max_length=45)
    municipio = models.ForeignKey(Municipio)

    def __unicode__(self):
        return self.nombre

    class Meta:
        ordering = ["municipio", "nombre"]
        verbose_name = 'Parroquia'
        verbose_name_plural = 'Parroquias'


class TipoProcedimiento(models.Model):
    nombre = models.CharField(max_length=80)
    division = models.CharField(max_length=2, choices=[('CI', 'Combate de Incendios'), ('BR', 'Búsqueda y Rescate'),
                                                       ('EP', 'Emergencia Pre-hospitalaria'),
                                                       ('AE', 'Actividades Especiales')])

    def __unicode__(self):
        return self.nombre

    def get_division(self):
        if self.division == "CI":
            return "Combate de Incendios"
        elif self.division == "BR":
            return "Búsqueda y Rescate"
        elif self.division == "EP":
            return "Emergencia Pre-hospitalaria"
        elif self.division == "AE":
            return "Actividades Especiales"
        else:
            return self.division

    class Meta:
        ordering = ["division", "nombre"]
        verbose_name = 'Tipo de Procedimiento'
        verbose_name_plural = 'Tipos de Procedimientos'


class DetalleTipoProcedimiento(models.Model):
    nombre = models.CharField(max_length=80)
    tipo_procedimiento = models.ForeignKey(TipoProcedimiento)

    def __unicode__(self):
        return self.nombre

    class Meta:
        ordering = ["tipo_procedimiento", "nombre"]
        verbose_name = 'Detalle de Tipo de Procedimiento'
        verbose_name_plural = 'Detalles de Tipos de Procedimientos'


class Comision(models.Model):
    nombre = models.CharField(max_length=45)
    descripcion = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre

    class Meta:
        ordering = ["nombre"]
        verbose_name = 'Comisión'
        verbose_name_plural = 'Comisiones'


class Persona(models.Model):
    nombre = models.CharField(max_length=80, null=True)
    cedula = models.CharField(max_length=10, unique=True, null=True)
    edad = models.SmallIntegerField(null=True)
    sexo = models.CharField(max_length=1, null=True, choices=[('M', 'Masculino'), ('F', 'Femenino')])

    def __unicode__(self):
        return self.nombre

    class Meta:
        ordering = ["cedula", "nombre"]
        verbose_name = "Persona"
        verbose_name_plural = "Personas"