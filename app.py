from flask import Flask, render_template, abort
import json
import os


app=Flask(__name__)

with open("books.json") as libros:
    datos=json.load(libros)

@app.route('/')
def inicio():
    nombre='Omar Elhani Botkala'
    return render_template('inicio.html', libros=datos, nombre=nombre)


@app.route('/libro/<isbn>')
def libro(isbn):
    for lib in datos:
        if "isbn" in lib.keys() and isbn == lib["isbn"]:
            return render_template('libros.html', libro=lib)

    return abort(404) 
@app.route('/categoria/<categoria>')
def categoria(categoria):
    for i in datos:
        if "categories" in i.keys() and categoria in i["categories"]:
            return render_template("categoria.html",libros=datos,categoria=categoria)
    abort(404)


port=os.environ["PORT"]
app.run('0.0.0.0', int(port), debug=True)