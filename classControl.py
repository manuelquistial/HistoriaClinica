#!/usr/bin/env python
# -*- coding: utf-8 -*-

from classLipidos import Lipidos

class Control(Lipidos):

	peso = 0
	altura = 0
	cadera = 0
	cuello = 0
	cintura = 0

	def __init__(self):
		return 

	def setPeso(self, attr):
		Control.peso = attr

	def getPeso(self):
		return Control.peso

	def setAltura(self, attr):
		Control.altura= attr

	def getAltura(self):
		return Control.altura

	def setCadera(self, attr):
		Control.cadera = attr

	def getCadera(self):
		return Control.cadera

	def setCuello(self, attr):
		Control.cuello = attr

	def getCuello(self):
		return Control.cuello

	def setCintura(self, attr):
		Control.cintura = attr

	def getCintura(self):
		return Control.cintura