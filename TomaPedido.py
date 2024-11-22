import tkinter
import tkinter as tk
from tkinter import ttk
from tkinter import *
import Bienvenida
import TotalPagar
from TotalPagar import abrirPagoPedido, contador_pedidos
import random

contador_pedidos = 0

def abrir_registrar_pedido(ventana_Bienvenida):
    Ventana = Toplevel(ventana_Bienvenida)
    Ventana.title("Toma de pedido")
    Ventana.geometry(f"500x600+400+50")
    Ventana.config(bg="#FDF5E6")
    Ventana.resizable(False, False)

    def pagoPedido():
        global contador_pedidos

        vegetariana = int(entryVegetariana.get() or 0)
        carnes = int(entryCarnes.get() or 0)
        peperoni = int(entryPeperoni.get() or 0)
        pollo = int(entryPollo.get() or 0)
        bbq = int(entryBbq.get() or 0)
        bebidas = int(entryBebidas.get() or 0)

        contador_pedidos += 1

        Ventana.withdraw()
        TotalPagar.abrirPagoPedido(Ventana, vegetariana, carnes, peperoni, pollo, bbq, bebidas,contador_pedidos)


    def volver():
        Ventana.destroy()
        ventana_Bienvenida.deiconify()

    # fecha y hora
    from time import strftime
    def actualizar_reloj():
        tiempo_actual = strftime('%H:%M:%S %p')
        fecha_actual = strftime('%Y-%m-%d')
        etiqueta_hora.config(text=tiempo_actual)
        etiqueta_fecha.config(text=fecha_actual)
        Ventana.after(100, actualizar_reloj)

    marco_derecho = tk.Frame(Ventana, background='#FDF5E6')
    marco_derecho.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    etiqueta_hora = tk.Label(Ventana, font=('cabril', 10, 'bold'), background='#FDF5E6', foreground='BLACK')
    etiqueta_hora.pack(anchor='center')

    etiqueta_fecha = tk.Label(Ventana, font=('cabril', 10, 'bold'), background='#FDF5E6', foreground='BLACK')
    etiqueta_fecha.pack(anchor='center')
    actualizar_reloj()
    # Fin fehca y hora

    label = tk.Label(Ventana, text="TOMA DE PEDIDO", font=("Open", 20, "bold"), fg="#f5402e", bg="#FDF5E6")
    label.pack()
    label.place(x=125, y=30)

    label1 = Label(Ventana, text="PRODUCTO", background="#FDF5E6", font=("Open", 12, "bold"), fg="#f5402e", bg="#FDF5E6")
    label1.pack()
    label1.place(x=63, y=100)

    label2 = Label(Ventana, text="CANTIDAD", background="#FDF5E6", font=("Open", 12, "bold"), fg="#f5402e", bg="#FDF5E6")
    label2.pack()
    label2.place(x=350, y=100)

    labelVegetariana = tk.Label(Ventana, text="PIZZA VEGETARIANA", bg="#FDF5E6", font=("Open", 10))
    labelVegetariana.place(x=60, y=150)

    labelPeperoni = tk.Label(Ventana, text="PIZZA PEPERONI", bg="#FDF5E6", font=("Open", 10))
    labelPeperoni.place(x=60, y=230)

    labelCarnes = tk.Label(Ventana, text="PIZZA DE CARNES", bg="#FDF5E6", font=("Open", 10))
    labelCarnes.place(x=60, y=190)

    labelPollo = tk.Label(Ventana, text="PIZZA DE POLLO", bg="#FDF5E6", font=("Open", 10))
    labelPollo.place(x=60, y=270)

    labelBbq = tk.Label(Ventana, text="PIZZA DE BBQ", bg="#FDF5E6", font=("Open", 10))
    labelBbq.place(x=60, y=310)

    labelBebidas = tk.Label(Ventana, text="BEBIDAS", bg="#FDF5E6", font=("Open", 10))
    labelBebidas.place(x=60, y=350)

    entryVegetariana = tk.Entry(Ventana, font=("Open Sans", 10), width=5)
    entryVegetariana.place(x=375, y=150)

    entryCarnes = tk.Entry(Ventana, font=("Open Sans", 10), width=5)
    entryCarnes.place(x=375, y=190)

    entryPeperoni = tk.Entry(Ventana, font=("Open Sans", 10), width=5)
    entryPeperoni.place(x=375, y=230)

    entryPollo = tk.Entry(Ventana, font=("Open Sans", 10), width=5)
    entryPollo.place(x=375, y=270)

    entryBbq = tk.Entry(Ventana, font=("Open Sans", 10), width=5)
    entryBbq.place(x=375, y=310)

    entryBebidas = tk.Entry(Ventana, font=("Open Sans", 10), width=5)
    entryBebidas.place(x=375, y=350)

    generar = tk.Button(Ventana, text="GENERAR PEDIDO", bg="#a6a6a6", command=pagoPedido)
    generar.place(x=190, y=400)
    generar.config(width=18)

    volver = tk.Button(Ventana, text="VOLVER", bg="#a6a6a6", command=volver)
    volver.place(x=190, y=450)
    volver.config(width=18)

    Ventana.iconbitmap(r"C:\Users\Diego Zamora\OneDrive\Documentos\Adsi 2024\interface grafica\recursos\logoico.ico")
    Ventana.mainloop()