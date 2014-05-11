from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

from django.contrib import admin
import os
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'incidencias.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^media/(?P<path>.*)$', 'django.contrib.staticfiles.views.serve', {'document_root': settings.STATIC_ROOT}),
	url(r'^$', 'incidencias.apps.autenticar.views.inicio'),
    url(r'^admin/', include(admin.site.urls)),
	#url(r'^autenticar/', include('incidencias.apps.autenticar.urls')),
	url(r'^comun/', include('incidencias.apps.comun.urls')),
	url(r'^novedad/', include('incidencias.apps.novedad.urls')),
)
