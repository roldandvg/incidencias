# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from incidencias.apps.institucion.models import Cargo, Rango, Trabajador


# Vistas genericas para controlar el CRUD del modelo Cargo
class CargoList(ListView):
    model = Cargo


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


class RangoCreate(CreateView):
    model = Rango
    success_url = reverse_lazy('rango_list')


class RangoUpdate(UpdateView):
    model = Rango
    success_url = reverse_lazy('rango_list')


class RangoDelete(DeleteView):
    model = Rango
    success_url = reverse_lazy('rango_list')


# Vistas genericas para controlar el CRUD del modelo Trabajador
class TrabajadorList(ListView):
    model = Trabajador


class TrabajadorCreate(CreateView):
    model = Trabajador
    success_url = reverse_lazy('trabajador_list')


class TrabajadorUpdate(UpdateView):
    model = Trabajador
    success_url = reverse_lazy('trabajador_list')


class TrabajadorDelete(DeleteView):
    model = Trabajador
    success_url = reverse_lazy('trabajador_list')