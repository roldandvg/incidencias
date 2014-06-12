# -*- coding: utf-8 -*-
from django.db import models


# Create your models here.
class Zona(models.Model):
    """!
    Clase de modelo correspondiente a la Zona

    @author Iraida Sanabria
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
    @date 06-05-14
    @version 1.0
    """

    ## Nombre de la zona
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
    """!
    Clase de modelo correspondiente al Municipio

    @author Iraida Sanabria
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
    @date 06-05-14
    @version 1.0
    """

    ## Nombre del Municipio
    nombre = models.CharField(max_length=45)

    ## Identificador de la zona
    zona = models.ForeignKey(Zona)

    def __unicode__(self):
        return self.nombre

    class Meta:
        ordering = ["zona", "nombre"]
        verbose_name = 'Municipio'
        verbose_name_plural = 'Municipios'


class Parroquia(models.Model):
    """!
    Clase de modelo correspondiente a la Parroquia

    @author Iraida Sanabria
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
    @date 06-05-14
    @version 1.0
    """

    ## Nombre de la Parroquia
    nombre = models.CharField(max_length=45)
    ## Identificador del municipio
    municipio = models.ForeignKey(Municipio)

    def __unicode__(self):
        return self.nombre

    class Meta:
        ordering = ["municipio", "nombre"]
        verbose_name = 'Parroquia'
        verbose_name_plural = 'Parroquias'


class TipoProcedimiento(models.Model):
    """!
    Clase de modelo correspondiente al Tipo de Procedimiento

    @author Iraida Sanabria
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
    @date 06-05-14
    @version 1.0
    """

    ## Nombre del tipo de procedimiento
    nombre = models.CharField(max_length=80)
    ## Tipo de división a la que pertenece el tipo de procedimiento
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
    """!
    Clase de modelo correspondiente al Detalle del tipo de procedimiento

    @author Iraida Sanabria
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
    @date 06-05-14
    @version 1.0
    """

    ## Nombre del detalle del tipo de procedimiento
    nombre = models.CharField(max_length=80)
    ## Identificdor del tipo de procedimiento
    tipo_procedimiento = models.ForeignKey(TipoProcedimiento)

    def __unicode__(self):
        return self.nombre

    class Meta:
        ordering = ["tipo_procedimiento", "nombre"]
        verbose_name = 'Detalle de Tipo de Procedimiento'
        verbose_name_plural = 'Detalles de Tipos de Procedimientos'


class Comision(models.Model):
    """!
    Clase de modelo correspondiente a la Comisión

    @author Iraida Sanabria
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
    @date 06-05-14
    @version 1.0
    """

    ## Nombre de la comisión
    nombre = models.CharField(max_length=45)
    ## Descripción de la comisión
    descripcion = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre

    class Meta:
        ordering = ["nombre"]
        verbose_name = 'Comisión'
        verbose_name_plural = 'Comisiones'


class Persona(models.Model):
    """!
    Clase de modelo correspondiente a la Persona

    @author Iraida Sanabria
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
    @date 06-05-14
    @version 1.0
    """

    ## Nombre de la persona
    nombre = models.CharField(max_length=80, null=True)
    ## Número de cédula
    cedula = models.CharField(max_length=10, unique=True, null=True)
    ## Edad de la persona
    edad = models.SmallIntegerField(null=True)
    ## Sexo de la persona, M: Masculino,  F: Femenino
    sexo = models.CharField(max_length=1, null=True, choices=[('M', 'Masculino'), ('F', 'Femenino')])

    def __unicode__(self):
        return self.nombre

    def get_sexo(self):
        if self.sexo == "M":
            return "Masculino"
        else:
            return "Femenino"

    class Meta:
        ordering = ["cedula", "nombre"]
        verbose_name = "Persona"
        verbose_name_plural = "Personas"