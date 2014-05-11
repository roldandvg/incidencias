from django.conf.urls import patterns, url

from incidencias.apps.novedad import views

urlpatterns = patterns('',
	url(r'^novedad/$', views.NovedadList.as_view(), name="novedad_list"),
	url(r'^novedad/new/$', views.NovedadCreate.as_view(), name='novedad_new'),
	url(r'^novedad/edit/(?P<pk>\d+)$', views.NovedadUpdate.as_view(), name='novedad_edit'),
	url(r'^novedad/delete/(?P<pk>\d+)$', views.NovedadDelete.as_view(), name='novedad_delete'),
)
