from flask import Flask, render_template, request, redirect, url_for,Response, jsonify
from flask_sqlalchemy import SQLAlchemy
import sqlite3
import os
import datetime as dt
from camera import VideoCamera
import numpy as np
import matplotlib.pyplot as plt
import io
import base64


APP_PATH = os.getcwd()
BD_PATH = 'templates\database\proyecto_python.db'

con = sqlite3.connect(BD_PATH)
con.close()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///templates/database/proyecto_python.db'
db = SQLAlchemy(app)
#camera
video_camera = None
global_frame = None
estado_req=False

# database conector


class Persona(db.Model):
    id = db.Column(db.String(10), primary_key= True)
    nombre = db.Column(db.String(50))
    nacimiento = db.Column(db.DateTime)
    #cedula = db.Column(db.String(10))

class Admin(db.Model):
    id_admin = db.Column(db.Integer, primary_key= True)
    nombre = db.Column(db.String(50))
    password = db.Column(db.String(50))

# class DATA(db.Model):
#     id = db.Column(db.Integer)
#     idPersona = db.Column(db.String(10))
#     idSecion = db.Column(db.Integer)
    # enojado = db.Column(db.Numeric)
    # disgusto = db.Column(REAL)
    # miedo = db.Column(REAL)
    # feliz = db.Column(REAL)
    # triste = db.Column(REAL)
    # sorpresa = db.Column(REAL)
    # neutral = db.Column(REAL)


# createTable = "CREATE TABLE DATA(id INTEGER,idPersona varchar(10), 
# idSecion INTEGER, enojado REAL, disgusto REAL, miedo REAL, feliz REAL, triste REAL, sorpresa REAL, neutral REAL)"

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

@app.route('/create-user', methods=['GET', 'POST'])
def create():    
    global estado_req
    print(request.method)
    if request.method == 'POST':
        if request.form.get('Iniciar') == 'Iniciar':
            # pass
            print("Iniciar")
            estado_req = True
        elif  request.form.get('Detener') == 'Detener':
            # pass # do something else
            print("Detener")
            
            estado_req = False
        else:
            # pass # unknown
            nacimiento= request.form['edad']
            tokens = nacimiento.split("-")
            print(tokens)
            fecha = dt.date(int(tokens[0]),int(tokens[1]),int(tokens[2]))
            usuario = Persona(nombre=request.form['nombre'],id=(request.form['cedula']),nacimiento= fecha)
            db.session.add(usuario)
            db.session.commit()
            
    elif request.method == 'GET':
            
        print("No Post Back Call")
    ###### aqui necesitotraer los datos de la base de datos y comparalos, para ello pienso crear una clase y ahi crear el metodo de comparacion para llamarlo en esta
    ###### al metodo es ingresar por parametro el nombre y la sentencia y que me retorne si existen coincidencias con las claves primarias para imprimir un error
    ###### otro metodo puede ser parar verificar los usuarios y contrasenias para lafuncion de abajo
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



def video_stream():
    global video_camera
    global global_frame
    global estado_req
    connectionObject = sqlite3.connect("templates/database/proyecto_python.db")
    cursorObject = connectionObject.cursor()
    contador=0
    secion = "5"
    persona = "1717171717"
    if estado_req:
        video_camera = VideoCamera()
        
    while estado_req:
        frame = video_camera.get_frame()
        datos=video_camera.datos
        
        if(sum(datos)>=10):        
            normalizados = [float(i)/sum(datos) for i in datos]
            insertValues = "INSERT INTO DATA values("+str(contador)+","+persona+","+secion+","+str(normalizados[0])+","+str(normalizados[1])+","+str(normalizados[2])+","+str(normalizados[3])+","+str(normalizados[4])+","+str(normalizados[5])+","+str(normalizados[6])+")"
            cursorObject.execute(insertValues)
            connectionObject.commit()
            print(normalizados)
            contador = contador + 1
            video_camera.datos = [0,0,0,0,0,0,0]           
        
        if frame != None:
            global_frame = frame
            yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
        else:
            yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + global_frame + b'\r\n\r\n')       
    video_camera = None
    yield (b'--frame\r\n'
        b'Content-Type: image/jpeg\r\n\r\n' + global_frame + b'\r\n\r\n')
    connectionObject.close()
    # cursorObject.close()


@app.route('/video_viewer')
def video_viewer():
    return Response(video_stream(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/graficos')
def graficos():
    return render_template('graficos.html')

# plot 
@app.route('/build_plot')
def build_plot():
    connectionObject = sqlite3.connect("templates/database/proyecto_python.db")
    cursorObject = connectionObject.cursor()
    queryTable = "SELECT * from DATA"
    queryResults = cursorObject.execute(queryTable)
    print("Datos registrados:")
    data = []
    for result in queryResults:
        data.append(result[3:])      

    x=np.array(data)
    y=np.transpose(x)
    
    x = range(len(x))

    fig, a = plt.subplots(7, sharex=True, sharey=True, gridspec_kw={'hspace': 0})
    connectionObject.close()
    fig.suptitle('Emociones')
    
    a[0].plot(x, y[0])
    a[0].text(-6, .5, 'Enojado')
    
    a[1].plot(x, y[1], 'tab:orange')
    a[1].text(-6, .5, 'Disgusto')
    
    a[2].plot(x, y[2], 'tab:green')
    a[2].text(-6, .5, 'Miedo')
    
    a[3].plot(x, y[3], 'tab:red')
    a[3].text(-6, .5, 'Feliz')
    
    a[4].plot(x, y[4], 'tab:blue')
    a[4].text(-6, .5, 'Triste')
    
    a[5].plot(x, y[5], 'tab:green')
    a[5].text(-6, .5, 'Sorpresa')
    
    a[6].plot(x, y[6],  'tab:orange')
    a[6].text(-6, .5, 'Neutral')
    # plt.axis([0, 160, 0, 1])
    # descargar
    # plt.savefig('grafica_lineal.png')
    plt.rcParams["figure.figsize"] = (20,3)
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    return img.getvalue()

if __name__ == '__main__':
    app.run(debug=True)