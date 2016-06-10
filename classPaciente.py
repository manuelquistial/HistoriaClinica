#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Paciente():

	nombres = ''
	apellidos = ''
	identificacion = 0
	edad = 0
	sexo = ''
	eps = ''

	def __init__(self):
		return 

	def setNombres(self, attr):
		Paciente.nombres = attr

	def getNombres(self):
		return Paciente.nombres

	def setApellidos(self, attr):
		Paciente.apellidos = attr

	def getApellidos(self):
		return Paciente.apellidos

	def setIdentificacion(self, attr):
		Paciente.identificacion = attr

	def getIdentificacion(self):
		return Paciente.identificacion

	def setEdad(self, attr):
		Paciente.edad = attr

	def getEdad(self,):
		return Paciente.edad
		
	def setSexo(self, attr):
		Paciente.sexo = attr

	def getSexo(self):
		return Paciente.sexo

	def setEps(self, attr):
		Paciente.eps = attr

	def getEps(self):
		return Paciente.eps


