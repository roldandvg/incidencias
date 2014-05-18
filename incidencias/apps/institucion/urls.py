from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from incidencias.apps.institucion import views

urlpatterns = patterns('',
                       url(r'^cargo/$', login_required(views.CargoList.as_view()), name="cargo_list"),
                       url(r'^cargo/new/$', login_required(views.CargoCreate.as_view()), name='cargo_new'),
                       url(r'^cargo/edit/(?P<pk>\d+)$', login_required(views.CargoUpdate.as_view()), name='cargo_edit'),
                       url(r'^cargo/delete/(?P<pk>\d+)$', login_required(views.CargoDelete.as_view()), name='cargo_delete'),

                       url(r'^rango/$', login_required(views.RangoList.as_view()), name="rango_list"),
                       url(r'^rango/new/$', login_required(views.RangoCreate.as_view()), name='rango_new'),
                       url(r'^rango/edit/(?P<pk>\d+)$', login_required(views.RangoUpdate.as_view()), name='rango_edit'),
                       url(r'^rango/delete/(?P<pk>\d+)$', login_required(views.RangoDelete.as_view()), name='rango_delete'),

                       url(r'^estacion/$', login_required(views.EstacionList.as_view()), name="estacion_list"),
                       url(r'^estacion/new/$', login_required(views.EstacionCreate.as_view()), name='estacion_new'),
                       url(r'^estacion/edit/(?P<pk>\d+)$', login_required(views.EstacionUpdate.as_view()), name='estacion_edit'),
                       url(r'^estacion/delete/(?P<pk>\d+)$', login_required(views.EstacionDelete.as_view()), name='estacion_delete'),

                       url(r'^trabajador/$', login_required(views.TrabajadorList.as_view()), name="trabajador_list"),
                       url(r'^trabajador/new/$', login_required(views.TrabajadorCreate.as_view()), name='trabajador_new'),
                       url(r'^trabajador/edit/(?P<pk>\d+)$', login_required(views.TrabajadorUpdate.as_view()), name='trabajador_edit'),
                       url(r'^trabajador/delete/(?P<pk>\d+)$', login_required(views.TrabajadorDelete.as_view()), name='trabajador_delete'),

                       url(r'^unidad/$', login_required(views.UnidadList.as_view()), name="unidad_list"),
                       url(r'^unidad/new/$', login_required(views.UnidadCreate.as_view()), name='unidad_new'),
                       url(r'^unidad/edit/(?P<pk>\d+)$', login_required(views.UnidadUpdate.as_view()), name='unidad_edit'),
                       url(r'^unidad/delete/(?P<pk>\d+)$', login_required(views.UnidadDelete.as_view()), name='unidad_delete'),
)