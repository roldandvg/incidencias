# -*- coding: utf-8 -*-
#from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from incidencias.apps.comun.models import Zona, Municipio, Parroquia, Estacion, Procedimiento, TipoProcedimiento, \
    DetalleTipoProcedimiento, Unidad, Comision, Diagnostico


# Vistas genericas para controlar el CRUD del modelo Zona
class ZonaList(ListView):
    model = Zona


class ZonaCreate(CreateView):
    model = Zona
    success_url = reverse_lazy('zona_list')


class ZonaUpdate(UpdateView):
    model = Zona
    success_url = reverse_lazy('zona_list')


class ZonaDelete(DeleteView):
    model = Zona
    success_url = reverse_lazy('zona_list')


# Vistas genericas para controlar el CRUD del modelo Municipio
class MunicipioList(ListView):
    model = Municipio


class MunicipioCreate(CreateView):
    model = Municipio
    success_url = reverse_lazy('municipio_list')


class MunicipioUpdate(UpdateView):
    model = Municipio
    success_url = reverse_lazy('municipio_list')


class MunicipioDelete(DeleteView):
    model = Municipio
    success_url = reverse_lazy('municipio_list')


# Vistas genericas para controlar el CRUD del modelo Parroquia
class ParroquiaList(ListView):
    model = Parroquia


class ParroquiaCreate(CreateView):
    model = Parroquia
    success_url = reverse_lazy('parroquia_list')


class ParroquiaUpdate(UpdateView):
    model = Parroquia
    success_url = reverse_lazy('parroquia_list')


class ParroquiaDelete(DeleteView):
    model = Parroquia
    success_url = reverse_lazy('parroquia_list')


# Vistas genericas para controlar el CRUD del modelo Estación
class EstacionList(ListView):
    model = Estacion


class EstacionCreate(CreateView):
    model = Estacion
    success_url = reverse_lazy('estacion_list')


class EstacionUpdate(UpdateView):
    model = Estacion
    success_url = reverse_lazy('estacion_list')


class EstacionDelete(DeleteView):
    model = Estacion
    success_url = reverse_lazy('estacion_list')


# Vistas genericas para controlar el CRUD del modelo Procedimiento
class ProcedimientoList(ListView):
    model = Procedimiento


class ProcedimientoCreate(CreateView):
    model = Procedimiento
    success_url = reverse_lazy('procedimiento_list')


class ProcedimientoUpdate(UpdateView):
    model = Procedimiento
    success_url = reverse_lazy('procedimiento_list')


class ProcedimientoDelete(DeleteView):
    model = Procedimiento
    success_url = reverse_lazy('procedimiento_list')


# Vistas genericas para controlar el CRUD del modelo TipoProcedimiento
class TipoProcedimientoList(ListView):
    model = TipoProcedimiento


class TipoProcedimientoCreate(CreateView):
    model = TipoProcedimiento
    success_url = reverse_lazy('tipoprocedimiento_list')


class TipoProcedimientoUpdate(UpdateView):
    model = TipoProcedimiento
    success_url = reverse_lazy('tipoprocedimiento_list')


class TipoProcedimientoDelete(DeleteView):
    model = TipoProcedimiento
    success_url = reverse_lazy('tipoprocedimiento_list')


# Vistas genericas para controlar el CRUD del modelo DetalleTipoProcedimiento
class DetalleTipoProcedimientoList(ListView):
    model = DetalleTipoProcedimiento


class DetalleTipoProcedimientoCreate(CreateView):
    model = DetalleTipoProcedimiento
    success_url = reverse_lazy('detalletipoprocedimiento_list')


class DetalleTipoProcedimientoUpdate(UpdateView):
    model = DetalleTipoProcedimiento
    success_url = reverse_lazy('detalletipoprocedimiento_list')


class DetalleTipoProcedimientoDelete(DeleteView):
    model = DetalleTipoProcedimiento
    success_url = reverse_lazy('detalletipoprocedimiento_list')


# Vistas genericas para controlar el CRUD del modelo Unidad
class UnidadList(ListView):
    model = Unidad


class UnidadCreate(CreateView):
    model = Unidad
    success_url = reverse_lazy('unidad_list')


class UnidadUpdate(UpdateView):
    model = Unidad
    success_url = reverse_lazy('unidad_list')


class UnidadDelete(DeleteView):
    model = Unidad
    success_url = reverse_lazy('unidad_list')


# Vistas genericas para controlar el CRUD del modelo Comision
class ComisionList(ListView):
    model = Comision


class ComisionCreate(CreateView):
    model = Comision
    success_url = reverse_lazy('comision_list')


class ComisionUpdate(UpdateView):
    model = Comision
    success_url = reverse_lazy('comision_list')


class ComisionDelete(DeleteView):
    model = Comision
    success_url = reverse_lazy('comision_list')


# Vistas genericas para controlar el CRUD del modelo Diagnostico
class DiagnosticoList(ListView):
    model = Diagnostico


class DiagnosticoCreate(CreateView):
    model = Diagnostico
    success_url = reverse_lazy('diagnostico_list')


class DiagnosticoUpdate(UpdateView):
    model = Diagnostico
    success_url = reverse_lazy('diagnostico_list')


class DiagnosticoDelete(DeleteView):
    model = Diagnostico
    success_url = reverse_lazy('diagnostico_list')
