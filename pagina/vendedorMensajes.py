#!C:\Python34\python
import cgi
import cgitb
cgitb.enable()

form = cgi.FieldStorage()

nombre = form.getfirst('nombre', 'empty')
correo = form.getfirst('correo', 'empty')
telefono = form.getfirst('telefono', 'empty')
mensaje = form.getfirst('mensaje', 'empty')

nombre = cgi.escape(nombre)
correo = cgi.escape(correo)
telefono = cgi.escape(telefono)
mensaje = cgi.escape(mensaje)

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
	<li class="activo1"><a href="iniciarSesion.html">Iniciar Sesi&oacuten</a></li>
    <li class="activo"><a href="crearUsuario.html">Crear usuario</a></li>
  </ul>
</nav>

<h1>Mensajes recibidos</h1>
""")

print("Nombre: " + nombre + "<br>")
print("Correo: " + correo + "<br>")
print("Telefono: " + telefono + "<br>")
print("Mensaje: " + mensaje + "<br>")
	
print("""	

<footer>
	<h3>Informaci&oacuten adicional</h3>
	<a href="contacto.html"><span id="contacto">Contacto</span></a>
	<a href="mapaSitio.html"><span id="mapaSitio">Mapa del sitio</span></a>
</footer>

<script src="script.js"></script>
</body>
</html>
""")
