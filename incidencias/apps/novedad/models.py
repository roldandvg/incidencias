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


class PersonaFallecida(models.Model):
    # Modelo que pertenece a la novedad de la División de Búsqueda y Rescate, en el tipo de procedimiento
    # Levantamiento de Cadaver
    posicion = models.CharField(max_length=45)
    dias_desaparecido = models.SmallIntegerField()
    causa_muerte = models.CharField(max_length=255, blank=True, null=True)
    camisa = models.CharField(max_length=45)
    pantalon = models.CharField(max_length=45)
    zapatos = models.CharField(max_length=45)
    observacion = models.CharField(max_length=255)
    persona = models.ForeignKey(Persona)

    def __unicode__(self):
        return self.persona

    class Meta:
        ordering = ["dias_desaparecido"]
        verbose_name = "Persona Fallecida"
        verbose_name_plural = "Personas Fallecidas"


class Vehiculo(models.Model):
    placa = models.CharField(max_length=10)
    marca = models.CharField(max_length=45)
    color = models.CharField(max_length=20)
    anno = models.CharField(max_length=4)
    modelo = models.CharField(max_length=45)
    tipo = models.CharField(max_length=30)

    def __unicode__(self):
        return self.placa

    class Meta:
        ordering = ["marca", "modelo", "placa"]
        verbose_name = "Vehículo"
        verbose_name_plural = "Vehículos"


class VehiculoPersona(models.Model):
    tipo = models.CharField(max_length=1, choices=[('C', 'Conductor'), ('A', 'Acompañante')])
    observacion = models.CharField(max_length=255)
    vehiculo = models.ForeignKey(Vehiculo)
    persona = models.ForeignKey(Persona)

    def __unicode__(self):
        return self.tipo

    class Meta:
        ordering = ["tipo"]
        verbose_name = 'Vehículo - Persona'
        verbose_name_plural = 'Vehículos - Personas'


class Novedad(models.Model):
    fecha = models.DateField()
    hora_salida = models.TimeField()
    hora_llegada = models.TimeField()
    hora_reporte = models.TimeField()
    direccion = models.CharField(max_length=255)
    procedimiento = models.CharField(max_length=255)
    alarma_infundada = models.BooleanField(default=False)
    acto_presencia = models.BooleanField(default=False)
    parroquia = models.ForeignKey(Parroquia)
    tipo_procedimiento = models.ForeignKey(TipoProcedimiento)
    usuario = models.ForeignKey(User)  # input hidden en template con value default request.username

    def __unicode__(self):
        return self.motivo

    class Meta:
        ordering = ["fecha", "tipo_procedimiento"]
        verbose_name = "Novedad"
        verbose_name_plural = "Novedades"


class NovedadIncendioEstructura(models.Model):
    nombre = models.CharField(max_length=100)
    #observaciones = models.CharField(max_length=255)
    causa = models.CharField(max_length=255)
    fase = models.CharField(max_length=255, null=True)
    perdida_inmueble = models.CharField(max_length=255)
    p_inmueble_obs = models.CharField(max_length=255)
    perdida_mueble = models.CharField(max_length=255)
    p_mueble_obs = models.CharField(max_length=255)
    zona_afectada = models.CharField(max_length=255)
    propietario = models.ForeignKey(Persona)
    novedad = models.ForeignKey(Novedad)

    class Meta:
        verbose_name = "Novedad de Incendio de Estructura"
        verbose_name_plural = "Novedades de Incendio de Estructuras"
        

class NovedadIncendioVehiculo(models.Model):
    causa = models.CharField(max_length=255)
    fase = models.CharField(max_length=255)
    perdidas = models.CharField(max_length=255)
    a_nivel_de = models.CharField(max_length=255)
    vehiculo = models.ForeignKey(VehiculoPersona)
    novedad = models.ForeignKey(Novedad)


class NovedadIncendioVegetacion(models.Model):
    tipo_vegetacion = models.CharField(max_length=45)
    area_quemada = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad_efectivo = models.IntegerField()
    propietario = models.ForeignKey(Persona)
    novedad = models.ForeignKey(Novedad)


class NovedadIncendioEscapeGas(models.Model):
    cilindro_empresa = models.CharField(max_length=150)
    cilindro_kg = models.DecimalField(max_digits=10, decimal_places=2)
    cilindro_color = models.CharField(max_length=25)
    cilindro_ubicacion = models.CharField(max_length=255)
    propietario = models.ForeignKey(Persona)
    novedad = models.ForeignKey(Novedad)


class NovedadIncendioServicioAgua(models.Model):
    motivo = models.CharField(max_length=255)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2)
    material = models.CharField(max_length=255)
    beneficiarios = models.IntegerField()
    novedad = models.ForeignKey(Novedad)


class NovedadRescateVehiculo(models.Model):
    vehiculo = models.ForeignKey(VehiculoPersona)
    novedad = models.ForeignKey(Novedad)


class NovedadHospital(models.Model):
    pass


class NovedadEspecial(models.Model):
    pass


class NovedadPersona(models.Model):
    novedad = models.ForeignKey(Novedad)
    persona = models.ForeignKey(Persona)
    diagnostico = models.ForeignKey(Diagnostico)
    detalle_diagnostico = models.CharField(max_length=255, null=True)
    estado = models.CharField(max_length=1, choices=[('I', 'Ileso'), ('A', 'Arrollado'), ('L', 'Lesionado'),
                                                     ('D', 'Desaparecido'), ('E', 'Desalojado'), ('F', 'Fallecido')])
    traslado_hasta = models.CharField(max_length=255, null=True)

    def get_estado(self):
        if self.estado == "I":
            return "Ileso"
        elif self.estado == "A":
            return "Arrollado"
        elif self.estado == "L":
            return "Lesionado"
        elif self.estado == "D":
            return "Desaparecido"
        elif self.estado == "E":
            return "Desalojado"
        elif self.estado == "F":
            return "Fallecido"

    class Meta:
        ordering = ["estado"]


class NovedadUnidad(models.Model):
    novedad = models.ForeignKey(Novedad)
    unidad = models.ForeignKey(Unidad)
    a_cargo_de = models.CharField(max_length=150, null=True)

    def __unicode__(self):
        return self.a_cargo_de

    class Meta:
        ordering = ["-pk"]
        verbose_name = "Unidad por Novedad"
        verbose_name_plural = "Unidades por Novedades"


class NovedadComision(models.Model):
    novedad = models.ForeignKey(Novedad)
    comision = models.ForeignKey(Comision)
    a_cargo_de = models.CharField(max_length=150, null=True)

    def __unicode__(self):
        return self.a_cargo_de

    class Meta:
        ordering = ["-pk"]
        verbose_name = "Comisión por Novedad"
        verbose_name_plural = "Comisiones por Novedades"


"""
NOTA: AGREGAR EN ESTA SECCION LAS DISTINTAS NOVEDADES DE ACUERDO AL TIPO DE PROCEDIMIENTO SELECCIONADO
"""


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
