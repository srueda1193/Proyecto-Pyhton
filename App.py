from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import sqlite3
import os
import datetime as dt

APP_PATH = os.getcwd()
BD_PATH = 'templates\database\proyecto_python.db'

con = sqlite3.connect(BD_PATH)
con.close()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///templates/database/proyecto_python.db'
db = SQLAlchemy(app)



class Persona(db.Model):
    id = db.Column(db.String(10), primary_key= True)
    nombre = db.Column(db.String(50))
    nacimiento = db.Column(db.DateTime)
    #cedula = db.Column(db.String(10))

class Admin(db.Model):
    id_admin = db.Column(db.Integer, primary_key= True)
    nombre = db.Column(db.String(50))
    password = db.Column(db.String(50))

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

@app.route('/lista-usuarios', methods=['POST'])
def mostrar_lista_usuarios():
    personas = Persona.query.all()
    return render_template('lista-usuarios.html', personas = personas)

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
    ###### aqui necesitotraer los datos de la base de datos y comparalos, para ello pienso crear una clase y ahi crear el metodo de comparacion para llamarlo en esta
    ###### al metodo es ingresar por parametro el nombre y la sentencia y que me retorne si existen coincidencias con las claves primarias para imprimir un error
    ###### otro metodo puede ser parar verificar los usuarios y contrasenias para lafuncion de abajo
    nacimiento= request.form['edad']
    tokens = nacimiento.split("-")
    print(tokens)
    fecha = dt.date(int(tokens[0]),int(tokens[1]),int(tokens[2]))
    usuario = Persona(nombre=request.form['nombre'],id=(request.form['cedula']),nacimiento= fecha)
    db.session.add(usuario)
    db.session.commit()
    return render_template('detector-emociones.html')

@app.route('/create-admin', methods=['POST'])
def create_admin():
    nombre=request.form['nombre']
    password= request.form['password']
    ############ aca debo hacer una consulta para que me traiga los nombres y los passwords para compararlos y permitir el ingreso
    if((nombre == 'sebas' and password=='sebas') or (nombre == 'patrick' and password == 'patrick')):
        admin = Admin(nombre=request.form['nombre'],password= request.form['password'])
        db.session.commit()
        return render_template('lista-usuarios.html')
    else:
        return 'error al ingresar'
    
@app.route('/tabla-usuarios', methods=['POST'])
def escribir_table():
    persona = db.Query(Persona)
    return persona

@app.route('/admin-estadisticas')
def admin_estadisticas():
    return render_template('admin-estadisticas.html')

if __name__ == '__main__':
    app.run(debug=True)