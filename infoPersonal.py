#!/usr/bin/env python
# -*- coding: utf-8 -*-

from validar import validarS, validarN, regresar
from classControl import Control

def codigoHistorial(ep, j):    

    if (ep.lower() == "sisben"):
        hce='HCE-EPS-S-00'+str(j+1)
    else:
        hce='HCE-EPS-00'+str(j+1)
    return hce

def datosPersonales():
    
    print('\nHistoria Clinica\n')

    nom = 'Ingrese nombres: ' 
    nom = validarS(nom)
    ape = 'Ingrese apellidos: '
    ape = validarS(ape)
    cc = 'Ingrese su documento de identidad: '
    cc = validarN(cc)
    edad = 'Ingrese su edad: '
    edad = validarN(edad)
    sexV = 'Ingrese su sexo, presione \n 1. Masculino\n 2. Femenino: '
    sexV = validarN(sexV)
    if(sexV == 1):
        sexo = "hombre"
    else:
        sexo = "mujer"

    ep = 'Ingrese la EPS: '
    ep = validarS(ep)

    op = regresar()

    if(op == 1):

        infoP = Control();

        infoP.setNombres(nom)
        infoP.setApellidos(ape)
        infoP.setIdentificacion(cc)
        infoP.setEdad(edad)
        infoP.setSexo(sexo)
        infoP.setEps(ep)

        return infoP
        
    else:

        return 0
        
    
    
   
       

