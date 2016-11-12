#!C:\Python34\python
import cgi
import cgitb
cgitb.enable()

form = cgi.FieldStorage()

print("""
<!DOCTYPE html>
<html lang="es">
<head>
	<title>Detalles dee inmueble</title>
	<meta charset="utf-8" >
	<meta name="keywords" content="detalles, inmueble">
	<meta name="viewport" content="width=device-width, initial-scale=1">
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
	<li class="activo1"><a href="iniciarSesion.html">Iniciar Sesi&oacuten</a></li>
    <li class="activo"><a href="crearUsuario.html">Crear usuario</a></li>
  </ul>
</nav>

<div id="descripcion">
	<span id="dirDet">Librer&iacutea C.C. Alcal&aacute Magna, C/ Valent&iacuten Juara Bellot, 4</span><br>
	<span id="costoDet">$500,000</span><br>
	<span id="datosDet">2 ba&ntildeos - 4 cuartos - 180 m2
	</span><br>
	<span id="tipoDet">Casa familiar moderna</span>
</div>

<div id="w3-content">
""")

numFotos = 7

for i in range(numFotos):
	print('<img class="mySlides" src="casa' + str(i) + '.jpg" alt="foto' + str(i) + '">')

print("""
	<a class="w3-btn-floating" style="position:absolute;top:45%;left:0" onclick="plusDivs(-1)">
	&#10094;</a>
	<a class="w3-btn-floating" style="position:absolute;top:45%;right:0" onclick="plusDivs(+1)">
	&#10095;</a>
</div>

    <div id="contactoVendedor">
		<form action="vendedorMensajes.py" method="post"> 
        <div id="tituloContacto">
            <p>Deseas saber mas de este inmueble?</p>
        </div>
        <div id="datos">
			<p>Nombre:</p>
			<input type="text" name="nombre" size="30"><br>
			<p>Direccion de Correo:</p>
			<input type="text" name="correo" size="30"><br>
			<p>Telefono:</p>
			<input type="text" name="telefono" size="30"><br>
			<p>Mensaje:</p>
			<textarea name="mensaje" cols="40" rows="4"></textarea>
        </div>
        <div id="ingreso">
			<input type="submit" value="Contactar"><br>
        </div>
		</form>
    </div>


<footer>
	<h3>Informaci&oacuten adicional</h3>
	<a href="contacto.html"><span id="contacto">Contacto</span></a>
	<a href="mapaSitio.html"><span id="mapaSitio">Mapa del sitio</span></a>
</footer>

<script src="script.js"></script>

</body>
</html>
""")
