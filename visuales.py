import sqlite3
from compras import Clase_Compras
from ventas import Clase_Ventas
from proveedores import Ver_Proveedores
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk

#PESTAÑA PRINCIPAL
root=Tk()
root.title("Programa de stock")
root.resizable(width=False, height=False)
frame1=Frame(root)
frame1.pack()


#----------------------------FUNCIONES BARRA DE HERRAMIENTAS
#---------------ARCHIVO
def salir_app():
	end=messagebox.askokcancel("Salir", "¿Deseas salir de la aplicación?")

	if end==True:
		root.destroy()

#---------------HERRAMIENTAS



#---------------AYUDA
def acerca_de():
	messagebox.showinfo(message="Gracias por ejecutar este programa!\n\n\nEmail: alanferrari95@hotmail.com\nLinkedin: /alanferrari95\nGithub: /alanferrari95")




#---------------BARRA DE HERRAMIENTAS
barramenu=Menu(root)
root.config(menu=barramenu)

archivomenu=Menu(barramenu, tearoff=0)
archivomenu.add_command(label="Salir", command=salir_app)
barramenu.add_cascade(label="Archivo", menu=archivomenu)

herramientasmenu=Menu(barramenu, tearoff=0)
barramenu.add_cascade(label="Herramientas", menu=herramientasmenu) 

exp_submenu=Menu(barramenu, tearoff=0)
exp_submenu.add_command(label="Ventas")
exp_submenu.add_command(label="Compras")
exp_submenu.add_command(label="Stock")

ver_submenu=Menu(barramenu, tearoff=0)
ver_submenu.add_command(label="Ventas")
ver_submenu.add_command(label="Compras")

editar_submenu=Menu(barramenu, tearoff=0)
editar_submenu.add_command(label="Ventas")
editar_submenu.add_command(label="Compras")

herramientasmenu.add_cascade(label="Exportar", menu=exp_submenu)
herramientasmenu.add_cascade(label="Ver", menu=ver_submenu)
herramientasmenu.add_cascade(label="Editar", menu=editar_submenu)


ayudamenu=Menu(barramenu, tearoff=0)
ayudamenu.add_command(label="Acerca de", command=acerca_de)
barramenu.add_cascade(label="Ayuda", menu=ayudamenu)

#----------------------------VISUAL

class visuales():


	def __init__(self):
		self.tipo=""
		self.cuitpantalla2=""
		self.razonpantalla2=""
		self.prodpantalla2=""
		self.cantpantalla2=""

	def cerrar():
		frame2.destroy()
	
	def mostrar_proveedores(self):	
		
		list_act=Ver_Proveedores()
		lista_actualizada=list_act.act_bbdd()
		print(lista_actualizada)
		x=self.tree.get_children()
		for item in x:
			self.tree.delete(item)

		for row in lista_actualizada:

			self.tree.insert("",tk.END, values=(row[0], row[1]))

	def nuevo_proveedor_aceptar(self):
		try:

			if 	len(self.dni_nuevo.get())==8 and self.nombre_nuevo.get().replace(" ","").isalpha() and len(self.nombre_nuevo.get())<20:
				
				cuit=(self.cuit_num1.get()+self.dni_nuevo.get()+self.cuit_num2.get())
				razon_social=(self.nombre_nuevo.get())
				print(cuit, razon_social)
				nuevo_proveedor_confirmar=Ver_Proveedores()
				nuevo_proveedor_confirmar.nuevo_aceptar(cuit, razon_social)
				self.mostrar_proveedores()
				self.reg_nuevo.destroy()
			else:
				self.error_datos()

		except:

			sqlite3.IntegrityError
			self.error_datos()

	def limitador(self, dni_nuevo): #limitar a 11 la cantidad de numeros de CUIT.
		if len(self.dni_nuevo.get()) > 0:

			self.dni_nuevo.set(self.dni_nuevo.get()[:8])	

	def seleccionar_proveedor(self):

		item = self.tree.selection()
		item2= self.tree.set(item, "#1")
		item3= self.tree.set(item, "#2")
		self.cuitpantalla.set(item2)
		self.razonpantalla.set(item3)
		self.lista.destroy()	

	def nuevo_proveedor(self):
		self.reg_nuevo=Toplevel(self.lista)
		self.dni_nuevo=StringVar()
		dni_nuevo2=Entry(self.reg_nuevo, textvariable=self.dni_nuevo)
		dni_nuevo2.grid(row=0, column=2, pady=10)
		cuit_nuevo=Label(self.reg_nuevo, text="CUIT")
		cuit_nuevo.grid(row=0, column=0)
		razon_social_nuevo=Label(self.reg_nuevo, text="Razon social")
		razon_social_nuevo.grid(row=1, column=0, padx=10)
		self.cuit_num1=ttk.Combobox(self.reg_nuevo, state="readonly", width=3)
		self.cuit_num1.grid(row=0, column=1, padx=10)
		self.cuit_num1["values"]=["20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33"]
		self.cuit_num2=ttk.Combobox(self.reg_nuevo, state="readonly", width=3)
		self.cuit_num2.grid(row=0, column=3, padx=10)
		self.cuit_num2["values"]=["0","1","2","3","4","5","6","7","8","9"]		
		self.nombre_nuevo=StringVar()
		nombre_nuevo2=Entry(self.reg_nuevo, textvariable=self.nombre_nuevo)
		nombre_nuevo2.grid(row=1, column=1, columnspan=3, pady=10, padx=10, sticky=S+N+E+W)
		crear=Button(self.reg_nuevo, text="Crear registro", command=self.nuevo_proveedor_aceptar)
		crear.grid(row=2, column=2, sticky=S+N+E+W, pady=10, padx=10)
		self.reg_nuevo.grab_set()

		self.reg_nuevo.transient(self.lista)	
		self.dni_nuevo.trace("w", lambda *args: self.limitador(self.dni_nuevo))	
	

	def selec_proveedor(self):
		self.lista=Toplevel(frame1)
		self.tree = ttk.Treeview(self.lista, selectmode=tk.BROWSE, column=("column1","column2"),show='headings')
		self.tree.heading("#1", text="CUIT")
		self.tree.heading("#2", text="Razon Social")
		self.tree.grid(row=0, columnspan=2)
		button=Button(self.lista, text="Seleccionar", command=self.seleccionar_proveedor)
		button.grid(row=1, column=0, padx=10, pady=10)
		button2=Button(self.lista, text="Nuevo", command=self.nuevo_proveedor)
		button2.grid(row=1, column=1, padx=10, pady=10)	
		self.lista.grab_set()
		self.mostrar_proveedores()


	

		

	def ventana(self):

		def capturar_datos(self):
			global frame2

			self.cuitpantalla2=self.cuitpantalla.get()
			self.razonpantalla2=self.razonpantalla.get()
			self.prodpantalla2=prodpantalla.get()
			self.cantpantalla2=cantpantalla.get()
			



		def boton_registrar():
			tipo_op=self.tipo
			capturar_datos(self)

			if tipo_op=="compras":

				op_compras=Clase_Compras()
				op_compras.validar_compra(self.cuitpantalla2, self.razonpantalla2, self.prodpantalla2, self.cantpantalla2)
				
				if op_compras.validar_compra(self.cuitpantalla2, self.razonpantalla2, self.prodpantalla2, self.cantpantalla2)==False:
					
					self.error_datos()
				else:
					op_compras.confirmar_compra()


			else:
				op_ventas=Clase_Ventas()
				op_ventas.validar_venta(self.cuitpantalla2, self.razonpantalla2, self.prodpantalla2, self.cantpantalla2)
				
				if op_ventas.validar_venta(self.cuitpantalla2, self.razonpantalla2, self.prodpantalla2, self.cantpantalla2)==False:
					self.error_datos()
				else:
					op_ventas.confirmar_venta()


			try:
				cantpantalla2=int(cantpantalla2)
			except:
				ValueError

		def limpiar():
			self.cuitpantalla.set("")
			razonpantalla.set("")
			prodpantalla.set("")
			cantpantalla.set("")


		try:
			nuevaventana.winfo_ismapped()
			
		except:
	
			#Creamos una ventana nueva
			nuevaventana=Toplevel(frame1)
			nuevaventana.resizable(width=False, height=False)
			nuevaventana.grab_set()
			
			#CUIT
			self.cuitpantalla=StringVar()
			cuitlabel=Label(nuevaventana, text="CUIT")
			cuitlabel.grid(row=0, column=0, pady=(20,15))			
			cuitentry=Entry(nuevaventana, bd=3, textvariable=self.cuitpantalla, state=DISABLED)
			cuitentry.grid(row=0, column=1, padx=(0,15), pady=(20,15))
			
			#RAZON
			self.razonpantalla=StringVar()
			razonlabel=Label(nuevaventana, text="RAZON SOCIAL")
			razonlabel.grid(row=1, column=0, pady=15, padx=20)
			razonentry=Entry(nuevaventana, bd=3, textvariable=self.razonpantalla, state=DISABLED)
			razonentry.grid(row=1, column=1, padx=(0,15))
			
			#PRODUCTO
			prodpantalla=StringVar()
			prodlabel=Label(nuevaventana, text="PRODUCTO")
			prodlabel.grid(row=2, column=0, pady=15)			
			prodentry=Entry(nuevaventana, bd=3, textvariable=prodpantalla, state=DISABLED)
			prodentry.grid(row=2, column=1, padx=(0,15))
			
			
			#CANTIDAD
			cantpantalla=StringVar()
			cantlabel=Label(nuevaventana, text="CANTIDAD")
			cantlabel.grid(row=3, column=0, pady=15)			
			cantentry=Entry(nuevaventana, bd=3, textvariable=cantpantalla)
			cantentry.grid(row=3, column=1, padx=(0,15))

			#BOTON AGREGAR		
			agregar=Button(nuevaventana, text="Registrar", command=boton_registrar, height=1, width=8, font=5, bd=3)
			agregar.grid(row=5, column=0, pady=15)
			#BOTON LIMPIAR
			limpiar=Button(nuevaventana, text="Limpiar", command=limpiar, height=1, width=8, font=5, bd=3)
			limpiar.grid(row=5, column=1)
			#BOTON SELECCIONAR CUIT
			selec_cuit=Button(nuevaventana, text="Seleccionar", command=self.selec_proveedor)
			selec_cuit.grid(row=0, column=2, padx=(0,15))
			#BOTON SELECCIONAR PRODUCTO
			selec_prod=Button(nuevaventana, text="Seleccionar")#, command=self.selec_articulo)
			selec_prod.grid(row=2, column=2, padx=(0,15))
			

	
	def error_datos(self):
		global frame2
		frame2=Toplevel(frame1, bd=3)
		frame2.grab_set()
		frame2.resizable(width=False, height=False)
		error=Label(frame2, text="ATENCIÓN!!!\nLos datos ingresados son incorrectos o existentes.", font=25)				
		error.grid(row=0, column=0, padx=20, pady=3)
		ok=Button(frame2, text="Continuar", bd=3, font=7, command=lambda: visuales.cerrar())
		ok.grid(row=1, columnspan=3, pady=10, ipady=2, ipadx=4)	





#----------------------------FUNCIONES

def compras():
	compra=visuales()
	compra.ventana()
	compra.tipo="compras"


	print(compra.tipo)

def ventas():
	ventas=visuales()
	ventas.ventana()
	ventas.tipo="ventas"

def stock():
	stock=Clase_Stock()
	stock.ventana_stock()


#-----------BOTONES PRINCIPALES

modificarst=Button(frame1, text="Compras", bd=4, font=(25), width=15, command=compras)
modificarst.grid(row=0, column=0, pady=(50,0))


agregarst=Button(frame1, text="Ventas", bd=4, font=(25), width=15, command=ventas)
agregarst.grid(row=1, column=0, pady=(50,50), padx=50)


borrarst=Button(frame1, text="Stock", bd=4, font=(25), width=15, command=stock)
borrarst.grid(row=4, column=0, pady=(0,50))


root.mainloop()