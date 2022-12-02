from tkinter import *
from tkinter import ttk
from tkinter.tix import COLUMN
from turtle import width
import base_datos

mysql = base_datos.BD()
ventana = Tk()
ventana.title("Mysql con tkinter")
ventana.geometry("850x500")

#   Variables con tkinter de la tabla EntradaSalidaDinero
FechaES = StringVar()
idIngEgr = StringVar()
montoIE = StringVar()
idPersonas = StringVar()
Observaciones = StringVar()

#   Agregamos un LabelFrame
marco = LabelFrame(ventana, text = "Tabla EntradaSalidaDinero")
marco.place(x = 50, y = 50, width = 620, height = 400)

#   Agregamos Label y texinput para cada variable
lblFechaES = Label(marco, text = "Fecha: ")
lblFechaES.grid(column = 0, row = 0, padx = 5, pady = 5)
lblFechaES = Entry(marco, textvariable = FechaES)
lblFechaES.grid(column = 1, row = 0)

lblidIngEgr = Label(marco, text = "Ingreso/Egreso: ")
lblidIngEgr.grid(column = 2, row = 0, padx = 5, pady = 5)
lblidIngEgr = Entry(marco, textvariable = idIngEgr)
lblidIngEgr.grid(column = 3, row = 0)

lblmontoIE = Label(marco, text = "Cantidad: ")
lblmontoIE.grid(column = 0, row = 1, padx = 5, pady = 5)
lblmontoIE = Entry(marco, textvariable = montoIE)
lblmontoIE.grid(column = 1, row = 1)

lblidPersonas = Label(marco, text = "IdPersona: ")
lblidPersonas.grid(column = 2, row = 1, padx = 5, pady = 5)
lblidPersonas = Entry(marco, textvariable = idPersonas)
lblidPersonas.grid(column = 3, row = 1)

lblObservaciones = Label(marco, text = "Observaciones: ")
lblObservaciones.grid(column = 0, row = 2, padx = 5, pady = 5)
lblObservaciones = Entry(marco, textvariable = Observaciones)
lblObservaciones.grid(column = 1, row = 2)

#Agregamos título para la tabla + color
mensaje = Label(marco, text = "Contenido de la tabla", fg = "purple")
mensaje.grid(column = 0, row = 3, columnspan = 4)

#Agregamos títulos para las columnas de la tabla
tventradasalidadinero = ttk.Treeview(marco)
tventradasalidadinero.grid(column = 0, row = 4, columnspan = 4, padx = 5)
tventradasalidadinero["columns"] = ("Id", "FechaES", "idIngEgr", "montoIE", "idPersonas", "Observaciones")

tventradasalidadinero.column("#0", width = 0, stretch = NO)
tventradasalidadinero.column("Id", width = 100, anchor = CENTER)
tventradasalidadinero.column("FechaES", width = 100, anchor = CENTER)
tventradasalidadinero.column("idIngEgr", width = 100, anchor = CENTER)
tventradasalidadinero.column("montoIE", width = 100, anchor = CENTER)
tventradasalidadinero.column("idPersonas", width = 100, anchor = CENTER)
tventradasalidadinero.column("Observaciones", width = 100, anchor = CENTER)

tventradasalidadinero.heading("Id", text = "Id", anchor = CENTER)
tventradasalidadinero.heading("FechaES", text = "FechaES", anchor = CENTER)
tventradasalidadinero.heading("idIngEgr", text = "idIngEgr", anchor = CENTER)
tventradasalidadinero.heading("montoIE", text = "montoIE", anchor = CENTER)
tventradasalidadinero.heading("idPersonas", text = "idPersonas", anchor = CENTER)
tventradasalidadinero.heading("Observaciones", text = "Observaciones", anchor = CENTER)

#Agregamos los botones de edición de la tabla
btnAgregar = Button(marco, text = "Agregar", command = lambda:agregar())
btnAgregar.grid(column = 0, row = 5, pady = 5)

btnActualizar = Button(marco, text = "Actualizar", command = lambda:actualizar())
btnActualizar.grid(column = 1, row = 5, pady = 5)

btnEliminar = Button(marco, text = "Eliminar", command = lambda:eliminar())
btnEliminar.grid(column = 2, row = 5, pady = 5)

#Se establecen las funciones requeridas para manipular la tabla
def validar():
    return len(FechaES.get()) and len(idIngEgr.get()) and len(montoIE.get()) and len(idPersonas.get()) and len(Observaciones.get())
def vaciar_tabla():
    filas = tventradasalidadinero.get_children()
    for fila in filas:
        tventradasalidadinero.delete(fila)

def llenar_tabla():
    vaciar_tabla()
    consulta = mysql.select("entradasalidadinero")
    for fila in consulta:
        id = fila[0]
        tventradasalidadinero.insert("",END, text = id, values = fila)

def limpiar():
    FechaES.set('')
    idIngEgr.set('')
    montoIE.set('')
    idPersonas.set('')
    Observaciones.set('')
def agregar():
    if validar():
        variables = FechaES.get(), idIngEgr.get(), montoIE.get(), idPersonas.get(), Observaciones.get()
        sql = "insert from entradasalidadinero into (FechaES, idIngEgr, montoIE, idPersonas, Observaciones) values (%s, %s, %s, %s, %s)"
        mysql.agregar(sql)
        llenar_tabla()
        limpiar()

def actualizar():
    pass

def eliminar():
    item_seleccionado = tventradasalidadinero.focus()
    detalle = tventradasalidadinero.item(item_seleccionado)
    id = detalle.get("values")[0]
    if id > 0:
        sql = 'delete from entradasalidadinero where id = ' + str(id)
        mysql.eliminar(sql)
        llenar_tabla()

llenar_tabla()
ventana.mainloop()
