import tkinter as tk
import Bienvenida


def abrir_cierre_caja(ventana_Bienvenida):
    Ventana = tk.Toplevel(ventana_Bienvenida)
    Ventana.title("ventana Tomas")
    Ventana.geometry(f"470x600+400+50")
    Ventana.configure(bg="#FDF5E6")
    Ventana.resizable(False, False)

    Ventana.title()
    etiqueta_total = tk.Label(Ventana, text="CIERRE DE CAJA")
    etiqueta_total.config(fg="red", bg="#FDF5E6", font=("Open Sans", 20, "bold"))
    etiqueta_total.pack()

    def volver():
        Ventana.destroy()
        ventana_Bienvenida.deiconify()

    boton_fecha = tk.Button(Ventana, text="FECHA")
    boton_fecha.configure(fg="black", bg="#a6a6a6", font=("Open Sans", 10), width=14)
    boton_fecha.place(x=55, y=100)

    etiqueta_cajero = tk.Label(Ventana, text="CAJERO")
    etiqueta_cajero.configure(fg="black", bg="#FDF5E6", font=("Open Sans", 10))
    etiqueta_cajero.place(x=55, y=180)

    etiqueta_gastos_total = tk.Label(Ventana, text="GASTOS TOTALES")
    etiqueta_gastos_total.configure(fg="black", bg="#FDF5E6", font=("Open Sans", 10))
    etiqueta_gastos_total.place(x=55, y=240)

    etiqueta_totalc = tk.Label(Ventana, text="TOTAL CIERRE")
    etiqueta_totalc.configure(fg="black", bg="#FDF5E6", font=("Open Sans", 10))
    etiqueta_totalc.place(x=55, y=300)

    etiqueta_fecha2 = tk.Label(Ventana, text="DD/MM/AAAA")
    etiqueta_fecha2.configure(fg="black", bg="#FDF5E6", font=("Open Sans", 10))
    etiqueta_fecha2.place(x=300, y=105)

    etiqueta_cajerou = tk.Label(Ventana, text="CAJERO USUARIO ")
    etiqueta_cajerou.configure(fg="black", bg="#FDF5E6", font=("Open Sans", 10))
    etiqueta_cajerou.place(x=300, y=180)

    etiqueta_signo1 = tk.Label(Ventana, text="$$$$$ ")
    etiqueta_signo1.configure(fg="black", bg="#FDF5E6", font=("Open Sans", 10))
    etiqueta_signo1.place(x=300, y=240)

    etiqueta_signo2 = tk.Label(Ventana, text="$$$$$")
    etiqueta_signo2.configure(fg="black", bg="#FDF5E6", font=("Open Sans", 10))
    etiqueta_signo2.place(x=300, y=300)

    boton_guardar_cierre = tk.Button(Ventana, text="GUARDAR CIERRE")
    boton_guardar_cierre.configure(fg="black", bg="#a6a6a6", font=("Open Sans", 10), width=14)
    boton_guardar_cierre.place(x=180, y=380)

    volver = tk.Button(Ventana, text="VOLVER", command=volver)
    volver.config(fg="black", bg="#a6a6a6", font=("Open Sans", 10), width=14)
    volver.place(x=180, y=420)

    Ventana.iconbitmap(r"C:\Users\Diego Zamora\OneDrive\Documentos\Adsi 2024\interface grafica\recursos\logoico.ico")

    Ventana.mainloop()
