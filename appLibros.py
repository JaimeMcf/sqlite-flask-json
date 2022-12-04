from flask import Flask, render_template, request, jsonify
import libros1 
from libros0 import create 


app =Flask(__name__)

@app.route('/', methods=['GET'])
def get_libros():
    libro1 = libros1.get_libros()
    return  jsonify(libro1)


@app.route('/', methods =['POST'])
def insertLibro():
    libros_details = request.get_json()
    nombre = libros_details['nombre']
    autor = libros_details['autor']
    precio =libros_details['precio']
    resultado = libros1.insertLibros[nombre, autor, precio]
    return  jsonify(resultado)  

@app.route('/', methods = ['PUT'])
def updateLibros():
   libros_details = request.get_json()
   nombre = libros_details['nombre']
   autor = libros_details['autor']
   precio =libros_details['precio']
   resultado = libros1.updatelibros[nombre, autor, precio]
   return  jsonify(resultado)  


@app.route('/', methods =['DELETE'])
def deleteLibros(id):
    resultado = libros1.deletelibros(id)
    return jsonify(resultado)
    
    
@app.route('/<id>', methods=['GET'])
def selec_libros(id):
    resultado = libros1.selec_libros(id)
    return jsonify(resultado)

if __name__== '__main__':
    create 

app.run(host='0.0.0.0', port=8000, debug=False)