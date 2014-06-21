/* Archivo de funciones JavaScript */
function filtrar_parroquia(url, codmun, codpar, campopar) {
	$.getJSON(url,{codmun: codmun, codpar: codpar, campopar:campopar}, function(datos) {
		if (datos.resultado) {
			$("#"+campopar).html(datos.parroquias);
			$("#"+campopar).removeAttr("disabled");
		}
		else {
			alert(datos.error);
		}
   });
}

function mostrar_unidad(url, id_unidad, valor) {
	$.getJSON(url, {valor: valor}, function (datos) {
		if (datos.resultado) {
			$("#"+id_unidad.replace("-unidad", "-detalle_unidad")).val(datos.unidad);
		}
		else {
			alert(datos.error);
		}
	});
}

function mostrar_comision(url, id_comision, valor) {
	$.getJSON(url, {valor: valor}, function (datos) {
		if (datos.resultado) {
			$("#"+id_comision.replace("-comision", "-detalle_comision")).val(datos.comision);
		}
		else {
			alert(datos.error);
		}
	});
}
