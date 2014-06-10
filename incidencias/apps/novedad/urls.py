from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from incidencias.apps.novedad import views

urlpatterns = patterns('',
                       url(r'^diagnostico/$', views.DiagnosticoList.as_view(), name="diagnostico_list"),
                       url(r'^diagnostico/search/([\w-]+)/$', login_required(views.DiagnosticoList.as_view()),
                           name="diagnostico_list"),
                       url(r'^diagnostico/new/$', views.DiagnosticoCreate.as_view(), name='diagnostico_new'),
                       url(r'^diagnostico/edit/(?P<pk>\d+)$', views.DiagnosticoUpdate.as_view(),
                           name='diagnostico_edit'),
                       url(r'^diagnostico/delete/(?P<pk>\d+)$', views.DiagnosticoDelete.as_view(),
                           name='diagnostico_delete'),
                       url(r'^$', login_required(views.NovedadList.as_view()), name="novedad_list"),
                       #url(r'^new/$', login_required(views.NovedadCreate.as_view()), name='novedad_new'),
                       #url(r'^edit/(?P<pk>\d+)$', login_required(views.NovedadUpdate.as_view()),
                       #    name='novedad_edit'),
                       #url(r'^delete/(?P<pk>\d+)$', login_required(views.NovedadDelete.as_view()),
                       #    name='novedad_delete'),
                       #url(r'^inlines/estructura/new/$', login_required(views.NovedadIncendioEstructura.as_view()),
                       #    name='novedad_estructura_new'),

                       #url(r'^incendio/new/$', 'incidencias.apps.novedad.views.novedad_incendio',
                       #    name='incendio_new'),
                       url(r'^incendio/new/$', views.NovedadIncendioCreateView.as_view(), name='incendio_new'),
)
