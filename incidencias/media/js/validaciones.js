function validar_solo_texto(e) {
	/**
	* Funci&oacute;n que permite validar que solo pueda introducirse cadenas de texto sin n&uacute;meros
	* Comas(44) y puntos(46)
	* flecha hacia la derecha - 39
	* flecha hacia la izquierda - 37
	* Tecla Del o Supr - 35
	* Backspace - 8
	* Enter - 13
	*/
	tecla = (document.all) ? e.keyCode : e.which;
    if (tecla==8) return true; // 3
    patron =/[A-Za-zñÑ\s]/; // 4
    te = String.fromCharCode(tecla); // 5
    return patron.test(te); // 6
}

function validar_solo_numeros(e) {
	/**
	* Funci&oacute;n que permite validar que solo se puedan introducir n&uacute;meros
	*/
    tecla = (document.all) ? e.keyCode : e.which;
    if (tecla==8) return true; // 3
    patron =/\d/; // 4
    te = String.fromCharCode(tecla); // 5
    return patron.test(te); // 6
}
