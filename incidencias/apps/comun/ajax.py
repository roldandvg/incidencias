# -*- coding: utf-8 -*-
from django.http import HttpResponse
from incidencias.apps.comun.models import Parroquia, Comision
from incidencias.apps.institucion.models import Unidad
import json

def update_parroquia(request):
	try:
		if not request.is_ajax():
			return HttpResponse(json.dumps({'resultado': False, 'error': 'No se puede procesar la petición'}))
		
		codmun = request.GET.get('codmun', None)
		out = "<option>Seleccione...</option>"
		
		if codmun and codmun != "0":
			codpar = request.GET['codpar']
			for p in Parroquia.objects.filter(municipio=codmun):
				selected = ''
				if codpar == p.id:
					selected = "selected='selected'"
				out = "%s<option value='%s' %s>%s</option>" % (out, p.id, selected, p.nombre)
				
		return HttpResponse(json.dumps({'resultado': True, 'parroquias': out}))
		
	except Exception, e:
		return HttpResponse(json.dumps({'resultado': False, 'error': e}))


def mostrar_comision(request):
	try:
		if not request.is_ajax():
			return HttpResponse(json.dumps({'resultado': False, 'error': 'No se puede procesar la petición'}))
			
		id_comision = request.GET.get('valor', None)
		
		if id_comision:
			descripcion = ""
			if Comision.objects.filter(pk=id_comision):
				comision = Comision.objects.get(pk=id_comision)
				descripcion = comision.descripcion
							
			return HttpResponse(json.dumps({'resultado': True, 'comision': descripcion}))
		else:
			return HttpResponse(json.dumps({'resultado': False, 'error': 'Debe seleccionar la unidad para mostrar los detalles'}))
	except Exception, e:
		return HttpResponse(json.dumps({'resultado': False, 'error': e}))
	
def mostrar_unidad(request):
	try:
		if not request.is_ajax():
			return HttpResponse(json.dumps({'resultado': False, 'error': 'No se puede procesar la petición'}))
			
		id_unidad = request.GET.get('valor', None)
		
		if id_unidad:
			tipo_unidad = ""
			if Unidad.objects.filter(pk=id_unidad):
				unidad = Unidad.objects.get(pk=id_unidad)
				tipo_unidad = unidad.get_tipo()
			
			return HttpResponse(json.dumps({'resultado': True, 'unidad': tipo_unidad}))
		else:
			return HttpResponse(json.dumps({'resultado': False, 'error': 'Debe seleccionar la unidad para mostrar los detalles'}))
	except Exception, e:
		return HttpResponse(json.dumps({'resultado': False, 'error': e}))
