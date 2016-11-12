#!C:\Python34\python
import cgi
import cgitb
cgitb.enable()

print("""
<!DOCTYPE html>
<html lang="es">
<head>
	<title>Pretty Houses</title>
	<meta charset="utf-8">
	<meta name="keywords" content="html, estilos">
	<link href="estilos.css" rel="stylesheet" type="text/css" media="screen">
	<link rel="stylesheet" href="w3.css">
</head>

<body>

<header id="headerPrincipal">
	<b><span style="color:red">pretty</span><span style="color:black">houses.com</span></b>
</header>


<nav>
  <ul>
    <li><a href="pagina_principal.html">Comprar</a></li>
    <li><a href="venderInmuebles.html">Vender</a></li>
    <li><a href="quienesSomos.html">Qui&eacutenes Somos</a></li>
    <li class="activo1"><a href="login.py">Iniciar Sesi&oacuten</a></li>
    <li class="activo"><a href="crearUsuario.html">Crear usuario</a></li>
  </ul>
</nav>

<section id="ventas">
	<header>
		<h2>Inmuebles a la venta</h2>
	</header>
""")

cont = 0

for cont in range(7):
	print ("""
	<div class="inmueble" id="casa""")
	print(str(cont))
	print("""">
	<a href="paginadeinmueble.html"><img src="casa""")
	print(str(cont))
	print(""".jpg" alt="casa""")
	print(str(cont))
	print("""" class="imgCasa"></a>
	<div class="infoInmueble">
		<a href="paginadeinmueble.html"><span class="direc">Librer&iacutea C.C. Alcal&aacute Magna, C/ Valent&iacuten Juara Bellot, 4</span></a>
		<br><br>
		<span class="costo">$500,000</span><br>
		<span class="datos">2 ba&ntildeos - 4 cuartos - 180 m2
		</span><br>
		<span class="tipo">Casa familiar moderna
		</span>
	</div>
	</div>
	""")
	
print("""	
</section>

<footer>
	<h3>Informaci&oacuten adicional</h3>
	<a href="contacto.html"><span id="contacto">Contacto</span></a>
	<a href="mapaSitio.html"><span id="mapaSitio">Mapa del sitio</span></a>
</footer>

<script src="script.js"></script>
</body>
</html>
""")
