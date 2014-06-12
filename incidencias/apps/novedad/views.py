# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect
from django.views.generic import ListView, CreateView
from django.views.generic.edit import UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.contrib.auth.models import User

#from incidencias.apps.comun.models import Persona
from incidencias.apps.novedad.models import Novedad, Diagnostico, NovedadIncendioEstructura
#from incidencias.apps.novedad.forms import FormPersona, FormNovedad, FormIncendioEstructura, FormUnidad, FormComision, \
#    FormCondicionPersona, FormIncendioVehiculo
from incidencias.apps.comun.forms import PersonaForm
from incidencias.apps.novedad.forms import NovedadForm, UnidadFormSet, ComisionFormSet, IncendioEstructuraFormSet


# Vistas genericas para controlar el CRUD del modelo Diagnostico
class DiagnosticoList(ListView):
    model = Diagnostico
    paginate_by = 10

    def get_queryset(self):
        if len(self.args) > 0:
            return Diagnostico.objects.filter(nombre__icontains=self.args[0])
        else:
            return Diagnostico.objects.all()


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
#descomentar
class NovedadIncendioCreateView(CreateView):
    #template_name = 'novedad/novedad_combate_incendio.html'
    model = Novedad
    form_class = NovedadForm
    success_url = 'novedad/'

    def get_form_kwargs(self):
        # Método que permite establecer el tipo de procedimiento a ser registrado en el formulario de novedades
        kwargs = super(NovedadIncendioCreateView, self).get_form_kwargs()
        kwargs.update({'division': 'CI'})
        return kwargs

    def get(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        unidad_form = UnidadFormSet()
        comision_form = ComisionFormSet()
        incendio_estructura_form = IncendioEstructuraFormSet()
        return self.render_to_response(self.get_context_data(form=form, unidad_form=unidad_form,
                                                             comision_form=comision_form,
                                                             incendio_estructura_form=incendio_estructura_form))

    def post(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        unidad_form = UnidadFormSet(self.request.POST)
        comision_form = ComisionFormSet(self.request.POST)
        incendio_estructura_form = IncendioEstructuraFormSet(self.request.POST)

        if form.is_valid() and unidad_form.is_valid() and comision_form.is_valid() \
                and incendio_estructura_form.is_valid():
            return self.form_valid(form, unidad_form, comision_form, incendio_estructura_form)
        else:
            return self.form_invalid(form, unidad_form, comision_form, incendio_estructura_form)

    def form_valid(self, form, unidad_form, comision_form, incendio_estructura_form):
        self.object = form.save()
        unidad_form.instance = self.object
        unidad_form.save()
        comision_form.instance = self.object
        comision_form.save()
        incendio_estructura_form.instance = self.object
        incendio_estructura_form.save()
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, unidad_form, comision_form, incendio_estructura_form):
        return render_to_response(self.get_context_data(form=form, unidad_form=unidad_form,
                                                        comision_form=comision_form,
                                                        incendio_estructura_form=incendio_estructura_form))
"""                                                        


def novedad_incendio(request):
    c = RequestContext(request)
    c.update(csrf(request))

    if request.POST:
        form = NovedadForm(data=request.POST, division="CI")
        print form
        if not form.is_valid():
            return render_to_response('novedad/novedad_combate_incendio.html',
                                      {'form': form,
                                       'unidad_form': UnidadFormSet(request.POST, prefix="unidad_formset"),
                                       'comision_form': ComisionFormSet(request.POST, prefix="comision_formset"),
                                       'incendio_estructura_form': IncendioEstructuraFormSet(request.POST, prefix="estructura_formset")},
                                      c)

        novedad = form.save(commit=False)
        incendio_estructura_form = IncendioEstructuraFormSet(data=request.POST, prefix="estructura_formset",
                                                             instance=novedad)
        unidad_form = UnidadFormSet(data=request.POST, prefix="unidad_formset", instance=novedad)
        comision_form = ComisionFormSet(data=request.POST, prefix="comision_formset", instance=novedad)

        if not incendio_estructura_form.is_valid() or not unidad_form.is_valid() or not comision_form.is_valid():
            return render_to_response('novedad/novedad_combate_incendio.html',
                                      {'form': form, 'unidad_form': unidad_form, 'comision_form': comision_form}, c)

    return render_to_response('novedad/novedad_combate_incendio.html',
                              {'form': NovedadForm(division='CI'),
                               'unidad_form': UnidadFormSet(prefix="unidad_formset"), 
                               'comision_form': ComisionFormSet(prefix="comision_formset"),
                               'incendio_estructura_form': IncendioEstructuraFormSet(prefix="estructura_formset")},
                               c)

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
"""
