# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.utils import simplejson
from django.core.management import call_command
from django.conf import settings
from datetime import datetime

from incidencias.apps.comun.models import Zona, Municipio, Parroquia, TipoProcedimiento, DetalleTipoProcedimiento, \
    Comision
from incidencias.apps.institucion.models import Estacion
    
import os


# Vistas genericas para controlar el CRUD del modelo Zona

class ZonaList(ListView):
    """!
    Clase que permite consultar una zona

    @author Iraida Sanabria
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
    @date 06-05-14
    @version 1.0
    """
    model = Zona
    paginate_by = 10

    def get_queryset(self):
        if len(self.args) > 0:
            return Zona.objects.filter(nombre__icontains=self.args[0])
        else:
            return Zona.objects.all()


class ZonaCreate(CreateView):
    """!
    Clase que permite crear una nueva zona

    @author Iraida Sanabria
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
    @date 06-05-14
    @version 1.0
    """
    model = Zona
    success_url = reverse_lazy('zona_list')
    

class ZonaUpdate(UpdateView):
    """!
    Clase que permite modificar una zona

    @author Iraida Sanabria
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
    @date 06-05-14
    @version 1.0
    """
    model = Zona
    success_url = reverse_lazy('zona_list')
    

class ZonaDelete(DeleteView):
    """!
    Clase que permite eliminar una zona

    @author Iraida Sanabria
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
    @date 06-05-14
    @version 1.0
    """
    model = Zona
    success_url = reverse_lazy('zona_list')


# Vistas genericas para controlar el CRUD del modelo Municipio
class MunicipioList(ListView):
    model = Municipio
    paginate_by = 10

    def get_queryset(self):
        if len(self.args) > 0:
            return Municipio.objects.filter(nombre__icontains=self.args[0])
        else:
            return Municipio.objects.all()


class MunicipioCreate(CreateView):
    """!
    Clase que permite crear un nuevo municipio

    @author Iraida Sanabria
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
    @date 06-05-14
    @version 1.0
    """
    model = Municipio
    success_url = reverse_lazy('municipio_list')


class MunicipioUpdate(UpdateView):
    """!
    Clase que permite modificar un municipio

    @author Iraida Sanabria
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
    @date 06-05-14
    @version 1.0
    """
    model = Municipio
    success_url = reverse_lazy('municipio_list')


class MunicipioDelete(DeleteView):
    """!
    Clase que permite eliminar un municipio

    @author Iraida Sanabria
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
    @date 06-05-14
    @version 1.0
    """
    model = Municipio
    success_url = reverse_lazy('municipio_list')


# Vistas genericas para controlar el CRUD del modelo Parroquia
class ParroquiaList(ListView):
    model = Parroquia
    paginate_by = 10

    def get_queryset(self):
        if len(self.args) > 0:
            return Parroquia.objects.filter(nombre__icontains=self.args[0])
        else:
            return Parroquia.objects.all()


class ParroquiaCreate(CreateView):
    """!
    Clase que permite crear una nueva parroquia

    @author Iraida Sanabria
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
    @date 06-05-14
    @version 1.0
    """
    model = Parroquia
    success_url = reverse_lazy('parroquia_list')


class ParroquiaUpdate(UpdateView):
    """!
    Clase que permite modificar una parroquia

    @author Iraida Sanabria
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
    @date 06-05-14
    @version 1.0
    """
    model = Parroquia
    success_url = reverse_lazy('parroquia_list')


class ParroquiaDelete(DeleteView):
    """!
    Clase que permite eliminar una parroquia

    @author Iraida Sanabria
    @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
    @date 06-05-14
    @version 1.0
    """
    model = Parroquia
    success_url = reverse_lazy('parroquia_list')


# Vistas genericas para controlar el CRUD del modelo TipoProcedimiento
class TipoProcedimientoList(ListView):
    model = TipoProcedimiento
    paginate_by = 10

    def get_queryset(self):
        """!
        Descripción del método o función

        @author Yanina Guillén
        @copyright <a href='http://www.gnu.org/licenses/gpl-2.0.html'>GNU Public License versión 2 (GPLv2)</a>
        @date 05-05-14
        @param[in] nombre_parametro  Indica el tipo de parámetro y que es lo que recibe
        @return Listado de tipos de procedimientos
        """
        if len(self.args) > 1:
            if self.args[0] == '0' and self.args[1] == '0':
                return TipoProcedimiento.objects.all()
            elif self.args[0] == '0' and self.args[1] != '0':
                return TipoProcedimiento.objects.filter(nombre__icontains=self.args[1])
            elif self.args[0] != '0' and self.args[1] == '0':
                return TipoProcedimiento.objects.filter(division=self.args[0])
            elif self.args[0] != '0' and self.args[1] != '0':
                return TipoProcedimiento.objects.filter(division=self.args[0], nombre__icontains=self.args[1])
        else:
            return TipoProcedimiento.objects.all()


class TipoProcedimientoCreate(CreateView):
    model = TipoProcedimiento
    success_url = reverse_lazy('tipoprocedimiento_list')


class TipoProcedimientoUpdate(UpdateView):
    model = TipoProcedimiento
    success_url = reverse_lazy('tipoprocedimiento_list')


class TipoProcedimientoDelete(DeleteView):
    model = TipoProcedimiento
    success_url = reverse_lazy('tipoprocedimiento_list')


# Vistas genericas para controlar el CRUD del modelo DetalleTipoProcedimiento
class DetalleTipoProcedimientoList(ListView):
    model = DetalleTipoProcedimiento
    paginate_by = 10

    def get_queryset(self):
        if len(self.args) > 0:
            return DetalleTipoProcedimiento.objects.filter(nombre__icontains=self.args[0])
        else:
            return DetalleTipoProcedimiento.objects.all()


class DetalleTipoProcedimientoCreate(CreateView):
    model = DetalleTipoProcedimiento
    success_url = reverse_lazy('detalletipoprocedimiento_list')


class DetalleTipoProcedimientoUpdate(UpdateView):
    model = DetalleTipoProcedimiento
    success_url = reverse_lazy('detalletipoprocedimiento_list')


class DetalleTipoProcedimientoDelete(DeleteView):
    model = DetalleTipoProcedimiento
    success_url = reverse_lazy('detalletipoprocedimiento_list')


# Vistas genericas para controlar el CRUD del modelo Comision
class ComisionList(ListView):
    model = Comision
    paginate_by = 10

    def get_queryset(self):
        if len(self.args) > 0:
            return Comision.objects.filter(nombre__icontains=self.args[0])
        else:
            return Comision.objects.all()


class ComisionCreate(CreateView):
    model = Comision
    success_url = reverse_lazy('comision_list')


class ComisionUpdate(UpdateView):
    model = Comision
    success_url = reverse_lazy('comision_list')


class ComisionDelete(DeleteView):
    model = Comision
    success_url = reverse_lazy('comision_list')
    
    
"""
@note: Funciones para el respaldo y restauración de datos
"""
def backup(request):
    respaldo = "exito"
    output_filename = os.path.join(settings.BASE_DIR, "incidencias/backup/respaldo_%s.json" % datetime.now().strftime("%d-%m-%Y_%I-%M%p"))
    output = open(output_filename, "w")
    try:
        call_command('dumpdata', format='json', indent=4, stdout=output)
    except Exception, e:
        print e
        respaldo = "error"
    output.close()
        
    return render_to_response('base.html', {'respaldo': respaldo}, context_instance=RequestContext(request))
    
def restore(request):
    loaddata = "exito"
    directorio = os.path.join(settings.BASE_DIR, "incidencias/backup")
    archivos = []
    try:
        for root, dirs, files in os.walk(directorio):
            for file in files:
                if file.endswith(".json"):
                    archivos.append(os.path.join(root, file))
                    
        archivos = sorted(archivos, reverse=True)
        call_command('loaddata', archivos[0])
    except Exception, e:
        print e
        loaddata = "error"
        
    return render_to_response('base.html', {'loaddata': loaddata}, context_instance=RequestContext(request))

"""
@note Funciones AJAX
"""


def filtrar_parroquia(request):
    parroquias = []
    if request.GET.has_key('id_municipio'):
        municipio = request.GET['id_municipio']
        parroquias = [{'value': p.id, 'nombre': p.nombre}
                      for p in Parroquia.objects.filter(municipio=municipio).order_by('nombre')]

    return HttpResponse(simplejson.dumps(parroquias))
    
    
"""
@note: Funciones de vista para los reportes
"""

from django_xhtml2pdf.utils import generate_pdf

import cStringIO as StringIO
from xhtml2pdf import pisa
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from cgi import escape

def render_to_pdf(template_src, context_dict):
    template = get_template(template_src)
    context = Context(context_dict)
    html  = template.render(context)
    result = StringIO.StringIO()

    pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("UTF-8")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), mimetype='application/pdf')
    return HttpResponse('We had some errors<pre>%s</pre>' % escape(html))
    
def reporte(request):
    estaciones = Estacion.objects.all()
    print estaciones
    c = {'logo': os.path.join(settings.BASE_DIR, "incidencias/media/images/logo.png"), 'estaciones': estaciones}
    return render_to_pdf('reportes/novedades_x_estacion.html', c)

"""
def reporte(request):
	resp = HttpResponse(content_type='application/pdf')
	template = get_template('reportes/prueba.html').render(Context({'mensaje':'esto es una prueba'}))
	result = generate_pdf('reportes/prueba.html', file_object=resp)
	return result
"""
