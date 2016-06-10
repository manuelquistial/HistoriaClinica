#!/usr/bin/env python
# -*- coding: utf-8 -*-

import MySQLdb

def iniciardb():
	server = 'localhost'
	user = 'HistoriaClinica'
	password = '1234'
	db = 'HistoriaClinica'

	try:
		conn = MySQLdb.connect(server, user, password, db)
		return conn
	except mysql.connector.Error as err:
	  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
	    print("Something is wrong with your user name or password")
	  elif err.errno == errorcode.ER_BAD_DB_ERROR:
	    print("Database does not exist")
	  else:
	    print(err)
	else:
	  conn.close()

def ingresarData(cursor, conn, codH, name, lName, cc, edad, sexo, eps, hdl, ldl, tria, colto, vld, peso, alt, cin, cade, cue):
	dataInput = "INSERT INTO pacientes(codigohistoriaclinica, nombres, apellidos, identificacion, edad, sexo, eps, HDL, LDL, TRIA, COLTO, VLD, peso, altura, cintura, cadera, cuello) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
	cursor.execute(dataInput,(codH, name, lName, cc, edad, sexo, eps, hdl, ldl, tria, colto, vld, peso, alt, cin, cade, cue))
	conn.commit()
	conn.close()
	cursor.close()