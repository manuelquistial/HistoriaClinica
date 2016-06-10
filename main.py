#!/usr/bin/env python
# -*- coding: utf-8 -*-

import MySQLdb
from infoPersonal import *
from perfilLipidico import *
from controlPaciente import *
from validar import nuevoU
from dataBase import *

cont = 1

#personal
codH = ''
name = ''
lName = ''
cc = 0
sexo = ''
edad = 0
eps = ''

#lipidos
hdl = 0
ldl = 0
tria = 0
colto = 0
vld = 0

#control 
peso = 0
alt = 0
cin = 0
cade = 0
cue = 0

while cont == 1:
	paciente = datosPersonales()

	while paciente == 0:
		paciente = datosPersonales()

	name = paciente.getNombres()
	lName = paciente.getApellidos()
	cc = paciente.getIdentificacion()
	edad = paciente.getEdad()
	sexo = paciente.getSexo()
	eps = paciente.getEps()

	pacienteL = lipidos(paciente)

	while pacienteL == 0:
		pacienteL = lipidos(paciente)

	hdl = pacienteL.getHDL()
	ldl = pacienteL.getLDL()
	tria = pacienteL.getTRIA()
	colto = pacienteL.getCOLTO()
	vld = pacienteL.getVLD()

	print('\n')
	HDL = funHDL(hdl)
	LDL = funLDL(ldl)
	TRIA = funTRIA(tria)
	COLTO = funCOLTO(colto)
	VLD = funVLD(vld)

	if((HDL and LDL and TRIA and COLTO and VLD) == True):
		cont = nuevoU()
	else:
		pacienteC = control(pacienteL)
		while pacienteC == 0:
			pacienteC = control(pacienteL)

		peso = pacienteC.getPeso()
		alt = pacienteC.getAltura()
		cin = pacienteC.getCintura()
		cade = pacienteC.getCadera()
		cue = pacienteC.getCuello()

		print('\n')
		if(pacienteC.getSexo() == "mujer"):
			mujer(peso, alt, cin, cade, cue)
		elif(pacienteC.getSexo() == "hombre"):
			hombre(peso, cin, alt, cue)
		cont = nuevoU()

	conn = iniciardb()
	cursor = conn.cursor()

	sql = "SELECT id FROM pacientes"
	cursor.execute(sql)
	idA = cursor.fetchall()
	idV = len(idA)
	codH = codigoHistorial(eps, idV)

	if not idA:
		ingresarData(cursor, conn, codH, name, lName, cc, edad, sexo, eps, hdl, ldl, tria, colto, vld, peso, alt, cin, cade, cue)
	else:
		ingresarData(cursor, conn, codH, name, lName, cc, edad, sexo, eps, hdl, ldl, tria, colto, vld, peso, alt, cin, cade, cue)