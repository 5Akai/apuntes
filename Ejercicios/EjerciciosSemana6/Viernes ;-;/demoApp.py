from flask import Flask, request, Response, jsonify, session, render_template
from demoModulo import *

#########################################################################
# Creamos una instancia de Flask
#########################################################################
app = Flask(__name__, template_folder="templates")


#########################################################################
# Rutas de la aplicación Flask
#########################################################################

# Ruta: http://dominio.com/
@app.route("/", methods=["GET"])
def index():
    return f'<h1 style="color: teal;">Hola Mundo !!!</h1>'



@app.route("/api/customers", methods=["GET"])
def customers():
    return jsonify(Get_Customers_List()), 200



@app.route("/api/customers/<string:id>", methods=["GET"])
def clist():
    return jsonify(Get_Customer(id)), 200

#########################################################################
# Ejecutar la aplicación de Flask en el servidor web integrado
#########################################################################
app.run()