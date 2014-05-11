from django.conf.urls import patterns, url

from incidencias.apps.comun import views

urlpatterns = patterns('',
	url(r'^zona/$', views.ZonaList.as_view(), name="zona_list"),
	url(r'^zona/new/$', views.ZonaCreate.as_view(), name='zona_new'),
	url(r'^zona/edit/(?P<pk>\d+)$', views.ZonaUpdate.as_view(), name='zona_edit'),
	url(r'^zona/delete/(?P<pk>\d+)$', views.ZonaDelete.as_view(), name='zona_delete'),
	url(r'^municipio/$', views.MunicipioList.as_view(), name="municipio_list"),
	url(r'^municipio/new/$', views.MunicipioCreate.as_view(), name='municipio_new'),
	url(r'^municipio/edit/(?P<pk>\d+)$', views.MunicipioUpdate.as_view(), name='municipio_edit'),
	url(r'^municipio/delete/(?P<pk>\d+)$', views.MunicipioDelete.as_view(), name='municipio_delete'),
	url(r'^parroquia/$', views.ParroquiaList.as_view(), name="parroquia_list"),
	url(r'^parroquia/new/$', views.ParroquiaCreate.as_view(), name='parroquia_new'),
	url(r'^parroquia/edit/(?P<pk>\d+)$', views.ParroquiaUpdate.as_view(), name='parroquia_edit'),
	url(r'^parroquia/delete/(?P<pk>\d+)$', views.ParroquiaDelete.as_view(), name='parroquia_delete'),
	url(r'^estacion/$', views.EstacionList.as_view(), name="estacion_list"),
	url(r'^estacion/new/$', views.EstacionCreate.as_view(), name='estacion_new'),
	url(r'^estacion/edit/(?P<pk>\d+)$', views.EstacionUpdate.as_view(), name='estacion_edit'),
	url(r'^estacion/delete/(?P<pk>\d+)$', views.EstacionDelete.as_view(), name='estacion_delete'),
	url(r'^procedimiento/$', views.ProcedimientoList.as_view(), name="procedimiento_list"),
	url(r'^procedimiento/new/$', views.ProcedimientoCreate.as_view(), name='procedimiento_new'),
	url(r'^procedimiento/edit/(?P<pk>\d+)$', views.ProcedimientoUpdate.as_view(), name='procedimiento_edit'),
	url(r'^procedimiento/delete/(?P<pk>\d+)$', views.ProcedimientoDelete.as_view(), name='procedimiento_delete'),
	
	url(r'^tipoprocedimiento/$', views.TipoProcedimientoList.as_view(), name="tipoprocedimiento_list"),
	url(r'^tipoprocedimiento/new/$', views.TipoProcedimientoCreate.as_view(), name='tipoprocedimiento_new'),
	url(r'^tipoprocedimiento/edit/(?P<pk>\d+)$', views.TipoProcedimientoUpdate.as_view(), name='tipoprocedimiento_edit'),
	url(r'^tipoprocedimiento/delete/(?P<pk>\d+)$', views.TipoProcedimientoDelete.as_view(), name='tipoprocedimiento_delete'),
	
	url(r'^detalletipoprocedimiento/$', views.DetalleTipoProcedimientoList.as_view(), name="detalletipoprocedimiento_list"),
	url(r'^detalletipoprocedimiento/new/$', views.DetalleTipoProcedimientoCreate.as_view(), name='detalletipoprocedimiento_new'),
	url(r'^detalletipoprocedimiento/edit/(?P<pk>\d+)$', views.DetalleTipoProcedimientoUpdate.as_view(), name='detalletipoprocedimiento_edit'),
	url(r'^detalletipoprocedimiento/delete/(?P<pk>\d+)$', views.DetalleTipoProcedimientoDelete.as_view(), name='detalletipoprocedimiento_delete'),
	
	url(r'^unidad/$', views.UnidadList.as_view(), name="unidad_list"),
	url(r'^unidad/new/$', views.UnidadCreate.as_view(), name='unidad_new'),
	url(r'^unidad/edit/(?P<pk>\d+)$', views.UnidadUpdate.as_view(), name='unidad_edit'),
	url(r'^unidad/delete/(?P<pk>\d+)$', views.UnidadDelete.as_view(), name='unidad_delete'),
	
	url(r'^comision/$', views.ComisionList.as_view(), name="comision_list"),
	url(r'^comision/new/$', views.ComisionCreate.as_view(), name='comision_new'),
	url(r'^comision/edit/(?P<pk>\d+)$', views.ComisionUpdate.as_view(), name='comision_edit'),
	url(r'^comision/delete/(?P<pk>\d+)$', views.ComisionDelete.as_view(), name='comision_delete'),
	
	url(r'^diagnostico/$', views.DiagnosticoList.as_view(), name="diagnostico_list"),
	url(r'^diagnostico/new/$', views.DiagnosticoCreate.as_view(), name='diagnostico_new'),
	url(r'^diagnostico/edit/(?P<pk>\d+)$', views.DiagnosticoUpdate.as_view(), name='diagnostico_edit'),
	url(r'^diagnostico/delete/(?P<pk>\d+)$', views.DiagnosticoDelete.as_view(), name='diagnostico_delete'),
)
