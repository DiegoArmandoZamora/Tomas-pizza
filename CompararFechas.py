import tkinter as tk


def abrir_comparar_fechas(ventana_Bienvenida):
    Ventana = tk.Toplevel(ventana_Bienvenida)
    Ventana.title("ventana Tomas")
    Ventana.geometry(f"510x600+400+50")
    Ventana.configure(bg="#FDF5E6")
    Ventana.resizable(False, False)

    def volver():
        Ventana.destroy()
        ventana_Bienvenida.deiconify()

    # Fecha y hora
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

    Ventana.title()
    etiqueta_total = tk.Label(Ventana, text="COMPARAR FECHAS")
    etiqueta_total.config(fg="red", bg="#FDF5E6", font=("Open Sans", 20, "bold"))
    etiqueta_total.place(x=110, y=30)

    boton_editar_pedido = tk.Button(Ventana, text="FECHA A")
    boton_editar_pedido.configure(fg="black", bg="#a6a6a6", font=("Open Sans", 10), width=13)
    boton_editar_pedido.place(x=50, y=100)

    boton_editar_pedido = tk.Button(Ventana, text="FECHA B ")
    boton_editar_pedido.configure(fg="black", bg="#a6a6a6", font=("Arial", 10), width=13)
    boton_editar_pedido.place(x=320, y=100)

    etiqueta_pedido = tk.Label(Ventana, text="FECHA DD/MM/AA: ")
    etiqueta_pedido.configure(fg="black", bg="#FDF5E6", font=("Open Sans", 10))
    etiqueta_pedido.place(x=55, y=180)

    etiqueta_cantidad = tk.Label(Ventana, text="GASTOS FECHAS $$$: ")
    etiqueta_cantidad.configure(fg="black", bg="#FDF5E6", font=("Open Sans", 10))
    etiqueta_cantidad.place(x=55, y=240)

    etiqueta_bebidas = tk.Label(Ventana, text="CIERRE$$$: ")
    etiqueta_bebidas.configure(fg="black", bg="#FDF5E6", font=("Open Sans", 10))
    etiqueta_bebidas.place(x=55, y=300)

    etiqueta_total_pizas = tk.Label(Ventana, text="FECHA DD/MM/AA: ")
    etiqueta_total_pizas.configure(fg="black", bg="#FDF5E6", font=("Open Sans", 10))
    etiqueta_total_pizas.place(x=320, y=180)

    etiqueta_total_pizas = tk.Label(Ventana, text="GASTOS FECHAS $$$: ")
    etiqueta_total_pizas.configure(fg="black", bg="#FDF5E6", font=("Open Sans", 10))
    etiqueta_total_pizas.place(x=320, y=240)

    etiqueta_total_bebidas = tk.Label(Ventana, text="CIERRE$$$: ")
    etiqueta_total_bebidas.configure(fg="black", bg="#FDF5E6", font=("Open Sans", 10))
    etiqueta_total_bebidas.place(x=320, y=300)

    boton_guardar_cierre = tk.Button(Ventana, text="IMPRIMIR REPORTE")
    boton_guardar_cierre.configure(fg="black", bg="#a6a6a6", font=("Open Sans", 10), width=15)
    boton_guardar_cierre.place(x=190, y=370)

    volver = tk.Button(Ventana, text="VOLVER", command=volver)
    volver.configure(fg="black", bg="#a6a6a6", font=("Open Sans", 10), width=15)
    volver.place(x=190, y=410)

    Ventana.iconbitmap(r"C:\Users\Diego Zamora\OneDrive\Documentos\Adsi 2024\interface grafica\recursos\logoico.ico")

    Ventana.mainloop()
