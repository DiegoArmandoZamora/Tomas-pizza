import tkinter as tk
from tkinter import *
import TomaPedido
import CierreCaja
import CompararFechas
import Gastos




def abrir_bienvenida(ventana_login):
    Bienvenida = Toplevel(ventana_login)
    Bienvenida.title("Bienvenida")
    Bienvenida.config(width=500, height=600, bg="#FDF5E6")
    Bienvenida.geometry(f"500x600+400+50")
    Bienvenida.resizable(False, False)



    def registrarPedido():
        Bienvenida.withdraw()
        TomaPedido.abrir_registrar_pedido(Bienvenida)

    def cierreCaja():
        Bienvenida.withdraw()
        CierreCaja.abrir_cierre_caja(Bienvenida)

    def compararFechas():
        Bienvenida.withdraw()
        CompararFechas.abrir_comparar_fechas(Bienvenida)

    def gastos():
        Bienvenida.withdraw()
        Gastos.abrir_gastos(Bienvenida)

        # FECHA Y HORA
        from time import strftime
        def actualizar_reloj():
            tiempo_actual = strftime('%H:%M:%S %p')
            fecha_actual = strftime('%Y-%m-%d')
            etiqueta_hora.config(text=tiempo_actual)
            etiqueta_fecha.config(text=fecha_actual)
            Bienvenida.after(100, actualizar_reloj)

        marco_derecho = tk.Frame(Bienvenida, background='#FDF5E6')
        marco_derecho.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        etiqueta_hora = tk.Label(Bienvenida, font=('cabril', 10, 'bold'), background='#FDF5E6', foreground='BLACK')
        etiqueta_hora.pack(anchor='center')

        etiqueta_fecha = tk.Label(Bienvenida, font=('cabril', 10, 'bold'), background='#FDF5E6', foreground='BLACK')
        etiqueta_fecha.pack(anchor='center')
        actualizar_reloj()

    label = Label(Bienvenida, text="BIENVENIDO USUARIO", background="#FDF5E6", font=("Open Sans", 20, 'bold'), fg="red")
    label.pack()
    label.place(x=95, y=100)



    botonr = tk.Button(Bienvenida, text="REGISTRAR PEDIDO", command=registrarPedido)
    botonr.place(x=190, y=200)
    botonr.config(width=15, bg="#FDF5E6")

    botonc = tk.Button(Bienvenida, text="CIERRE DE CAJA", command=cierreCaja)
    botonc.place(x=190, y=250)
    botonc.config(width=15, bg="#FDF5E6")

    botonf = tk.Button(Bienvenida, text="COMPARAR FECHAS", command=compararFechas)
    botonf.place(x=190, y=300)
    botonf.config(width=15, bg="#FDF5E6")

    botong = tk.Button(Bienvenida, text="AGREGAR GASTO", command=gastos)
    botong.place(x=190, y=350)
    botong.config(width=15, bg="#FDF5E6")

    Bienvenida.iconbitmap(r"C:\Users\Diego Zamora\OneDrive\Documentos\Adsi 2024\interface grafica\recursos\logoico.ico")

    Bienvenida.mainloop()
