# -*- coding:utf-8 -*-
from django import forms
from incidencias.apps.comun.models import Municipio, Parroquia, TipoProcedimiento, Comision
from incidencias.apps.institucion.models import Unidad
from incidencias.apps.novedad.models import Diagnostico


def cargar_municipio():
    lista = ('0', 'Seleccione...'),
    try:
        for mun in Municipio.objects.all():
            lista += (mun.pk, mun.nombre),
    except Municipio.DoesNotExists, e:
        pass

    return lista


def cargar_parroquia():
    lista = ('0', 'Seleccione...'),
    try:
        for par in Parroquia.objects.all():
            lista += (par.pk, par.nombre),
    except Parroquia.DoesNotExists, e:
        pass

    return lista


def cargar_tipo_procedimiento(division=None):
    lista = ('0', 'Seleccione...'),
    try:
        if division:
            tipo_procedimiento = TipoProcedimiento.objects.filter(division=division)
        else:
            tipo_procedimiento = TipoProcedimiento.objects.all()

        for tp in tipo_procedimiento:
            lista += (tp.pk, tp.nombre),
    except TipoProcedimiento.DoesNotExists, e:
        pass

    return lista


def cargar_unidad():
    lista = ('0', 'Seleccione...'),
    try:
        for und in Unidad.objects.all():
            lista += (und.pk, und.numero),
    except Unidad.DoesNotExists, e:
        pass

    return lista


def cargar_comision():
    lista = ('0', 'Seleccione...'),
    try:
        for com in Comision.objects.all():
            lista += (com.pk, com.nombre),
    except Comision.DoesNotExists, e:
        pass

    return lista


def cargar_diagnostico():
    lista = ('0', 'Seleccione...'),
    try:
        for dia in Diagnostico.objects.all():
            lista += (dia.pk, dia.nombre),
    except Diagnostico.DoesNotExists, e:
        pass

    return lista


class FormPersona(forms.Form):
    nombre = forms.CharField(label="Nombre",
                             widget=forms.TextInput(attrs={'title': 'Indique el nombre de la persona',
                                                           'placeholder': 'Indique el nombre',
                                                           'class': 'tooltip-top', 'size': '40'}))
    cedula = forms.CharField(label="Cédula",
                             widget=forms.TextInput(attrs={'title': 'Indique el número de cédula de la persona',
                                                           'placeholder': 'V-00000000',
                                                           'class': 'tooltip-top', 'size': '10'}))
    edad = forms.IntegerField(label="Edad",
                              widget=forms.TextInput(attrs={'title': 'Indique la edad de la persona',
                                                            'placeholder': '00', 'class': 'tooltip-top', 'size': '3'}))
    sexo = forms.ChoiceField(label="Sexo", choices=[('M', 'Masculino'), ('F', 'Femenino')],
                             widget=forms.Select(attrs={'title': 'Seleccione el sexo de la persona',
                                                        'class': 'tooltip-top'}))

    def __init__(self, *args, **kwargs):
        super(FormPersona, self).__init__(*args, **kwargs)


class FormCondicionPersona(FormPersona):
    diagnostico = forms.ChoiceField(label="Diagnóstico", choices=cargar_diagnostico(),
                                    widget=forms.Select(attrs={'title': 'Seleccione el diagnóstico de la persona',
                                                               'class': 'tooltip-top'}))
    detalle_diagnostico = forms.CharField(label="Detalles diagnóstico",
                                          widget=forms.Textarea(attrs={'title': 'Indique el detalle del diagnóstico '
                                                                                'dado a la persona',
                                                                       'placeholder': 'Indique detalles del '
                                                                                      'diagnóstico',
                                                                       'class': 'tooltip-top', 'cols': '60'}))
    estado = forms.ChoiceField(label="Estado", choices=[('0', 'Seleccione...'), ('I', 'Ileso'), ('A', 'Arrollado'),
                                                        ('L', 'Lesionado'), ('D', 'Desaparecido'), ('E', 'Desalojado'),
                                                        ('F', 'Fallecido')],
                               widget=forms.Select(attrs={'title': 'Seleccione el estado de la persona',
                                                          'class': 'tooltip-top'}))

    def __init__(self, *args, **kwargs):
        super(FormCondicionPersona, self).__init__(*args, **kwargs)


# Este formulario debe hacerser en el template con tabs debido a lo extenso del mismo
class FormNovedad(forms.Form):
    fecha = forms.DateField(label="Fecha",
                            widget=forms.TextInput(attrs={'title': 'Indique la fecha del reporte',
                                                          'placeholder': 'DD/MM/YYYY',
                                                          'class': 'tooltip-top', 'size': '10'}))
    hora_salida = forms.TimeField(label="Hora de Salida",
                                  widget=forms.TextInput(attrs={'title': 'Indique la hora de salida de la estación',
                                                                'placeholder': '00:00', 'class': 'tooltip-top',
                                                                'size': '6'}))
    hora_llegada = forms.TimeField(label="Hora de Llegada",
                                   widget=forms.TextInput(attrs={'title': 'Indique la hora de llegada a la novedad',
                                                                 'placeholder': '00:00', 'class': 'tooltip-top',
                                                                 'size': '6'}))
    hora_reporte = forms.TimeField(label="Hora de Reporte",
                                   widget=forms.TextInput(attrs={'title': 'Indique la hora en la que se elaboró el '
                                                                          'reporte de la novedad',
                                                                 'placeholder': '00:00', 'class': 'tooltip-top',
                                                                 'size': '6'}))
    direccion = forms.CharField(label="Dirección",
                                widget=forms.Textarea(attrs={'title': 'Indique la dirección exacta en donde se generó '
                                                                      'la novedad',
                                                             'placeholder': 'dirección de la novedad',
                                                             'class': 'tooltip-top', 'cols': '60'}))
    procedimiento = forms.CharField(label="Procedimiento",
                                    widget=forms.Textarea(attrs={'title': 'Indique el procedimiento realizado al '
                                                                          'atender la novedad',
                                                                 'placeholder': 'Indique el procedimiento',
                                                                 'class': 'tooltip-top', 'cols': '60'}))
    alarma_infundada = forms.BooleanField()
    acto_presencia = forms.BooleanField()
    municipio = forms.ChoiceField(label="Municipio", choices=cargar_municipio(),
                                  widget=forms.Select(attrs={'title': 'Seleccione el Municipio en donde se generó la '
                                                                      'novedad',
                                                             'class': 'tooltip-top'}))
    parroquia = forms.ChoiceField(label="Parroquia", choices=cargar_parroquia(),
                                  widget=forms.Select(attrs={'title': 'Seleccione la Parroquia en donde se generó la '
                                                                      'novedad',
                                                             'class': 'tooltip-top'}))
    tipo_procedimiento = forms.ChoiceField(label="Tipo de Procedimiento", choices=cargar_tipo_procedimiento(),
                                           widget=forms.Select(attrs={'title': 'Seleccione el tipo de procedimiento',
                                                                      'class': 'tooltip-top'}))

    def __init__(self, division=None, *args, **kwargs):
        super(FormNovedad, self).__init__(*args, **kwargs)
        self.fields['tipo_procedimiento'].choices = cargar_tipo_procedimiento(division)


class FormUnidad(forms.Form):
    numero = forms.ChoiceField(label="Número de Unidad", choices=cargar_unidad(),
                               widget=forms.Select(attrs={'title': 'Seleccione el número de la Unidad',
                                                          'class': 'tooltip-top'}))

    def __init__(self, *args, **kwargs):
        super(FormUnidad, self).__init__(*args, **kwargs)


class FormComision(forms.Form):
    nombre = forms.ChoiceField(label="Nombre de la comisión", choices=cargar_comision(),
                               widget=forms.Select(attrs={'title': 'Seleccione la comisión',
                                                          'class': 'tooltip-top'}))

    def __init__(self, *args, **kwargs):
        super(FormComision, self).__init__(*args, **kwargs)


class FormIncendioEstructura(FormPersona):
    nombre_inmueble = forms.CharField(label='Nombre del Inmueble',
                                      widget=forms.TextInput(attrs={'title': 'Indique el nombre del inmueble objeto '
                                                                             'del incendio que causo la novedad',
                                                                    'class': 'tooltip-top', 'size': '40',
                                                                    'placeholder': 'Indique el nombre del inmueble'}))
    causa = forms.CharField(label="Causa",
                            widget=forms.Textarea(attrs={'title': 'Indique la causa por la cual se genero el incendio '
                                                                  'del inmueble',
                                                         'placeholder': 'Indique la causa del incendio',
                                                         'class': 'tooltip-top', 'cols': '40'}))
    fase = forms.CharField(label="Fase",
                           widget=forms.TextInput(attrs={'title': 'Indique la fase de avance del incendio',
                                                         'placeholder': 'Indique fase de avance',
                                                         'class': 'tooltip-top', 'size': '40'}))
    perdida_inmueble = forms.CharField(label="Perdida del Inmueble",
                                       widget=forms.Textarea(attrs={'title': 'Indique las perdidas generadas por el '
                                                                             'incendio sobre el inmueble',
                                                                    'placeholder': 'Indique perdidas del inmueble',
                                                                    'class': 'tooltip-top', 'cols': '40'}))
    p_inmueble_obs = forms.CharField(label="A nivel de",
                                     widget=forms.Textarea(attrs={'title': 'Indique algunas observaciones sobre las '
                                                                           'perdidas del inmueble',
                                                                  'placeholder': 'Indique observaciones a nivel de la '
                                                                                 'perdida del inmueble',
                                                                  'class': 'tooltip-top', 'cols': '40'}))
    perdida_mueble = forms.CharField(label="Perdida del mueble",
                                     widget=forms.Textarea(attrs={'title': 'Indique las perdidas generadas por el '
                                                                           'incendio sobre los bienes muebles',
                                                                  'placeholder': 'Indique las perdidas del mueble',
                                                                  'class': 'tooltip-top', 'size': '40'}))
    p_mueble_obs = forms.CharField(label="A nivel de",
                                   widget=forms.Textarea(attrs={'title': 'Indique algunas observaciones sobre las '
                                                                         'perdidas de los bienes muebles',
                                                                'placeholder': 'Indique observaciones a nivel de la '
                                                                               'perdida de bienes muebles',
                                                                'class': 'tooltip-top', 'cols': '40'}))
    zona_afectada = forms.CharField(label="Zona Afectada",
                                    widget=forms.Textarea(attrs={'title': 'Indique las zonas afectadas por el incendio',
                                                                 'placeholder': 'Indique zonas afectadas',
                                                                 'class': 'tooltip-top', 'cols': '40'}))

    def __init__(self, *args, **kwargs):
        super(FormIncendioEstructura, self).__init__(*args, **kwargs)


class FormIncendioVehiculo(FormCondicionPersona):
    # DAtos del vehiculo
    placa = forms.CharField(label="Placa",
                            widget=forms.TextInput(attrs={'title': 'Indique la placa del vehículo',
                                                          'placeholder': 'XXXXXXXX', 'size': '12',
                                                          'class': 'tooltip-top'}))
    marca = forms.CharField(label="Marca",
                            widget=forms.TextInput(attrs={'title': 'Indique la marca del vehículo',
                                                          'placeholder': 'Indique marca', 'size': '25',
                                                          'class': 'tooltip-top'}))
    color = forms.CharField(label="Color",
                            widget=forms.TextInput(attrs={'title': 'Indique el color del vehículo',
                                                          'placeholder': 'Indique color', 'size': '25',
                                                          'class': 'tooltip-top'}))
    anno = forms.CharField(label="Año",
                           widget=forms.TextInput(attrs={'title': 'Indique el año del vehículo',
                                                         'placeholder': 'YYYY', 'size': '4', 'class': 'tooltip-top'}))
    modelo = forms.CharField(label="Modelo",
                             widget=forms.TextInput(attrs={'title': 'Indique el modelo del vehículo',
                                                           'placeholder': 'Indique modelo', 'size': '25',
                                                           'class': 'tooltip-top'}))
    tipo = forms.CharField(label="Tipo",
                           widget=forms.TextInput(attrs={'title': 'Indique el tipo de vehículo',
                                                         'placeholder': 'Indique tipo', 'size': '25',
                                                         'class': 'tooltip-top'}))
    # Datos de la novedad
    causa = forms.CharField(label="Causa",
                            widget=forms.Textarea(attrs={'title': 'Indique la causa del incendio en el vehículo',
                                                         'placeholder': 'Indique causa de incendio',
                                                         'class': 'tooltip-top', 'cols': '26'}))
    fase = forms.CharField(label="Fase",
                           widget=forms.TextInput(attrs={'title': 'Indique la fase de incendio en el vehículo',
                                                         'placeholder': 'Indique fase', 'size': '25',
                                                         'class': 'tooltip-top'}))
    perdidas = forms.CharField(label="Perdidas",
                               widget=forms.Textarea(attrs={'title': 'Indique las perdidas del vehículo',
                                                            'placeholder': 'Indique perdida del vehículo',
                                                            'class': 'tooltip-top', 'cols': '26'}))
    a_nivel_de = forms.CharField(label="A nivel de",
                                 widget=forms.Textarea(attrs={'title': 'Indique algunas observaciones sobre las '
                                                                       'perdidas del vehículo a nivel de...',
                                                              'placeholder': 'Indique perdidas a nivel de...',
                                                              'class': 'tooltip-top', 'cols': '26'}))
    persona_vehiculo = forms.ChoiceField(label="Persona en vehículo",
                                         choices=[('C', 'Conductor'), ('A', 'Acompañante')],
                                         widget=forms.Select(attrs={'title': 'Seleccione el tipo de persona del '
                                                                             'vehículo',
                                                                    'class': 'tooltip-top'}))
    observacion = forms.CharField(label="Observac.",
                                  widget=forms.Textarea(attrs={'title': 'Indique las observaciones sobre el incendio '
                                                                        'en el vehículo',
                                                               'placeholder': 'Indique causa de incendio',
                                                               'class': 'tooltip-top', 'cols': '26'}))
