/* Archivo de funciones JavaScript */
function filtrar_parroquia(id_municipio, id_parroquia)
{$("#"+id_parroquia).attr('innerHTML','')
   option = $("<option></option>").attr({'value':'0','innerHTML':'---------'});
   $("#"+id_parroquia).append(option)

   $.getJSON("/parroquia/ajax",{id_municipio: $("#"+id_municipio).val()}, function(parroquias)
   {
       for (var i = 0; i < parroquias.length; i++)
	   {

          option = $("<option></option>").attr({'value':parroquias[i].value,
			                                    'innerHTML':parroquias[i].nombre});

		  $("#"+id_parroquia).append(option);
	   }

       $("#"+id_parroquia).attr('disabled',false);
   });
}