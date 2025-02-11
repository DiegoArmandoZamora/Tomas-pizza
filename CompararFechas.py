import tkinter as tk
from tkinter import simpledialog
from PIL import Image, ImageTk
import messagebox
import mysql.connector
from time import strftime



def conectar_db():
    conn = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="Tomas_pizza",
        port="3306"
    )
    return conn

def obtener_gastos(fecha):
    conn = conectar_db()
    cursor = conn.cursor()
    query= f"SELECT SUM(valor_gasto) FROM gastos WHERE fecha LIKE '{fecha}%'"
    cursor.execute(query)
    resultado = cursor.fetchone()
    conn.close()
    return resultado[0] if resultado[0] else 0

def obtener_cierre(fecha):
    conn = conectar_db()
    cursor = conn.cursor()
    query = f"SELECT Total_general FROM cierre WHERE Ventas_fecha = '{fecha}'"
    cursor.execute(query)
    resultado = cursor.fetchone()
    conn.close()
    return resultado[0] if resultado else 0

def abrir_comparar_fechas(ventana_Bienvenida):
        Ventana = tk.Toplevel(ventana_Bienvenida)
        Ventana.title("ventana Tomas")
        Ventana.geometry(f"510x600+400+50")
        Ventana.configure(bg="#FDF5E6")
        Ventana.resizable(False, False)


        # Fecha y hora

        from time import strftime
        def actualizar_reloj():
            tiempo_actual = strftime('%H:%M:%S %p')
            fecha_actual = strftime('%Y-%m-%d')
            etiqueta_hora.config(text=tiempo_actual)
            etiqueta_fecha.config(text=fecha_actual)
            Ventana.after(100, actualizar_reloj)

        def volver():
            Ventana.destroy()
            ventana_Bienvenida.deiconify()



        marco_derecho = tk.Frame(Ventana, background='#FDF5E6')
        marco_derecho.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        ruta_imagen_fondo = r"C:\Users\Diego Zamora\OneDrive\Documentos\Adsi 2024\repositorio\Tomas-pizza\recursos\fondo 1.jpg"
        imagen_fondo = Image.open(ruta_imagen_fondo)
        imagen_fondo = imagen_fondo.resize((500, 600))
        imagen_fondo = ImageTk.PhotoImage(imagen_fondo)

        label_fondo = tk.Label(Ventana, image=imagen_fondo)
        label_fondo.place(x=0, y=0, relwidth=1, relheight=1)

        etiqueta_hora = tk.Label(Ventana, font=('cabril', 10, 'bold'), background='#FDF5E6', foreground='BLACK')
        etiqueta_hora.pack(anchor='center')

        etiqueta_fecha = tk.Label(Ventana, font=('cabril', 10, 'bold'), background='#FDF5E6', foreground='BLACK')
        etiqueta_fecha.pack(anchor='center')

        actualizar_reloj()

        Ventana.title()
        etiqueta_total = tk.Label(Ventana, text="COMPARAR FECHAS")
        etiqueta_total.config(fg="red", bg="#FDF5E6", font=("Open Sans", 20, "bold"))
        etiqueta_total.place(x=110, y=30)

        def seleccionar_fecha_a():
            fecha_a = simpledialog.askstring("Fecha A", "Introduce la fecha (YYYY-MM-DD):")
            if fecha_a:
                gastos_a = obtener_gastos(fecha_a)
                cierre_a = obtener_cierre(fecha_a)
                if gastos_a == 0 and cierre_a == 0:
                    messagebox.showwarning("No hay datos", "No se encontro ningun resultado para la consulta")
                    seleccionar_fecha_a()
                else:
                   etiqueta_gastos_a.config(text=f"GASTOS FECHA A: ${gastos_a}")
                   etiqueta_cierre_a.config(text=f"CIERRE FECHA A: ${cierre_a}")
                   etiqueta_fecha_a.config(text=f"Fecha A Consultada: {fecha_a}")

        def seleccionar_fecha_b():
            fecha_b = simpledialog.askstring("Fecha B", "Introduce la fecha (YYYY-MM-DD):")
            if fecha_b:
                gastos_b = obtener_gastos(fecha_b)
                cierre_b = obtener_cierre(fecha_b)
                if gastos_b == 0 and cierre_b == 0:
                    messagebox.showerror("No hay datos disponibles", "No se encontro ningun resultado para la consulta")

                else:
                    etiqueta_gastos_b.config(text=f"GASTOS FECHA B: ${gastos_b}")
                    etiqueta_cierre_b.config(text=f"CIERRE FECHA B: ${cierre_b}")
                    etiqueta_fecha_b.config(text=f"Fecha B consulta: {fecha_b}")

        def borrar_consulta():
            etiqueta_gastos_a.config(text="GASTOS FECHA A:")
            etiqueta_cierre_a.config(text="CIERRE FECHA A:")
            etiqueta_fecha_a.config(text="Fecha A Consultar")
            etiqueta_gastos_b.config(text="GASTOS FECHA B:")
            etiqueta_cierre_b.config(text="CIERRE FECHA B:")
            etiqueta_fecha_b.config(text="Fecha B Consultar")


        boton_fecha_a = tk.Button(Ventana, text="FECHA A", command=seleccionar_fecha_a)
        boton_fecha_a.configure(fg="black", bg="#FDF5E6", font=("Open Sans", 10), width=13)
        boton_fecha_a.place(x=50,y=100)

        boton_fecha_b = tk.Button(Ventana, text="FECHA B", command=seleccionar_fecha_b)
        boton_fecha_b.configure(fg="black", bg="#FDF5E6", font=("Open Sans", 10), width=13)
        boton_fecha_b.place(x=320, y=100)

        def cambiar_color_hover(boton):
            boton.config(bg="gray")

        def restaurar_color(boton):
            boton.config(bg="#FDF5E6")

        boton_fecha_a.bind("<Enter>", lambda event: cambiar_color_hover(boton_fecha_a))
        boton_fecha_a.bind("<Leave>", lambda event: restaurar_color(boton_fecha_a))

        boton_fecha_b.bind("<Enter>", lambda event: cambiar_color_hover(boton_fecha_b))
        boton_fecha_b.bind("<Leave>", lambda event: restaurar_color(boton_fecha_b))

        etiqueta_total_pizas = tk.Label(Ventana, text="GASTOS FECHA A: ")
        etiqueta_total_pizas.configure(fg="black", bg="#FDF5E6", font=("Open Sans", 10))
        etiqueta_total_pizas.place(x=55, y=180)

        etiqueta_total_bebidas = tk.Label(Ventana, text="CIERRE FECHA A: ")
        etiqueta_total_bebidas.configure(fg="black", bg="#FDF5E6", font=("Open Sans", 10))
        etiqueta_total_bebidas.place(x=55, y=240)

        etiqueta_gastos_a = tk.Label(Ventana, text="GASTOS FECHA A: ")
        etiqueta_gastos_a.configure(fg="black", bg="#FDF5E6", font=("Open Sans", 10))
        etiqueta_gastos_a.place(x=55, y=180)

        etiqueta_cierre_a = tk.Label(Ventana, text="CIERRE FECHA A: ")
        etiqueta_cierre_a.configure(fg="black", bg="#FDF5E6", font=("Open Sans", 10))
        etiqueta_cierre_a.place(x=55, y=240)

        etiqueta_gastos_b = tk.Label(Ventana, text="GASTOS FECHA B: ")
        etiqueta_gastos_b.configure(fg="black", bg="#FDF5E6", font=("Open Sans", 10))
        etiqueta_gastos_b.place(x=320, y=180)

        etiqueta_cierre_b = tk.Label(Ventana, text="CIERRE FECHA B: ")
        etiqueta_cierre_b.configure(fg="black", bg="#FDF5E6", font=("Open Sans", 10))
        etiqueta_cierre_b.place(x=320, y=240)

        etiqueta_fecha_a = tk.Label(Ventana,text="fecha A Consultar")
        etiqueta_fecha_a.configure(fg="black", bg="#FDF5E6", font=("Open Sans", 10))
        etiqueta_fecha_a.place(x=55, y=300)

        etiqueta_fecha_b = tk.Label(Ventana, text="Fecha B Consultada: ")
        etiqueta_fecha_b.configure(fg="black", bg="#FDF5E6", font=("Open Sans", 10))
        etiqueta_fecha_b.place(x=320, y=300)

        boton_borrar = tk.Button(Ventana, text="BORRAR CONSULTA", command=borrar_consulta)
        boton_borrar.configure(fg="black", bg="#ff6666", font=("Open Sans", 10), width=16)
        boton_borrar.place(x=190, y=360)


        volver_btn = tk.Button(Ventana, text="VOLVER", command=volver)
        volver_btn.configure(fg="black", bg="#a6a6a6", font=("Open Sans", 10), width=15)
        volver_btn.place(x=190, y=410)

        def cambiar_color_hover(boton):
            boton.config(bg="gray")

        def restaurar_color(boton):
            boton.config(bg="#FDF5E6")

        boton_borrar.bind("<Enter>", lambda event: cambiar_color_hover(boton_borrar))
        boton_borrar.bind("<Leave>", lambda event: restaurar_color(boton_borrar))

        volver_btn.bind("<Enter>", lambda event: cambiar_color_hover(volver_btn))
        volver_btn.bind("<Leave>", lambda event: restaurar_color(volver_btn))


        Ventana.iconbitmap( r"C:\Users\Diego Zamora\OneDrive\Documentos\Adsi 2024\repositorio\Tomas-pizza\recursos\logoico.ico")
        Ventana.mainloop()