var numUsers;

function eliminar()
{
	var padre = document.getElementById("listaUsers");
	var hijo, hijoAux;
	numUsers = listaUsers.length;
	
	for (var i = 0; i < numUsers; i++)
	{
		hijoAux = document.getElementById("checkUser" + i);

		if (hijoAux.checked == true)
		{
			padre.parentNode.removeChild(padre.childNodes[i]);
		}
	}
}

function marcar(source, clase)
{
	var marca = document.getElementsByClassName(clase);
	
	for (var i = 0; i < marca.length; i++)
		marca[i].checked=source.checked;
}