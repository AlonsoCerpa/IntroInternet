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

codigo = form.getfirst('codigo', 'empty')
direccion = form.getfirst('direccion', 'empty')
referencia = form.getfirst('referencia', 'empty')
precio = form.getfirst('precio', 'empty')
supTot = form.getfirst('supTot', 'empty')
supConst = form.getfirst('supConst', 'empty')
descripcion = form.getfirst('descripcion', 'empty')
tipo = form.getfirst('tipo', 'empty')

cumple = True
existe = False
creado = False

if (codigo != 'empty' and direccion != 'empty' and referencia != 'empty'
    and precio != 'empty' and supTot != 'empty' and supConst != 'empty'
    and descripcion != 'empty' and tipo != 'empty'):
        #codigo
        if (not re.match("^[A-Z]{3}-[0-9]{6}-[0-9]{3}$", codigo)):
            cumple = False;

        #direccion
        if (re.search("[^a-zA-Z0-9]", direccion)):
            cumple = False;

        #referencia
        if (re.search("[^a-zA-Z0-9]", referencia)):
            cumple = False;
            
        #precio
        if (not (re.search("^[0-9]+.[0-9]+$", precio) or re.search("[0-9]+$", precio))):
            cumple = False;

        #superficie total
        if (not (re.search("^[0-9]+.[0-9]+$", supTot) or re.search("[0-9]+$", supTot))):
            cumple = False;

        #superficie construida
        if (not (re.search("^[0-9]+.[0-9]+$", supConst) or re.search("[0-9]+$", supConst))):
            cumple = False;

        #descripcion
        if (re.search("[^a-zA-Z0-9]", descripcion)):
            cumple = False;

        if (cumple == True):
                if (tipo == "comprar"):
                        tipo = 1
                elif (tipo == "alquilar"):
                        tipo = 2
                inmID = 4
                
                consulta = db.cursor()
                consulta.execute("select * from inmuebles where codigo = '%s'" % (codigo))
                resultado = consulta.fetchall()
                if (len(resultado) == 0):
                    insertar = db.cursor()
                    insertar.execute("insert into inmuebles values(null,'%s','%s','%s','%s','%s','%s','%s','%s', '%s')"
                                     % (codigo, direccion, referencia, precio, supTot, supConst, descripcion, tipo, inmID))
                    db.commit()
                    insertar.close()
                    creado = True
                else:
                    existe = True

print("""
<!DOCTYPE html>
<html lang="es">
<head>
	<title>vendedor</title>
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

<h1>Panel de Vendedor de PrettyHouses.com</h1>

<h3>Gestion de inmuebles</h3>

<script src="scriptAdmin.js"></script>

<div id="nuevaInmobiliaria">
        <h3>Crear nuevo inmueble</h3>
        <form action="vendedor.py" method="post" id="vendedor">
        <div class="whiteSpace">
        """)

if (cumple == False):
    print("""
    No ha ingresado valores correctamente, vuelva a ingresar.<br>
""")
elif (existe == True):
    print("""
    El inmueble ingresado ya existe. Ingrese de nuevo.<br>
""")
elif (creado == True):
    print("""
    El inmueble ha sido creado exitosamente.<br>
""")

print("""
           Codigo:<br>
           <input type="text" name="codigo"><br>
           Direccion:<br>
           <input type="text" name="direccion"><br>
           Referencia:<br>
           <input type="text" name="referencia"><br>
           Precio:<br>
           <input type="text" name="precio"><br>
           Superficie total:<br>
           <input type="text" name="supTot"><br>
           Superficie construida:<br>
           <input type="text" name="supConst"><br>
           Descripcion:<br>
           <input type="text" name="descripcion"><br>
           Tipo:<br>
           <select name="tipo" form="vendedor">
              <option value="comprar">Comprar</option>
              <option value="alquilar">Alquilar</option>
           </select><br><br>
           <input type="submit" value="Crear nuevo inmueble">
        </div>
        </form>
</div>

</body>
</html>
""")

db.close()
