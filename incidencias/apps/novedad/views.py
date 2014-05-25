# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from incidencias.apps.novedad.models import Novedad, Diagnostico


# Vistas genericas para controlar el CRUD del modelo Diagnostico
class DiagnosticoList(ListView):
    model = Diagnostico
    paginate_by = 10


class DiagnosticoCreate(CreateView):
    model = Diagnostico
    success_url = reverse_lazy('diagnostico_list')


class DiagnosticoUpdate(UpdateView):
    model = Diagnostico
    success_url = reverse_lazy('diagnostico_list')


class DiagnosticoDelete(DeleteView):
    model = Diagnostico
    success_url = reverse_lazy('diagnostico_list')


# Vistas genericas para controlar el CRUD del modelo Novedad
class NovedadList(ListView):
    model = Novedad
    paginate_by = 10


class NovedadCreate(CreateView):
    model = Novedad
    success_url = reverse_lazy('novedad_list')


class NovedadUpdate(UpdateView):
    model = Novedad
    success_url = reverse_lazy('novedad_list')


class NovedadDelete(DeleteView):
    model = Novedad
    success_url = reverse_lazy('novedad_list')


# Vistas genericas para el CRUD de novedades de acuerdo a la división que va a registrar
"""class NovedadIncendioList(ListView):
    model = NovedadIncendio
    paginate_by =  10"""