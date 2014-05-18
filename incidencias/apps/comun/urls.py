from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from incidencias.apps.comun import views

urlpatterns = patterns('',
                       url(r'^zona/$', login_required(views.ZonaList.as_view()), name="zona_list"),
                       url(r'^zona/new/$', login_required(views.ZonaCreate.as_view()), name='zona_new'),
                       url(r'^zona/edit/(?P<pk>\d+)$', login_required(views.ZonaUpdate.as_view()), name='zona_edit'),
                       url(r'^zona/delete/(?P<pk>\d+)$', login_required(views.ZonaDelete.as_view()), name='zona_delete'),
                       url(r'^municipio/$', login_required(views.MunicipioList.as_view()), name="municipio_list"),
                       url(r'^municipio/new/$', login_required(views.MunicipioCreate.as_view()), name='municipio_new'),
                       url(r'^municipio/edit/(?P<pk>\d+)$', login_required(views.MunicipioUpdate.as_view()), name='municipio_edit'),
                       url(r'^municipio/delete/(?P<pk>\d+)$', login_required(views.MunicipioDelete.as_view()), name='municipio_delete'),
                       url(r'^parroquia/$', login_required(views.ParroquiaList.as_view()), name="parroquia_list"),
                       url(r'^parroquia/new/$', login_required(views.ParroquiaCreate.as_view()), name='parroquia_new'),
                       url(r'^parroquia/edit/(?P<pk>\d+)$', login_required(views.ParroquiaUpdate.as_view()), name='parroquia_edit'),
                       url(r'^parroquia/delete/(?P<pk>\d+)$', login_required(views.ParroquiaDelete.as_view()), name='parroquia_delete'),
                       url(r'^procedimiento/$', login_required(views.ProcedimientoList.as_view()), name="procedimiento_list"),
                       url(r'^procedimiento/new/$', login_required(views.ProcedimientoCreate.as_view()), name='procedimiento_new'),
                       url(r'^procedimiento/edit/(?P<pk>\d+)$', login_required(views.ProcedimientoUpdate.as_view()),
                           name='procedimiento_edit'),
                       url(r'^procedimiento/delete/(?P<pk>\d+)$', login_required(views.ProcedimientoDelete.as_view()),
                           name='procedimiento_delete'),

                       url(r'^tipoprocedimiento/$', login_required(views.TipoProcedimientoList.as_view()),
                           name="tipoprocedimiento_list"),
                       url(r'^tipoprocedimiento/new/$', login_required(views.TipoProcedimientoCreate.as_view()),
                           name='tipoprocedimiento_new'),
                       url(r'^tipoprocedimiento/edit/(?P<pk>\d+)$', login_required(views.TipoProcedimientoUpdate.as_view()),
                           name='tipoprocedimiento_edit'),
                       url(r'^tipoprocedimiento/delete/(?P<pk>\d+)$', login_required(views.TipoProcedimientoDelete.as_view()),
                           name='tipoprocedimiento_delete'),

                       url(r'^detalletipoprocedimiento/$', login_required(views.DetalleTipoProcedimientoList.as_view()),
                           name="detalletipoprocedimiento_list"),
                       url(r'^detalletipoprocedimiento/new/$', login_required(views.DetalleTipoProcedimientoCreate.as_view()),
                           name='detalletipoprocedimiento_new'),
                       url(r'^detalletipoprocedimiento/edit/(?P<pk>\d+)$',
                           login_required(views.DetalleTipoProcedimientoUpdate.as_view()), name='detalletipoprocedimiento_edit'),
                       url(r'^detalletipoprocedimiento/delete/(?P<pk>\d+)$',
                           login_required(views.DetalleTipoProcedimientoDelete.as_view()), name='detalletipoprocedimiento_delete'),



                       url(r'^comision/$', views.ComisionList.as_view(), name="comision_list"),
                       url(r'^comision/new/$', views.ComisionCreate.as_view(), name='comision_new'),
                       url(r'^comision/edit/(?P<pk>\d+)$', views.ComisionUpdate.as_view(), name='comision_edit'),
                       url(r'^comision/delete/(?P<pk>\d+)$', views.ComisionDelete.as_view(), name='comision_delete'),
)
