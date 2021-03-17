import sqlite3

#----------------------------COMPRAS
class Clase_Compras():
	
	def __init__(self):
		self.c_cuit=""
		self.c_razon=""
		self.c_producto=""
		self.c_cantidad=""
		
		try: 	
			conexion=sqlite3.connect("MiNegocio")
			cursor=conexion.cursor()
			cursor.execute("CREATE TABLE COMPRAS (CUIT INTEGER PRIMARY KEY, RAZON VARCHAR(50), PRODUCTO VARCHAR(50), CANTIDAD INTEGER (4))")
			

		except:
			sqlite3.OperationalError


	def validar_compra(self, cuitpantalla2,razonpantalla2,prodpantalla2,cantpantalla2):

		self.c_cuit=cuitpantalla2
		self.c_razon=razonpantalla2
		self.c_producto=prodpantalla2
		self.c_cantidad=cantpantalla2
		try:
			cantpantalla2=int(cantpantalla2)
		except:
			ValueError


		if cuitpantalla2=="" or prodpantalla2=="" or isinstance(cantpantalla2,int)==False or cantpantalla2==0:
			
			return False
		else:
			return True
			
	def confirmar_compra(self):

			compra=[self.c_cuit, self.c_razon, self.c_producto, self.c_cantidad]
			print(compra)
			
			conexion=sqlite3.connect("MiNegocio")
			cursor=conexion.cursor()
			cursor.execute("INSERT INTO COMPRAS VALUES(?,?,?,?)", compra)
			conexion.commit()
			messagebox.showinfo(message="La compra fue registrada correctamente")
