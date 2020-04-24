#!/usr/bin/python3
#-*- coding: utf-8 -*-

import pymysql

class Connection(object):
    """Clase Connection.
        
        Permite generar una conexión a una base de datos
        MySQL usando el modulo de pyMySQL
        
        Atributos:
        __user - usuario que se conectara a la BD.
        __pass - contraseña del usuario
        __host - dirección ip de donde se encuentra la BD.
        __db - Nombre de la base de datos
        __cursor - Objeto para interactuar con la BD.
    """
    # -----------------------------------------------------
    # Atributos del objeto Connexión
    # -----------------------------------------------------
    __user = ""
    __pass = ""
    __host = ""
    __db = ""
    __cursor = None
    # -----------------------------------------------------

    # -----------------------------------------------------
    # Constructores
    # -----------------------------------------------------

    # Constructor default
    def __init__(self):
        pass
    
    # Constructor completo
    def __init__(self,user,password,host,db):
        self.__user = user
        self.__pass = password
        self.__host = host
        self.__db = db
    # -----------------------------------------------------

    # -----------------------------------------------------
    # Métodos
    # -----------------------------------------------------
    def createConnection(self):
        conexion = pymysql.connect(
            host = self.__host,
            user = self.__user,
            password = self.__pass,
            db = self.__db
        )
        self.__cursor = conexion.cursor()
        return conexion
    
    def damePass(self,user):
        sql = 'SELECT password FROM Usuarios where usuario = \'{}\''.format(user)

        try:
            self.__cursor.execute(sql)
            password = self.__cursor.fetchone()

            print("Pass: ",password)
        except Exception as e:
            raise
