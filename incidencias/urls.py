from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin

from model_report import report
import os

admin.autodiscover()
report.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'incidencias.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),
                       url(r'^media/(?P<path>.*)$', 'django.contrib.staticfiles.views.serve',
                           {'document_root': settings.STATIC_ROOT}),
                       url(r'^$', 'incidencias.apps.autenticar.views.inicio', name="inicio"),
                       url(r'^admin/', include(admin.site.urls)),
                       #url(r'^autenticar/', include('incidencias.apps.autenticar.urls')),
                       url(r'^comun/', include('incidencias.apps.comun.urls')),
                       url(r'^institucion/', include('incidencias.apps.institucion.urls')),
                       url(r'^novedad/', include('incidencias.apps.novedad.urls')),
                       url(r'', include('model_report.urls')),
)
