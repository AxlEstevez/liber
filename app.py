#!/usr/bin/python3
#-*- coding: utf-8 -*-
# Autor: Axl Estevez, axlestevez@hotmail.com

from flask import Flask, render_template, redirect, request
from flaskext.mysql import MySQL
from modulos.conexion import Connection

conexion = Connection("root","","127.0.0.1","Biblioteca")

try:
    conexion.createConnection()
    print("Conexión establecida")
except Exception as e:
    print("Error no se ha conectado con la base de datos")

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')


if __name__ == "__main__":
    app.run(port=8000,debug=True)