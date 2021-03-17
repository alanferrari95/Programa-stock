from tkinter import ttk
import tkinter as tk
import sqlite3
from tkinter import *
from tkinter import messagebox



class Ver_Proveedores():

	def __init__(self):

		try: 	
			conexion=sqlite3.connect("MiNegocio")
			cursor=conexion.cursor()
			cursor.execute("CREATE TABLE PROVEEDORES (CUIT INTEGER PRIMARY KEY, RAZON VARCHAR(50))")
			conexion.commit()

		except:
			sqlite3.OperationalError



	def act_bbdd(self):
		self.db = sqlite3.connect("MiNegocio")
		self.cursor = self.db.cursor()
		self.cursor.execute("SELECT * FROM PROVEEDORES")
		actualizar_bbdd=self.cursor.fetchall()
		self.db.commit()
		return actualizar_bbdd
		
		#self.db.close()
		
	def seleccionar(self):


		item = self.tree.selection()
		item2= self.tree.set(item, "#1")
		item3= self.tree.set(item, "#2")
		dni.set(item2)
		nombre.set(item3)
		self.lista.destroy()




	def nuevo_aceptar(self, cuit, razon_social):
		datos=(cuit, razon_social)
		self.db = sqlite3.connect("MiNegocio")
		self.cursor = self.db.cursor()		
		self.cursor.execute("INSERT INTO PROVEEDORES VALUES (?,?)", datos)
		self.db.commit()
		self.act_bbdd()
		print(datos)
		




	




