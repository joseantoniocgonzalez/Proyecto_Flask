#Importamos lo que vamos a necesitar de flask
from flask import Flask, render_template,abort
# Importamos la libreria os del sistema para utilizar environ
import os 
# La aplicación nos va permitir mostrar la información del fichero books.json
# Por tanto, importamos json para leer el fichero 
import json 
# Definimos la variable app por Flask
app = Flask(__name__)
# Leemos el fichero y lo añadimos a una variable 
with open ("books.json") as fichero:
    info = json.load(fichero)

# Definimos la ruta principal de la página de incio 

@app.route('/',methods=["GET","POST"])
def inicio():
	return render_template("inicio.html", lista_libros=info)

# Definimos la ruta secundaria donde va estar la información del libro al que accedamos. La función recibe el codigo isbn
@app.route('/libro/<isbn>',methods=["GET","POST"])
def info_libros(isbn):
    for elem in info:
        if "isbn" in elem.keys() and isbn == elem["isbn"]:
        	return render_template("detalle_libro.html", detalle_libro=elem)
    abort(404)

# Definimos la tercera ruta de las categorías.
@app.route('/categoria/<categoria>',methods=["GET","POST"])
def categoria(categoria):
    for category in info:
        if "categories" in category.keys() and categoria in category["categories"]:
            return render_template("categoria.html", lista_libros=info, categoria=categoria)


#Probar en el entorno de desarrollo
#app.run(debug=True)




