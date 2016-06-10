#!/usr/bin/env python
# -*- coding: utf-8 -*-

from validar import validarN
from validar import regresar

def lipidos(lipido):

    hdl = "\nIngrese parámetro de HDL-COLESTEROL en mg/ld: "
    hdl = validarN(hdl)
    ldl = "Ingrese parámetro de LDL-COLESTEROL en mg/ld: "
    ldl = validarN(ldl)
    tria = "Ingrese parámetro de TRIGLICÉRIDOS en mg/ld: "
    tria = validarN(tria)
    colto = "Ingrese parámetro de COLESTEROL TOTAL: "
    colto = validarN(colto)
    vld = "Ingrese parámetro de VLDL-COLESTEROL: "
    vld = validarN(vld)

    op = regresar()

    if op == 1:

        lipido.setHDL(hdl)
        lipido.setLDL(ldl)
        lipido.setTRIA(tria)
        lipido.setCOLTO(colto)
        lipido.setVLD(vld)

        return lipido
 
    else:

        return 0

def funHDL(hdl):
    ver = False

    if hdl<40:
        print("Su colesterol HDL es bajo y constituye un factor de riesgo coronario de la enfermedad cardiaca")
        print("Su rango normal debería estar entre 40-60 mg/ld")
    elif hdl>60:
        print("Su colesterol HDL  es mayor que 60 mg/dl  es un factor de protección para la enfermedad cardiaca coronaria")#Se muestra mensaje de situacion de salud 
        print("Su rango normal debería estar entre 40-60 mg/ld") # Se le informa al usuario en que rango deberian estar los parámetros ingresados
    elif hdl>=40 and hdl<=60: #ESTE ES EL RANGO NORMAL 
        print("Su resultado es óptimo; se encuentra en el rango normal; el cual corresponde entre 40-60 mg/dl")#Se muestra mensaje de situacion de salud normal
        ver = True

    return ver

def funLDL(ldl):
    ver = False

    if ldl<100:
        print("Su valor de colesterol ldl está en el rango normal") #Se muestra mensaje de situación de salud normal
        print("El colesterol LDL es normal cuando es menor a 100 mg/ld")# Se le informa al usuario en que rango deberian estar los parámetros ingresados
        ver = True
    elif ldl>=100 and ldl<=129:
        print("Su valor de LDL-COLESTEROL está sobre el limite de lo normal; aunque se puede considerar como adecuado")# Se muestra mensaje de situacion de salud normal
        print("El rango normal se logra cuando el LDL-COLESTEROL es menor a 100mg/ld")# Se le informa al usuario en que rango deberian estar los parámetros ingresados
    elif ldl >=130 and ldl<=189:
        print("RIESGO! Su valor de LDL-COLESTEROL  es alto; consultar inmediatamente ")#Recomendaciones de diagnostico
        print("El rango normal se logra cuando el LDL-COLESTEROL es menor a 100mg/ld")# Se le informa al usuario en que rango deberian estar los parámetros ingresados
    elif ldl>=190:
        print("RIESGO! su valor de LDL-COLESTEROL indica una hipercolesterolemía ")#Recomendaciones de diagnostico
        print("El rango normal se logra cuando el LDL-COLESTEROL es menor a 100mg/ld")#Se le informa al usuario en que rango deberian estar los parámetros ingresados
    
    return ver

def funTRIA(tria):
    ver = False

    if tria<150:
        print("Su valor de TRIGLICÉRIDOS se encuentran en el rango normal")# Se muestra mensaje de situacion de salud normal
        print("El rango normal de TRIGLICÉRIDOS es menor a 150 mg/ld")#Se le informa al usuario en que rango deberian estar los parámetros ingresados
        ver = True
    elif tria>=150 and tria<=199:
        print("Su valor de TRIGLICÉRIDOS está sobre el limite de lo normal; aunque se puede considerar como adecuado")#Se muestra mensaje de situacion de salud normal
        print("El rango normal de TRIGLICÉRIDOS es menor a 150 mg/ld")#Se le informa al usuario en que rango deberian estar los parámetros ingresados
    elif tria>=200 and tria<499:
        print("ALERTA! Su valor de TRIGLICÉRIDOS es de alto riesgo coronario ")#Recomendaciones de diagnóstico
        print("El rango normal de TRIGLICÉRIDOS es menor a 150 mg/ld")
    elif tria>500:
        print("URGENTE! Su valor de TRIGLICÉRIDOS es muy alto")#Recomendaciones de diagnóstico
        print("El rango normal de TRIGLICÉRIDOS es menor a 150 mg/ld")

    return ver

def funCOLTO(colto):
    ver = False

    if colto<=200:
        print("Su valor de COLESTEROL TOTAL es normal")#Se muestra mensaje de situacion de salud normal
        print("El rango normal de COLESTEROL TOTAL es menor ó igual a 200mg/ld")
        ver = True
    elif colto>200 and colto<=240:
        print("ATENCIÓN! Su valor de COLESTETOL TOTAL es alto ");#Recomendaciones de diagnóstico
        print("El rango normal de COLESTEROL TOTAL es menor ó igual a 200mg/ld")
    elif colto>240:
        print("URGENTE! Su valor de COLESTEROL TOTAL es muy alto ")#Recomendaciones de diagnóstico
        print ("El rango normal de COLESTEROL TOTAL es menor ó igual a 200mg/ld")
    
    return ver
        
def funVLD(vld):
    ver = False

    if vld>=2 and vld<=30:
        print("Su valor de COLESTEROL VLDL es normal")#Se muestra mensaje de situacion de salud normal
        print("El rango normal de COLESTEROL VLDL es entre 2-30mg/ld")
        ver = True
    elif vld>0 and vld<2:
        print ("Su valor de COLESTEROL VLDL no está contemplado en la literatura ")
        print("El rango normal de COLESTEROL VLDL es entre 2-30mg/ld") 
    elif vld>30:
        print("ATENCIÓN!Su valor de COLESTETOL VLDL es alto")#Recomendaciones de diagnóstico
        print("El rango normal de COLESTEROL VLDL es entre 2-30mg/ld")

    return ver
               
                
            

