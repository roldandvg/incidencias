from django.db import models
from django.contrib.auth.models import User
from incidencias.apps.comun.models import Persona, Estacion

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
		
class Trabajador(models.Model):
	persona = models.ForeignKey(Persona)
	cargo = models.ForeignKey(Cargo)
	rango = models.ForeignKey(Rango)
	estacion = models.ForeignKey(Estacion)
	usuario = models.ForeignKey(User, null=True)

	def __unicode__(self):
		return self.persona
		
	class Meta:
		ordering = ["estacion", "cargo", "persona"]
		verbose_name = "Trabajador"
		verbose_name_plural = "Trabajadores"
