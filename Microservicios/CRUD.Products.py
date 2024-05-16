from flask import Flask, render_template, render_template_string

#########################################################################
# Creamos una instancia de Flask
#########################################################################
app = Flask(__name__, template_folder="templates")


#########################################################################
# Rutas de la aplicación Flask
#########################################################################

# Retorna una lista de productos
# Ruta: http://dominio.com/api/products
@app.route("/api/products", methods=["GET"])
def products_get():
    return jsonify(), 200


# Retorna los datos del producto 34
# Ruta http://dominio.com/api/products/34
@app.route("/api/products/<int:id>", methods=["GET"])
def product34_get(id):
    return jsonify(), 200



#########################################################################
# Ejecutar la aplicación de Flask en el servidor web integrado
#########################################################################
app.run()