import sqlite3

#----------------------------VENTAS
class Clase_Ventas():
	
	def __init__(self):
		self.v_cuit=""
		self.v_razon=""
		self.v_producto=""
		self.v_cantidad=""
		
		try: 	
			conexion=sqlite3.connect("MiNegocio")
			cursor=conexion.cursor()
			cursor.execute("CREATE TABLE VENTAS (CUIT INTEGER PRIMARY KEY, RAZON VARCHAR(50), PRODUCTO VARCHAR(50), CANTIDAD INTEGER(4))")
		except:
			sqlite3.OperationalError	

	def validar_venta(self, cuitpantalla2,razonpantalla2,prodpantalla2,cantpantalla2):
		self.v_cuit=cuitpantalla2
		self.v_razon=razonpantalla2
		self.v_producto=prodpantalla2
		self.v_cantidad=cantpantalla2
		try:
			cantpantalla2=int(cantpantalla2)
		except:
			ValueError


		if cuitpantalla2=="" or prodpantalla2=="" or isinstance(cantpantalla2,int)==False or cantpantalla2==0:

			return False
		else:
			return True

			
	def confirmar_venta(self):

			ventas=[self.v_cuit, self.v_razon, self.v_producto, self.v_cantidad]
			print(ventas)
			
			conexion=sqlite3.connect("MiNegocio")
			cursor=conexion.cursor()
			cursor.execute("INSERT INTO VENTAS VALUES(?,?,?,?)", ventas)
			conexion.commit()
			messagebox.showinfo(message="La compra fue registrada correctamente")