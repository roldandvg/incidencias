# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class Novedad(models.Model):
	fecha = models.DateField()
	lugar = models.CharField(max_length=255)
	motivo = models.CharField(max_length=45)
	hora_salida = models.TimeField()
	hora_llegada = models.TimeField()
	hora_reporte = models.TimeField()
	
	def __unicode__(self):
		return self.motivo
		
	class Meta:
		ordering = ["fecha"]
		verbose_name = 'Novedad'
		verbose_name_plural = 'Novedades'
