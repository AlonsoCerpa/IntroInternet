#!C:\Python34\python
import cgi
import cgitb
cgitb.enable()

form = cgi.FieldStorage()

print("""
<!DOCTYPE html>
<html lang="es">
<head>
	<title>adminUsers</title>
	<meta charset="utf-8">
	<meta name="keywords" content="admin, prettyhouses">
	<link rel="stylesheet" href="estilos.css">
	<link rel="stylesheet" href="w3.css">
	<link rel="stylesheet" type="text/css" href="estilosAdmin.css">
</head>

<body>

<header id="headerPrincipal">
	<b><span style="color:red">pretty</span><span style="color:black">houses.com</span></b>
</header>

<nav>
  <ul>
    <li><a href="users.html">Usuarios</a></li>
    <li><a href="ventas.html">Ventas</a></li>
    <li><a href="vendedores.html">Vendedores</a></li>
    <li class="activo2"><a href="index.py">Cerrar sesion</a></li>
  </ul>
</nav>

<h1>Administrador de PrettyHouses.com</h1>
<article id="usuarios">
	<h2>Usuarios</h2>
	<form action="admin.py" method="post">
	<ul id="listaUsers">
""")

usuarios = [
"Fabrizio Flores",
"Giancarlo Anco",
"Alonso Cerpa",
"Rodrigo Sanchez",
"Marco Perez",
"Antonio Valdivia",
"Carl Rodriguez",
"Gabriela Delgado",
"Alejandra Salas",
"Gonzalo Guzman",
"German Chavez",
"Pablo Ugarte",
"Jose Mendez"]

totalUsuarios = len(usuarios)
usuariosElim = 0
posElim = 0

for contUsuarios in range(totalUsuarios):
	if form.getvalue('user' + str(contUsuarios)):
		usuarios.pop(posElim)
		usuariosElim += 1
	else:
		posElim += 1

totalUsuarios -= usuariosElim

for contUsuarios in range(totalUsuarios):
	print('<li><input type="checkbox" class="listaUsuarios" name="user' + str(contUsuarios) + '"> ' + usuarios[contUsuarios] + '</li>')
	
print("""
	</ul>
	<input type="checkbox" onClick="marcar(this, 'listaUsuarios')"> Marcar/Desmarcar todos
	<div id="botonElimUser">
	<input type="submit" value="Eliminar usuario(s)">
	</div>
	</form>
</article>

<article id="venta">
	<h2>Aprobar ventas</h2>
	<form action="admin.py" method="post">
	<ul>
""")

casas = [
"Las Alamedas 123",
"Aviacion 456",
"Ramos 147",
"Perales 245",
"Av. Peru 947",
"Goyoneche 714"]

casasCostos = [
500000,
125000,
1000000,
247000,
2500000,
489000]

totalCasas = len(casas)
casasElim = 0
posElim = 0

for contCasas in range(totalCasas):
	if form.getvalue('casa' + str(contCasas)):
		casas.pop(posElim)
		casasCostos.pop(posElim)
		casasElim += 1
	else:
		posElim += 1
		
totalCasas -= casasElim

for contCasas in range(totalCasas):
	print('<li><input type="checkbox" class="listaCasas"  name="casa' + str(contCasas) + '">')
	print("""
	<span class="casa">
	""")
	print(casas[contCasas])
	print("""</span><br> Info:<br>
			<span class="costo">Costo: $
	""")
	print(str(casasCostos[contCasas]))
	print("""</span><br><span class="datos">Datos: 2 ba&ntildeos - 4 cuartos - 180 m2</span>
			<br><span class="tipo">Tipo: Casa familiar moderna</span>
		</li>
	""")
	
print("""
	</ul>
	<input type="checkbox" onClick="marcar(this, 'listaCasas')"> Marcar/Desmarcar todos
	<div id="botonElimVenta">
	<input type="submit" value="Aprobar Venta(s)">
	</div>
	</form>
</article>

<article id="vendedores">
	<h2>Vendedores</h2>
	<form action="admin.py" method="post">
	<ul>
""")
	
vendedores = [
"Rodrigo Sanchez",
"Marco Perez",
"Antonio Valdivia",
"Carl Rodriguez",
"Gabriela Delgado"]
	
totalVendedores = len(vendedores)
posElim = 0
vendedoresElim = 0

for contVendedores in range(totalVendedores):
	if form.getvalue('vendedor' + str(contVendedores)):
		vendedores.pop(posElim)
		vendedoresElim += 1
	else:
		posElim += 1
	
totalVendedores -= vendedoresElim	

for contVendedores in range(totalVendedores):
	print('<li><input type="checkbox" class="listaVendedores" name="vendedor' + str(contVendedores) + '">' + vendedores[contVendedores] + '</li>')
	
print("""</ul>
	<input type="checkbox" onClick="marcar(this, 'listaVendedores')"> Marcar/Desmarcar todos
	<div id="botonElimVend">
	<input type="submit" value="Eliminar vendedor(es)">
	</div>
	</form>
</article>

<script src="scriptAdmin.js"></script>

</body>
</html>
""")

