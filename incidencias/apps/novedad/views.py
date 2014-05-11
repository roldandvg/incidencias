# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from incidencias.apps.novedad.models import Novedad

# Vistas genericas para controlar el CRUD del modelo Novedad
class NovedadList(ListView):
	model = Novedad
	
class NovedadCreate(CreateView):
	model = Novedad
	success_url = reverse_lazy('novedad_list')

class NovedadUpdate(UpdateView):
	model = Novedad
	success_url = reverse_lazy('novedad_list')
	
class NovedadDelete(DeleteView):
	model = Novedad
	success_url = reverse_lazy('novedad_list')
