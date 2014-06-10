from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from incidencias.apps.autenticar import views

urlpatterns = patterns('',
                       url(r'^usuario/$', login_required(views.UsuarioList.as_view()), name="user_list"),
                       url(r'^usuario/search/([\w-]+)/$', login_required(views.UsuarioList.as_view()),
                           name="user_list"),
                       url(r'^usuario/new/$', login_required(views.UsuarioCreate.as_view()), name='user_new'),
                       url(r'^usuario/edit/(?P<pk>\d+)$', login_required(views.UsuarioUpdate.as_view()), name='user_edit'),
                       url(r'^usuario/delete/(?P<pk>\d+)$', login_required(views.UsuarioDelete.as_view()), name='user_delete'),
                       url(r'^login/?$', 'incidencias.apps.autenticar.views.acceso', name='acceso_sistema'),
                       url(r'^logout/?$', 'incidencias.apps.autenticar.views.salir', name='salir_sistema'),
)