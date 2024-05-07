from flask import Flask, render_template, render_template_string
##Creamos una instancia de flask

app = Flask(__name__)



##Rutas de la aplicación Flask
#http://localhost:5000/
@app.route("/")
def index():
    return f'<h1 style="color: blue;">Taki Taki!</h1>'

#http://localhost:5000/rumba/
@app.route("/rumba/")
def saludo():
    return f'<h1 style="color: blue;">Taki Taki Rumba!</h1>'

#http://localhost:5000/template/<nombre>
@app.route("/template/<nombre>/")
def indexdos():
    return render_template("demotemplate.html, nombreEnPlantilla=nombre")


# Ejecutar la aplicación de flask en el servidor web integrado
app.run()