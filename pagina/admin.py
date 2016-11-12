#!C:\Python34\python
import cgi
import cgitb
import mysql.connector
import re

cgitb.enable()

db= mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='inmobiliaria')

form = cgi.FieldStorage()

usuario = form.getfirst('usuario', 'empty')
password = form.getfirst('password', 'empty')
codigo = form.getfirst('codigo', 'empty')
nombre = form.getfirst('nombre', 'empty')
ruc = form.getfirst('ruc', 'empty')
email = form.getfirst('email', 'empty')
direccion = form.getfirst('direccion', 'empty')
telefono = form.getfirst('telefono', 'empty')
celular = form.getfirst('celular', 'empty')

cumple = True
existe = False
creado = False

if (usuario != 'empty' and password != 'empty' and codigo != 'empty'
    and nombre != 'empty' and ruc != 'empty' and email != 'empty'
    and direccion != 'empty' and telefono != 'empty' and celular != 'empty'):
    #usuario
    if (re.search("[^0-9a-z]+", usuario)):
        cumple = False

    #password
    if (not (re.search("[A-Z].*[A-Z]", password) and re.search("[^a-zA-Z0-9]+", password))):
        cumple = False

    #codigo
    if (not re.match("^[A-Z]{3}-[0-9]{6}$", codigo)):
        cumple = False

    #nombre
    if (re.search("[^a-zA-Z0-9]+", nombre)):
        cumple = False

    #ruc
    if (not re.search("^[0-9]{1,11}$", ruc)):
        cumple = False

    #email
    if (not re.search("^[a-zA-Z0-9._%+-]+@[a-z0-9.-]+(.[a-z])+$", email)):
        cumple = False

    #direccion
    if (re.search("[^a-zA-Z0-9]", direccion)):
        cumple = False

    #telefono
    if (re.search("[^0-9\-]", telefono)):
        cumple = False

    #celular
    if (re.search("[^0-9\-]", celular)):
        cumple = False

    if (cumple == True):
        consulta = db.cursor()
        consulta.execute("select * from inmobiliarias where usuario = '%s'" % (usuario))
        resultado = consulta.fetchall()
        if (len(resultado) == 0):
            insertar = db.cursor()
            insertar.execute("insert into inmobiliarias values(null,'%s','%s','%s','%s','%s','%s','%s','%s', '%s')"
                             % (usuario, password, codigo, nombre, ruc, email, direccion, telefono, celular))
            db.commit()
            insertar.close()
            creado = True
        else:
            existe = True

print("""
<!DOCTYPE html>
<html lang="es">
<head>
	<title>admin</title>
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

<h3>Gestion de inmobiliarias</h3>

<script src="scriptAdmin.js"></script>

<div id="nuevaInmobiliaria">
        <h3>Crear nueva inmobiliaria</h3>
        <form action="admin.py" method="post">
        <div class="whiteSpace">
        """)

if (cumple == False):
    print("""
    No ha ingresado valores correctamente, vuelva a ingresar.<br>
""")
elif (existe == True):
    print("""
    El usuario ingresado ya existe. Ingrese de nuevo.<br>
""")
elif (creado == True):
    print("""
    El usuario ha sido creado exitosamente.<br>
""")

print("""
           Usuario:<br>
           <input type="text" name="usuario"><br>
           Password:<br>
           <input type="password" name="password"><br>
           Codigo:<br>
           <input type="text" name="codigo"><br>
           Nombre:<br>
           <input type="text" name="nombre"><br>
           RUC:<br>
           <input type="text" name="ruc"><br>
           Email:<br>
           <input type="text" name="email"><br>
           Direccion:<br>
           <input type="text" name="direccion"><br>
           Telefono:<br>
           <input type="text" name="telefono"><br>
           Celular:<br>
           <input type="text" name="celular"><br><br>
           <input type="submit" value="Crear nueva inmobiliaria">
        </div>
        </form>
</div>

</body>
</html>
""")

db.close()

