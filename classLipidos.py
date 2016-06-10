#!/usr/bin/env python
# -*- coding: utf-8 -*-

from classPaciente import Paciente  

class Lipidos(Paciente):

	HDL = 0
	LDL = 0
	TRIA = 0
	COLTO = 0
	VLD = 0

	def __init__(self):
		return 

	def setHDL(self, attr):
		Lipidos.HDL = attr

	def getHDL(self):
		return Lipidos.HDL

	def setLDL(self, attr):
		Lipidos.LDL = attr

	def getLDL(self):
		return Lipidos.LDL

	def setTRIA(self, attr):
		Lipidos.TRIA = attr

	def getTRIA(self):
		return Lipidos.TRIA

	def setCOLTO(self, attr):
		Lipidos.COLTO = attr

	def getCOLTO(self):
		return Lipidos.COLTO

	def setVLD(self, attr):
		Lipidos.VLD = attr

	def getVLD(self):
		return Lipidos.VLD