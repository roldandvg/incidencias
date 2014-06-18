# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

from incidencias.apps.comun.models import TipoProcedimiento, Comision, Persona, Parroquia
from incidencias.apps.institucion.models import Estacion, Unidad


# Create your models here.
class Diagnostico(models.Model):
    """!
    Clase de modelo correspondiente al Diagnóstico

    @author Iraida Sanabria
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
    @date 06-05-14
    @version 1.0
    """

    ## Nombre del diagnóstico
    nombre = models.CharField(max_length=45)
    ## Descripción del diagnóstico
    descripcion = models.CharField(max_length=255)

    def __unicode__(self):
        return self.nombre

    class Meta:
        ordering = ["nombre"]
        verbose_name = 'Diagnóstico'
        verbose_name_plural = 'Diagnósticos'


class PersonaFallecida(models.Model):
    """!
    Clase de modelo correspondiente a Persona fallecida en el tipo de procedimiento levantamiento de cadáver

    @author Iraida Sanabria
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
    @date 06-05-14
    @version 1.0
    """

    ## Posición en la que se econtró al occiso
    posicion = models.CharField(max_length=45)

    ## Número de días desaparecido
    dias_desaparecido = models.SmallIntegerField()

    ## Posible causa de muerte
    causa_muerte = models.CharField(max_length=255, blank=True, null=True)

    ## Descripción de la camisa que poseía el occiso
    camisa = models.CharField(max_length=45)

    ## Descripción del pantalón que poseía el occiso
    pantalon = models.CharField(max_length=45)

    ## Descripción de los zapatos que poseía el occiso
    zapatos = models.CharField(max_length=45)

    ## Otras observaciones del occiso
    observacion = models.CharField(max_length=255)

    ## Identificador de la persona
    persona = models.ForeignKey(Persona)

    def __unicode__(self):
        return self.persona

    class Meta:
        ordering = ["dias_desaparecido"]
        verbose_name = "Persona Fallecida"
        verbose_name_plural = "Personas Fallecidas"


class Vehiculo(models.Model):
    """!
    Clase de modelo correspondiente al Vehículo

    @author Iraida Sanabria
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
    @date 06-05-14
    @version 1.0
    """

    ## Número de la placa del vehículo
    placa = models.CharField(max_length=10)

    ##Marca del vehículo
    marca = models.CharField(max_length=45)

    ## Color del vehículo
    color = models.CharField(max_length=20)

    ## Año del vehículo
    anno = models.CharField(max_length=4)

    ## Modelo del vehículo
    modelo = models.CharField(max_length=45)

    ## Tipo de vehículo, moto, carro, camión
    tipo = models.CharField(max_length=30)

    def __unicode__(self):
        return self.placa

    class Meta:
        ordering = ["marca", "modelo", "placa"]
        verbose_name = "Vehículo"
        verbose_name_plural = "Vehículos"


class VehiculoPersona(models.Model):
    """!
    Clase de modelo correspondiente a la relación del Vehículo con la Persona

    @author Iraida Sanabria
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
    @date 06-05-14
    @version 1.0
    """

    ## Tipo de Persona en el vehículo, C: consuctor, A: acompañante
    tipo = models.CharField(max_length=1, choices=[('C', 'Conductor'), ('A', 'Acompañante')])

    ## Observaciones de la persona en el vehículo
    observacion = models.CharField(max_length=255)

    ## Identificador del vehículo
    vehiculo = models.ForeignKey(Vehiculo)

    ## Identificador de la persona
    persona = models.ForeignKey(Persona)

    def __unicode__(self):
        return self.tipo

    class Meta:
        ordering = ["tipo"]
        verbose_name = 'Vehículo - Persona'
        verbose_name_plural = 'Vehículos - Personas'


class Novedad(models.Model):
    """!
    Clase de modelo correspondiente a la Novedad

    @author Iraida Sanabria
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
    @date 06-05-14
    @version 1.0
    """

    ## Fecha e la que ocurrió la novedad
    fecha = models.DateField()

    ## Hora de salida de la unidad desde la estación al sitio donde ocurrió la novedad
    hora_salida = models.TimeField()

    ## Hora de llegada de la unidad al sitio donde ocurrió la novedad
    hora_llegada = models.TimeField()

    ## Hora en la que se hizo el reporte del procedimiento
    hora_reporte = models.TimeField()

    ## Dirección donde ocurrió la novedad
    direccion = models.CharField(max_length=255)

    ## Descripción de los métodos y técnicas utilizadas en la novedad
    procedimiento = models.CharField(max_length=255)

    ## Valor lógico que indica si la novedad es una alarma infundada
    alarma_infundada = models.BooleanField(default=False)

    ## Valor lógico que indica si la novedad es sólo un acto de presencia
    acto_presencia = models.BooleanField(default=False)

    ## Identificador de la parroquia
    parroquia = models.ForeignKey(Parroquia)

    ## Identificador del tipo de procedimiento
    tipo_procedimiento = models.ForeignKey(TipoProcedimiento)

    ## Identificador del usuario en sesión
    

    class Meta:
        ordering = ["fecha", "tipo_procedimiento"]
        verbose_name = "Novedad"
        verbose_name_plural = "Novedades"


class NovedadIncendioEstructura(models.Model):
    nombre = models.CharField(max_length=100)
    fase = models.CharField(max_length=255, null=True)
    perdida_inmueble = models.CharField(max_length=255)
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
    """!
    Clase de modelo correspondiente a la relación de la vivienda con la persona

    @author Iraida Sanabria
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
    @date 06-05-14
    @version 1.0
    """

    ## Valor lógico que indica si la persona es la propietaria de la vivienda
    propietario = models.BooleanField(default=False)

    ## Parentesco de la persona con el propietario de la vivienda
    parentesco = models.CharField(max_length=20)

    lesionados = models.SmallIntegerField(default=0)
    fallecidos = models.SmallIntegerField(default=0)

    ## Identificador de la vivienda
    vivienda = models.ForeignKey(Vivienda)

    ## Identificador de la persona
    persona = models.ForeignKey(Persona)

    def __unicode__(self):
        return self.propietario

    class Meta:
        ordering = ["propietario"]
        verbose_name = 'Vivienda - Persona'
        verbose_name_plural = 'Vivienda - Personas'
