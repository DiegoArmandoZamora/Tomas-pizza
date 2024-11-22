import tkinter as tk
from tkinter import messagebox
import mysql.connector



def abrir_gastos(ventana_Bienvenida):
    Ventana = tk.Toplevel(ventana_Bienvenida)
    Ventana.title("ventana Tomas")
    Ventana.geometry(f"490x600+400+50")
    Ventana.configure(bg="#FDF5E6")
    Ventana.resizable(False, False)

    def volver():
        Ventana.destroy()
        ventana_Bienvenida.deiconify()

    Ventana.title()
    etiqueta_total = tk.Label(Ventana, text="GASTOS DE OPERACION")
    etiqueta_total.config(fg="red", bg="#FDF5E6", font=("Open Sans", 20, "bold"))
    etiqueta_total.pack()

    def volver():
        Ventana.destroy()
        ventana_Bienvenida.deiconify()

# Funcion para conectar a la base de datos
    def conectar_db():
        try:
            conexion = mysql.connector.connect(
                host = "127.0.0.1",
                user= "root",
                password= "",
                database= "Tomas_pizza",
                port="3306"
            )
            return conexion

        except mysql.connector.Error as err:
            messagebox.showerror("Error de coneccion",f"Error: {err}")
            return None
# Funcion para guardar gastos en la base de datos

    def guardar_gastos():
        nombre_cajero = etiqueta_cajerou.get()
        valor_gasto = gasto.get()
        factura_num = factura.get()
        descripcion = info.get()

        if not nombre_cajero or not valor_gasto or not factura_num or not descripcion:
            messagebox.showwarning("Ingreso de datos exitoso","Por favor completa los todos los campos.")
            return

        conexion = conectar_db()
        if conexion:
            cursor = conexion.cursor()

            try:
                query = "insert into gastos (nombre_cajero,valor_gasto,factura_num,descripcion)VALUES(%s,%s,%s,%s)"
                cursor.execute(query,(nombre_cajero,valor_gasto,factura_num,descripcion))
                conexion.commit()
                messagebox.showinfo("Exito","gasto guardado correctamente.")
            except mysql.connector.Error as err:
                messagebox.showerror("Error al guardar",f"Error:{err}")
            finally:
                cursor.close()
                conexion.close()

    # CODIGO FECHA Y HORA
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
# Boton fecha
    boton_fecha = tk.Button(Ventana, text="FECHA")
    boton_fecha.configure(fg="black", bg="#a6a6a6", font=("Open Sans", 10), width=14)
    boton_fecha.place(x=55, y=100)

    etiqueta_cajero = tk.Label(Ventana, text="CAJERO")
    etiqueta_cajero.configure(fg="black", bg="#FDF5E6", font=("Open Sans", 10))
    etiqueta_cajero.place(x=55, y=160)

    etiqueta_gastos_total = tk.Label(Ventana, text="VALOR GASTO")
    etiqueta_gastos_total.configure(fg="black", bg="#FDF5E6", font=("Open Sans", 10))
    etiqueta_gastos_total.place(x=55, y=200)

    etiqueta_totalc = tk.Label(Ventana, text="FACTURA #")
    etiqueta_totalc.configure(fg="black", bg="#FDF5E6", font=("Open Sans", 10))
    etiqueta_totalc.place(x=55, y=240)

    etiqueta_des = tk.Label(Ventana, text="DESCRIPCION GASTO")
    etiqueta_des.config(fg="black", bg="#FDF5E6", font=("Open Sans", 10))
    etiqueta_des.place(x=55, y=280)

    etiqueta_fecha2 = tk.Label(Ventana, text="DD/MM/AAAA")
    etiqueta_fecha2.configure(fg="black", bg="#FDF5E6", font=("Open Sans", 10))
    etiqueta_fecha2.place(x=300, y=105)

    etiqueta_cajerou = tk.Label(Ventana, text="NOMBRE CAJERO ")
    etiqueta_cajerou = tk.Entry(Ventana, font=("Open Sans", 10), width=15)
    etiqueta_cajerou.place(x=300, y=160)

    gasto = tk.Entry(Ventana, font=("Open Sans", 10), width=15)
    gasto.place(x=300, y=200)

    factura = tk.Entry(Ventana, font=("Open Sans", 10), width=15)
    factura.place(x=300, y=240)

    info = tk.Entry(Ventana, font=("Open Sans", 10), width=15)
    info.place(x=300, y=280)

    boton_guardar_cierre = tk.Button(Ventana, text="GUARDAR GASTO",command=guardar_gastos)
    boton_guardar_cierre.configure(fg="black", bg="#a6a6a6", font=("Open Sans", 10), width=14)
    boton_guardar_cierre.place(x=180, y=360)

    volver = tk.Button(Ventana, text="VOLVER", command=volver)
    volver.config(fg="black", bg="#a6a6a6", font=("Open Sans", 10), width=14)
    volver.place(x=180, y=400)



    Ventana.iconbitmap(r"C:\Users\Diego Zamora\OneDrive\Documentos\Adsi 2024\interface grafica\recursos\logoico.ico")

    Ventana.mainloop()
