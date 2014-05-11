# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class Zona(models.Model):
	nombre = models.CharField(max_length=150)

	def __unicode__(self):
		if self.nombre.__len__()>50:
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


class Unidad(models.Model):
	numero = models.CharField(max_length=10)
	modelo = models.CharField(max_length=45)

	def __unicode__(self):
		return self.numero+' '+self.modelo

	class Meta:
		ordering = ["numero","modelo"]
		verbose_name = 'Unidad'
		verbose_name_plural = 'Unidades'


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

	def __unicode__(self):
		return self.nombre

	class Meta:
		ordering = ["nombre"]
		verbose_name = 'Diagnóstico'
		verbose_name_plural = 'Diagnósticos'

