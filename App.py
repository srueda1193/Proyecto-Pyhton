from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import sqlite3
import os

APP_PATH = os.getcwd()
BD_PATH = 'templates\database\proyecto_python.db'

con = sqlite3.connect(BD_PATH)
con.close()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///templates/database/proyecto_python.db'
db = SQLAlchemy(app)



class Persona(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    nombre = db.Column(db.String(50))
    edad = db.Column(db.Integer)
    nacimiento = db.Column(db.Date)


####Metodos para el redicreccionamiento de botones


@app.route('/')
def home():
    return render_template('index.html')

####################### redireccion del lado del Administrador del sistema

@app.route('/login-admin')
def log_admin():
    return render_template('login-admin.html')

@app.route('/menu-admin')
def menu_admin():
    return render_template('menu-admin.html')

@app.route('/admin-estadisticas')
def motrar_estadisticas_admin():
    return render_template('admin-estadisticas.html')

@app.route('/lista-usuarios')
def mostrar_lista_usuarios():
    return render_template('lista-usuarios.html')

###################### redireccion del lado de los usuarios del sistema

@app.route('/login-usuario')
def log_usuario():
    return render_template('login-usuario.html')

@app.route('/detector-emociones')
def dectectar_emociones():
    return render_template('detector-emociones.html')

@app.route('/estadisticas-tr')
def resultados_tiempo_real():
    return render_template('estadisticas-tr.html')

@app.route('/estadisticas-finales')
def resultado_final():
    return render_template('estadisticas-finales.html')


###############metodos para traer datos o cargarlo en el sql y el servidor

@app.route('/create-user', methods=['POST'])
def create():
    request.form

@app.route('/admin-estadisticas')
def admin_estadisticas():
    return render_template('admin-estadisticas.html')

if __name__ == '__main__':
    app.run(debug=True)

