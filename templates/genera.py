from flask import Flask, render_template, request, redirect, url_for,Response, jsonify
from flask_sqlalchemy import SQLAlchemy
import sqlite3

app2 = Flask(__name__)
app2.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///templates/database/proyecto_python.db'
db2 = SQLAlchemy(app2)



class DATA(db2.Model):
    id = db.Column(db.Integer)
    idPersona = db.Column(db.String(10))
    idSecion = db.Column(db.Integer)
    enojado = db.Column(db.Numeric)
    neutral = db.Column(db.Numeric)
    miedo = db.Column(db.Numeric)
    feliz = db.Column(db.Numeric)
    triste = db.Column(db.Numeric)
    sorpresa = db.Column(db.Numeric)