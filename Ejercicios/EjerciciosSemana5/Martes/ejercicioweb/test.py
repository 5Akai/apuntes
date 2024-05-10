from flask import Flask, render_template,render_template_string

#creamos una instancia de flask
app=Flask(__name__, template_folder="template")


#ruta de la aplicacion
@app.route("/")
def index():
    return f"<h1>hola mundo </h1>"

@app.route("/saludo/<nombre>")
def saludo(nombre):
    return f"<h1> hola {nombre} </h1>"

#ruta de templates
@app.route("/template/<nombre>")
def template(nombre):
    return render_template("demotemplate.html",nombrePlantilla=nombre)

#ejecutamos la aplicacion 
app.run()