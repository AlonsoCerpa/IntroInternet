#!C:\Python34\python
import cgi
import cgitb; cgitb.enable()
import mysql.connector

print("Content-Type: text/html\n")

db= mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='inmobiliaria')

form = cgi.FieldStorage() # se instancia solo una vez
usuario = form.getfirst('usuario', 'empty')
password = form.getfirst('password', 'empty')

if (usuario != 'empty' and password != 'empty'):
        consulta = db.cursor()
        consulta.execute("select * from administradores where usuario = '%s'" % (usuario))
        resultado = consulta.fetchall()
        if (resultado != [] and resultado[0][2] == password):
                print('<meta http-equiv="Refresh" content="0;url=admin.py">"')
        else:
                consulta.execute("select * from inmobiliarias where usuario = '%s'" % (usuario))
                resultado = consulta.fetchall()
                if (resultado != [] and resultado[0][2] == password):
                        print('<meta http-equiv="Refresh" content="0;url=vendedor.py">"')



        """
        if (len(resultado) == 0):
                insertar = db.cursor()
                insertar.execute("insert into administradores values(null,'%s','%s')" % (usuario, password))
                db.commit()
                print ("ID de ultimo registro insertado: %s<br>" % insertar.lastrowid)
                insertar.close()
        else:
                print ("Ya existe") """


        

print("""
<!DOCTYPE html>
<html lang="es">
<head>
	<title>adminUsers</title>
	<meta charset="utf-8">
	<meta name="keywords" content="admin, prettyhouses">
	<link href="estilos.css" rel="stylesheet" type="text/css" media="screen">
	<link rel="stylesheet" href="w3.css">
	<link rel="stylesheet" type="text/css" href="estilosAdmin.css">
</head>

<body>

<header id="headerPrincipal">
	<b><span style="color:red">pretty</span><span style="color:black">houses.com</span></b>
</header>
<nav>
  <ul>
  	<li><a href="#"></a></li>
  </ul>
</nav>

<h1>Iniciar sesion</h1>

""")


print("""
<form name="usuario" action="login.py" method="post">
Usuario: 
<input type="text" name="usuario"><br>
Contrase&ntildea:
<input type="password" name="password"><br>
<input type="submit" value="Ingresar">
</form>
""")  
print ("""
    </body>
    </html>
"""
)    
db.close()
