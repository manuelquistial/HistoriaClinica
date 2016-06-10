#!/usr/bin/env python
# -*- coding: utf-8 -*-

def validarN(x): #definimos "validar" como función
    flag=True #Le damos valor "verdadero" a la variable booleana flag
    while flag: #Ciclo while que corre mientras la variable flag sea "verdadera"
        dato=(raw_input(x)) #Función de python para garantizar la entrada de un numero entero
        try: #Se hace el llamado al bloque "try" que puede lanzar una excepción
                dato= float(dato)
                if dato>0:
                    flag=False
                else:
                    print('Error, el dato ingresado no es válido, ingrese un valor correcto')#Se le informa al usuario que ingreso un numero erróneo
        except ValueError: #Se ejecuta el bloque except cuando la función es llamada con un valor de tipo correcto pero valor incorrecto.
            print('Error, el dato ingresado no es válido, ingrese un valor correcto') #Se le informa al usuario que ingreso un número erróneo
    return(dato)

def validarS(x):
    c=True
    while c:
        p=(raw_input(x))
        try:
            p= int(p) 
            print('Error, ingrese string')          
        except ValueError:
            c=False
    return p

def regresar(): #Función para validar regreso 
    x = '\n¿Sus datos estan correctos?\n 1.SI \n 2.NO: '
    cami=True
    while cami:
        dato=(raw_input(x))
        try:
            dato=int(dato)
            if dato!=1 and dato!=2:
                print('Error, ingrese un dato correcto ')
            else:
                cami=False
        except ValueError:
            print('Eroor, ingrese un dato correcto ')
    return(dato)

def nuevoU():
    op = '\n¿Desea ingresar otro paciente? \n1.SI\n2.NO: '
    d = True
    while d:
        v = (raw_input(op))
        try:
            dato=int(v)
            if dato!=1 and dato!=2:
                print('Error, ingrese un dato correcto ')
            else:
                d=False
        except ValueError:
            print('Eroor, ingrese un dato correcto ')
    return(dato)