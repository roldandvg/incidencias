# -*- coding: utf-8 -*-
#from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.utils import simplejson

from incidencias.apps.comun.models import Zona, Municipio, Parroquia, TipoProcedimiento, DetalleTipoProcedimiento, \
    Comision


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
@note Funciones AJAX
"""


def filtrar_parroquia(request):
    parroquias = []
    if request.GET.has_key('id_municipio'):
        municipio = request.GET['id_municipio']
        parroquias = [{'value': p.id, 'nombre': p.nombre}
                      for p in Parroquia.objects.filter(municipio=municipio).order_by('nombre')]

    return HttpResponse(simplejson.dumps(parroquias))