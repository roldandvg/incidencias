# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from incidencias.apps.institucion.models import Cargo, Rango, Estacion, Trabajador, Unidad


# Vistas genericas para controlar el CRUD del modelo Cargo
class CargoList(ListView):
    model = Cargo
    paginate_by = 10


class CargoCreate(CreateView):
    model = Cargo
    success_url = reverse_lazy('cargo_list')


class CargoUpdate(UpdateView):
    model = Cargo
    success_url = reverse_lazy('cargo_list')


class CargoDelete(DeleteView):
    model = Cargo
    success_url = reverse_lazy('cargo_list')


# Vistas genericas para controlar el CRUD del modelo Rango
class RangoList(ListView):
    model = Rango
    paginate_by = 10


class RangoCreate(CreateView):
    model = Rango
    success_url = reverse_lazy('rango_list')


class RangoUpdate(UpdateView):
    model = Rango
    success_url = reverse_lazy('rango_list')


class RangoDelete(DeleteView):
    model = Rango
    success_url = reverse_lazy('rango_list')


# Vistas genericas para controlar el CRUD del modelo Estación
class EstacionList(ListView):
    model = Estacion
    paginate_by = 10


class EstacionCreate(CreateView):
    model = Estacion
    success_url = reverse_lazy('estacion_list')


class EstacionUpdate(UpdateView):
    model = Estacion
    success_url = reverse_lazy('estacion_list')


class EstacionDelete(DeleteView):
    model = Estacion
    success_url = reverse_lazy('estacion_list')


# Vistas genericas para controlar el CRUD del modelo Trabajador
class TrabajadorList(ListView):
    model = Trabajador
    paginate_by = 10


class TrabajadorCreate(CreateView):
    model = Trabajador
    fields = ["nombre", "cedula", "edad", "sexo", "estacion", "cargo", "rango"]
    initial = {"rango": 1}
    success_url = reverse_lazy('trabajador_list')


class TrabajadorUpdate(UpdateView):
    model = Trabajador
    fields = ["nombre", "cedula", "edad", "sexo", "estacion", "cargo", "rango"]
    success_url = reverse_lazy('trabajador_list')


class TrabajadorDelete(DeleteView):
    model = Trabajador
    success_url = reverse_lazy('trabajador_list')


# Vistas genericas para controlar el CRUD del modelo Unidad
class UnidadList(ListView):
    model = Unidad
    paginate_by = 10


class UnidadCreate(CreateView):
    model = Unidad
    success_url = reverse_lazy('unidad_list')


class UnidadUpdate(UpdateView):
    model = Unidad
    success_url = reverse_lazy('unidad_list')


class UnidadDelete(DeleteView):
    model = Unidad
    success_url = reverse_lazy('unidad_list')