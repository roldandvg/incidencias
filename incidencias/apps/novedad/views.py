# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, render_to_response
from django.template import RequestContext

# Vistas genericas para formset
from extra_views import FormSetView, ModelFormSetView, InlineFormSetView, InlineFormSet, CreateWithInlinesView, \
    UpdateWithInlinesView, CalendarMonthView, NamedFormsetsMixin, SortableListMixin, SearchableListMixin
from extra_views.generic import GenericInlineFormSet, GenericInlineFormSetView

from incidencias.apps.comun.models import Persona
from incidencias.apps.novedad.models import Novedad, Diagnostico, NovedadIncendioEstructura
from incidencias.apps.novedad.forms import FormPersona, FormNovedad, FormIncendioEstructura, FormUnidad, FormComision, \
    FormCondicionPersona, FormIncendioVehiculo


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

"""
class NovedadCreate(CreateView):
    model = Novedad
    success_url = reverse_lazy('novedad_list')


class NovedadUpdate(UpdateView):
    model = Novedad
    success_url = reverse_lazy('novedad_list')


class NovedadDelete(DeleteView):
    model = Novedad
    success_url = reverse_lazy('novedad_list')
"""

# Vistas genericas para el CRUD de novedades de acuerdo a la división que va a registrar
"""class NovedadIncendioList(ListView):
    model = NovedadIncendio
    paginate_by =  10
class IncendioEstructuraInline(InlineFormSet):
    model = NovedadIncendioEstructura


class PersonaInline(InlineFormSet):
    model = Persona


class NovedadIncendioEstructura(CreateWithInlinesView):
    model = Novedad
    inlines = [IncendioEstructuraInline, PersonaInline]
    template_name = "novedad/incendio_estructura.html"
"""
@login_required()
def novedad_incendio(request):
    form_novedad = FormNovedad(auto_id="%s", division="CI")
    form_unidad = FormUnidad(auto_id="%s")
    form_comision = FormComision(auto_id="%s")
    form_persona = FormCondicionPersona(auto_id="%s")
    form_estructura = FormIncendioEstructura(auto_id="%s")
    form_vehiculo = FormIncendioVehiculo(auto_id="%s")
    if request.method == "POST":
        form_novedad = FormNovedad(request.POST, auto_id="%s")
        form_unidad = FormUnidad(request.POST, auto_id="%s")
        form_comision = FormComision(request.POST, auto_id="%s")
        form_persona = FormCondicionPersona(request.POST, auto_id="%s")
        form_estructura = FormIncendioEstructura(request.POST, auto_id="%s")
        form_vehiculo = FormIncendioVehiculo(request.POST, auto_id="%s")

    c = {'formNovedad': form_novedad, 'formUnidad': form_unidad, 'formComision': form_comision,
         'formPersona': form_persona, 'formEstructura': form_estructura, 'formVehiculo': form_vehiculo,
         'user': request.user}
    c.update(csrf(request))

    return render_to_response('novedad/novedad_combate_incendio.html', c, context_instance=RequestContext(request))