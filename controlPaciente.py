#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Integrantes:
#Juanita Fonnegra Villegas CC.1017225586
#Juan Camilo Mesa Agudelo CC. 1035832696
#Robinson Damian Pineda Arroyave CC 1044506276
#Julieth Quinchia Pineda CC. 114407458

from math import * #Importamos el módulo "math"
from classControl import Control
from validar import validarN, regresar

def control(control):

    print('\nSigua las instrucciones correctamente\n') #Se le da la bienvenida al usuario

    x = 'Ingrese su peso en Kg: ' #En las variables x,y,z,f,h se ingresa la altura, medidas de cadera, cintura y cuello
    x = validarN(x)
    y = 'Ingrese su altura en metros: '
    y = validarN(y)

    if(control.getSexo() == "mujer"):
        z = 'Ingrese la medida de la cadera en cm: '
        z = validarN(z)
    elif(control.getSexo() == "hombre"):
        z = 0

    f = 'Ingrese la medida del cuello en cm: '
    f = validarN(f)
    h = 'Ingrese la medida de la cintura en cm: '
    h = validarN(h)

    op = regresar()

    if op == 1:
        
        control.setPeso(x)
        control.setAltura(y)
        control.setCadera(z)
        control.setCuello(f)
        control.setCintura(h)

        return control

    else:

        return 0


def mujer(pesom, alturam, cinturam, cadera, cuellom):

    imcm=(float((pesom))/float((alturam**2)))#Fórmula para calcular el IMC
    cinaltm=(float(cinturam))/(float(alturam*100))#Fórmula para calcular el índice cintura altura
    grasam=((float(495))/float(1.29579-(0.35004*(log10(cinturam+cadera-cuellom)))+(0.22100*(log10(alturam*100)))))-450#Fórmula para calcular el porcentaje de grasa
    masacormm=(pesom*(100-grasam))#Fórmula para calcular la masa corporal magra
    calminm=1622+(((alturam*100)-150)*13.2)+0.5#Fórmula para calcular la cantidad de calorías mínimas por día
    calmaxm=2194+(((alturam*100)-150)*19.3)+0.5#Fórmula para calcular la cantidad de calorías máxmas por día
    pesoidealmin=18.5*(alturam**2)#Usamos los rangos del IMC para calcular el peso ideal de la persona
    pesoidealmax=24.99*(alturam**2)

    if  imcm<18.5: #Se hacen los condicionales establecidos para los valores del IMC
        print('Su IMC indica que se encuentra "debajo del peso normal", y el valor es: ' + str(imcm))  #Se le informa al usuario que su peso está por debajo de lo normal
    elif imcm>=18.5 and imcm<25.0:#rango del IMC establecido para el peso normal
        print('Su IMC indica que se encuentra en el peso "normal", y el valor es: ' + str(imcm))  #Se le informa al usuario que su peso es normal
    elif imcm>=25.0 and imcm<30.0:#rango del IMC establecido para el sobre peso
        print('Su IMC indica que se encuentra en "sobre peso", y el valor es: '+ str(imcm)) #Se le informa al usuario que sufre se sobrepeso
    elif imcm>=30.0:#rango del IMC establecido para la obesidad
        print('Su IMC indica que se encuentra en "obesidad", y el valor es: ' + str(imcm))  #Se le informa al usuario sobre su obesidad
    else:
        print('Sus datos son incoherentes ') #Se le informa al usuarios que sus datos no tienen sentido

    if imcm>=25 and cinaltm<0.5 and grasam>=14 and grasam<=24:#Excepción para una persona musculosa con la fórmula
        print('A PESAR DE QUE SU IMC ES ALTO, USTED ES PROBABLEMENTE MUSCULOSA Y NO OBESA') #Se le informa al usuario que IMC es alto, pero por su altura lo más seguro es que no sea obesa
    elif imcm>=25:#Cuando la persona no se encuentra en el peso normal se ejecuta el siguiente paso para dar información del sobre peso ó deficiencia de peso 
        pm=pesom-pesoidealmax
        print('Usted está por encima del peso ideal por: '+str(pm)+ 'Kg')
    elif imcm<18.5:
        pm=pesoidealmin-pesom
        print('Usted está por debajo del peso ideal por: '+str(pm)+ 'Kg')

    if cinaltm>=0.5:#Rangos establecidos para el índice de cintura altura
        print('Su índice cintura altura es alto e indica "adiposidad abdominal" y el valor es: ' + str(cinaltm))  #Se le informa al usuario sobre su adiposidad abdominal
        print('El cual se asocia con un riesgo elevado para las enfermedades cardiovasculares arteriosclerósicas  ') #Se le informa al usuario el riesgo de su condición
        print('Se recomienda disminuir el porcentaje de grasa abdominal')
    elif cinaltm<0.5:
        print( 'Su valor de índice cintura altura es normal y el valor es: ' + str(cinaltm)) #Se le muestra al usuario el valor del índice cintura/altura y que es normal

    if grasam>=10 and grasam <=12:#Rangos establecidos para el porcentaje de grasa esencial
        print('Su valor de porcentaje de grasa se considera "grasa esencial" y el valor es: ' +str(grasam)) #Se le informa al usuario que su porcentaje de grasa es esencial 
    elif grasam>=14 and grasam<=20:#rango de porcentaje de grasa establecido para un atleta
        print('Su valor de porcentaje de grasa se considera "atleta" y el valor es: ' +str(grasam))  #Se le informa al usuario que su porcentaje de grasa es atleta
    elif grasam>=21 and grasam<=24:#rango de porcentaje de grasa establecido para 'fitness'
        print('Su valor de porcentaje de grasa se considera "fitness" y el valor es: '+str(grasam))  #Se le informa al usuario que su porcentaje de grasa es considerada fitness
    elif grasam>=25 and grasam<=31:#rango de porcentaje de grasa establecido 'aceptable'
        print('Su valor de porcentaje de grasa se considera "aceptable" y el valor es: '+str(grasam)) #Su porcentaje de grasa es normal
    elif grasam>=32:#rango de porcentaje de grasa establecido para una persona 'obesa'
        print('Su valor de porcentaje de grasa se considera "obesidad" y el valor es: '+str(grasam))  #Se le informa al usuario que su porcentaje de grasa ya es considerada obesidad
    else:
        print('Su valor de porcentaje de grasa no está contemplado en la literatura y el valor es: '+str(grasam)) #No se le puede informar al usuario su porcentaje de grasa

    print('Su valor de masa corporal magra es : '+str(masacormm)) #Se le informa al usuario su valor de masa corporal
    print('La cantidad de calorías mínimas a consumir por día es: '+str(calminm))#Se le informa al usuario las calorías mínimas a consumir por día
    print('La cantidad de calorías máximas a consumir por día es: '+str(calmaxm)) #Se le informa al usuario las calorías máximas a consumir por día  

    if pesom>=pesoidealmin and pesom<=pesoidealmax: #Validamos que se encuentre en el peso ideal para poder darle la cantidad de proteína a consumir diariamente
        while True:
            cte=raw_input('Ingrese de acuerdo a su nivel de actividad :\n 1.Si es sedentario\n 2.Si es moderado \n 3.Si es activo ' )
            try: #Se hace el llamado al bloque "try" que puede lanzar una excepción
                cte = int(cte)        
            except ValueError: #Se ejecuta el bloque except cuando la función es llamada con un valor de tipo correcto pero valor incorrecto.
                print('Error, ingrese 1,2 ó 3 ') #Se le informa al usuario que ingreso un numero erróneo
            if cte!= 1 and cte!=2 and cte!=3 and type(cte)==int:
                print('Error, ingrese 1,2 ó 3 ') #Se le informa al usuario que ingreso un numero erróneo
            else:
                
                if cte==1:#Se usa las condiciones para establecer el valor de la constante 
                    prote=pesom*(0.8)
                    print('La cantidad de proteína a consumir diariamente es: '+str(prote)+' gramos') #Dependiendo del valor de la variable "cte" se le informa al usuario la cantidad de proteína a consumir diariamente
                    a=False#Finalizamos el ciclo para que no retorne más
                    c=False#Finalizamos el ciclo para que no retorne más
                    break
                elif cte==2:
                    prote=pesom*(1.1)
                    print('La cantidad de proteína a consumir diariamente es: '+str(prote)+' gramos')
                    a=False#Finalizamos el ciclo para que no retorne más
                    c=False#Finalizamos el ciclo para que no retorne más
                    break
                elif cte==3:
                    prote=pesom*(1.4)
                    print('La cantidad de proteína a consumir diariamente es: '+str(prote)+' gramos')
                    a=False #Finalizamos el ciclo para que no retorne más
                    c=False #Finalizamos el ciclo para que no retorne más
                    break
    else:
        print('La cantidad de proteína a consumir diariamente en su dieta no está definida en la literatura ') #No se le puede informar al usuario la cantidad de proteína a consumir diariamente
        print('Consulte con el especialista para mayor información') #Recomendación al usuario
         
        
def hombre(pesoh, cinturah, alturah, cuelloh):

    imch=(float((pesoh))/float((alturah**2)))#Fórmula para calcular el IMC
    cinalth=(float(cinturah))/(float(alturah*100))#Fórmula para calcular el indice cintura altura
    imch=(float((pesoh))/float((alturah**2)))
    grasah=((float(495))/(float(1.0324-(0.19077*log10(cinturah-cuelloh))+(0.15456*log10(alturah*100)))))-450#Fórmula para calcular el porcentaje de grasa
    masacormh=(pesoh*(100-grasah))#Fórmula para calcular la masa corporal magra
    calminh=1842+(((alturah*100)-150)*15.4)+0.5#Fórmula para calcular la cantidad de calorías mínimas por día
    calmaxh=2488+(((alturah*100)-150)*23.6)+0.5#Fórmula para calcular la cantidad de calorías máxmas por día
    pesoidealmin=18.5*(alturah**2)#Rangos para evaluar el peso ideal de una persona
    pesoidealmax=24.99*(alturah**2)

    if imch<18.5: #Se hacen los condicionales establecidas para los valores del IMC
        print('Su IMC indica que se encuentra "debajo del peso normal", y el valor es: ' + str(imch))  #Se le informa al usuario que su peso está por debajo de lo normal
    elif imch>=18.5 and imch<25.0:#rango del IMC establecido para el peso normal
        print('Su IMC indica que se encuentra en el peso "normal", y el valor es: ' + str(imch))  #Se le informa al usuario que su peso es normal
    elif imch>=25.0 and imch<30.0:#rango del IMC establecido para el sobre peso
        print('Su IMC indica que se encuentra en "sobre peso", y el valor es: '+ str(imch)) #Se le informa al usuario que sufre se sobrepeso
    elif imch>=30:#rango del IMC establecido para la obesidad
        print('Su IMC indica que se encuentra en "obesidad", y el valor es: ' + str(imch))  #Se le informa al usuario sobre su obesidad
    else:
        print('Sus datos son incoherentes ') #Se le informa al usuarios que sus datos no tienen sentido

    if imch>=25 and cinalth<0.5 and grasah>=6 and grasah<=17: #Excepción para una persona musculosa con la fórmula
        print('A PESAR DE QUE SU IMC ES ALTO, USTED ES PROBABLEMENTE MUSCULOSO Y NO OBESO') #Se le informa al usuario que IMC es alto, pero por su altura lo más seguro es que no sea obeso
    elif imch>=25:#Condición del IMC para indicar que está por encima del peso normal
        ph=pesoh-pesoidealmax
        print('Usted está por encima del peso ideal por: '+str(ph)+ 'Kg')
    elif imch<18.5:#Condición del IMC para indicar que está por debajo del peso normal
        ph=pesoidealmin-pesoh
        print('Usted está por debajo del peso ideal por: '+str(ph)+ 'Kg')

    if grasah>=2 and grasah <=4: #Se hacen las condiciones establecidas para los valores del porcentaje de grasa
        print('Su valor de porcentaje de grasa se considera "grasa esencial" y el valor es: ' +str(grasah))#Se le informa al usuario que su porcentaje de grasa ya es considerada esencial
    elif grasah>=6 and grasah<=13:#porcentaje de grasa corporal establecido para un atleta
        print('Su valor de porcentaje de grasa se considera "atleta" y el valor es: ' +str(grasah))  #Se le informa al usuario que su porcentaje de grasa es atleta
    elif grasah>=14 and grasah<=17:#porcentaje de grasa corporal establecido para una mujer 'fitness'
        print('Su valor de porcentaje de grasa se considera "fitness" y el valor es: '+str(grasah)) #Se le informa al usuario que su porcentaje de grasa es considerada fitness
    elif grasah>=18 and grasah<=25:#porcentaje de grasa corporal 'aceptable'
        print('Su valor de porcentaje de grasa se considera "aceptable" y el valor es: '+str(grasah)) #Su porcentaje de grasa es normal
    elif grasah>=26:#porcentaje de grasa corporal establecido para una persona 'obesa'
        print('Su valor de porcentaje de grasa se considera "obesidad" y el valor es: '+str(grasah)) #Se le informa al usuario que su porcentaje de grasa ya es considerada obesidad
    else:
        print('Su valor de porcentaje de grasa no está contemplado en la literatura y el valor es: '+ str(grasah)) #No se le puede informar al usuario su porcentaje de grasa

    if cinalth>=0.5: #Se hacen las condiciones establecidas para el valor del índice cintura-altura
        print('Su índice cintura altura es alto e indica "adiposidad abdominal" y el valor es: ' + str(cinalth)) #Se le informa al usuario sobre su adiposidad abdominal
        print('El cual se asocia con un riesgo elevado para las enfermedades cardiovasculares arteriosclerósicas  ')#Se le informa al usuario el riesgo de su condición
        print('Se recomienda disminuir la grasa abdominal')
    elif cinalth<0.5:
        print( 'Su valor de índice cintura altura es normal y el valor es: ' + str(cinalth)) #Se le muestra al usuario el valor del índice cintura/altura y que es normal

    print('Su valor de masa corporal magra es : '+str(masacormh)) #Se le informa al usuario su valor de masa corporal
    print('La cantidad de calorías mínimas a consumir por día es: '+str(calminh))#Se le informa al usuario las calorías mínimas a consumir por día
    print('La cantidad de calorías máximas a consumir por día es: '+str(calmaxh)) #Se le informa al usuario las calorías máximas a consumir por día 

    if pesoh>=pesoidealmin and pesoh<=pesoidealmax:
        while True: #Ciclo while que corre mientras la variable de la que depende sea "Verdadera"
            cte=raw_input('Ingrese de acuerdo a su nivel de actividad :\n 1.Si es sedentario\n 2.Si es moderado \n 3.Si es activo ' )
            try: #Se hace llamado al bloque "try" que puede lanzar una excepción
                cte = int(cte)        
            except ValueError: #Se ejecuta el bloque except cuando la función es llamada con un valor de tipo correcto pero valor incorrecto.
                print('Error, ingrese 1,2 ó 3 ') #Se le informa al usuario que ingreso un número erróneo
            if cte!= 1 and cte!=2 and cte!=3 and type(cte)==int: #Se inicia ciclo condicional
                print('Error, ingrese 1,2 ó 3 ') #Se le informa al usuario que ingreso un numero erróneo
            else:
                if cte==1: #Se inicia ciclo condicional
                    prote=pesoh*(0.8)
                    print('La cantidad de proteína a consumir diariamente es: '+str(prote)+' gramos') #Dependiendo del valor de la variable "cte" se le informa al usuario la cantidad de proteína a consumir diariamente
                    d=False#Finalizamos el ciclo para que no retorne más
                    c=False#Finalizamos el ciclo para que no retorne más
                    a=False#Finalizamos el ciclo para que no retorne más
                    break
                elif cte==2:
                    prote=pesoh*(1.1)
                    print('La cantidad de proteína a consumir diariamente es: '+str(prote)+ 'gramos ')
                    d=False#Finalizamos el ciclo para que no retorne más
                    c=False#Finalizamos el ciclo para que no retorne más
                    a=False#Finalizamos el ciclo para que no retorne más
                    break
                elif cte==3:
                    prote=pesoh*(1.4)
                    print('La cantidad de proteína a consumir diariamente es: '+str(prote)+ 'gramos ')
                    d=False#Finalizamos el ciclo para que no retorne más
                    c=False#Finalizamos el ciclo para que no retorne más
                    a=False#Finalizamos el ciclo para que no retorne más
                    break
                    
    else:
        print('La cantidad de proteína a consumir diariamente no está establecida en la literatura ')
        print('Consulte con el especialista para mayor información') #Recomendación al usuario
                        