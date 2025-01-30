import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox
import mysql.connector
from django.db.models.expressions import result
from datetime import datetime,date
from PIL import Image, ImageTk



def abrir_cierre_caja(ventana_Bienvenida, boton_registrar_pedido):
    Ventana = tk.Toplevel(ventana_Bienvenida)
    Ventana.title("Ventana Tomas")
    Ventana.geometry(f"470x600+400+50")
    Ventana.configure(bg="#FDF5E6")
    Ventana.resizable(False, False)

# fondo de pantalla

    ruta_imagen_fondo = r"C:\Users\Diego Zamora\OneDrive\Documentos\Adsi 2024\repositorio\Tomas-pizza\recursos\fondo 3.jpg"
    imagen_fondo = Image.open(ruta_imagen_fondo)
    imagen_fondo = imagen_fondo.resize((500, 600))
    imagen_fondo = ImageTk.PhotoImage(imagen_fondo)

    label_fondo = tk.Label(Ventana, image=imagen_fondo)
    label_fondo.place(x=0, y=0, relwidth=1, relheight=1)

    etiqueta_total = tk.Label(Ventana, text="CIERRE DE CAJA")
    etiqueta_total.config(fg="red", bg="#FDF5E6", font=("Open Sans", 20, "bold"))
    etiqueta_total.pack()



    def volver():
        Ventana.destroy()
        ventana_Bienvenida.deiconify()

    def consultar_ventas():

        fecha = simpledialog.askstring("Fecha", "Ingresa la fecha (YYYY-MM-DD):", parent=Ventana)



        if fecha:
            try:
                conexion = mysql.connector.connect(
                    host="127.0.0.1",
                    user="root",
                    password="",
                    database="Tomas_pizza",
                    port="3306"
                )
                cursor = conexion.cursor()

                # consultas de cierre de ventas por pago en efectivo y transferencia

                consulta_ventas = """
                   SELECT 
                      COUNT(*), 
                      SUM(total_general),
                      COUNT(CASE WHEN modo_pago = 'efectivo' THEN 1 END) AS ventas_efectivo,
                      SUM(CASE WHEN modo_pago = 'efectivo' THEN total_general ELSE 0 END) AS total_efectivo,
                      COUNT(CASE WHEN modo_pago = 'transferencia' THEN 1 END) AS ventas_transferencia,
                      SUM(CASE WHEN modo_pago = 'transferencia' THEN total_general ELSE 0 END) AS total_transferencia
                 FROM ventas 
                 WHERE DATE(fecha) = %s

                """
                cursor.execute(consulta_ventas, (fecha,))
                resultado = cursor.fetchone()

                cantidad_ventas = resultado[0] if resultado else 0
                total_ventas = resultado[1] if resultado[1] is not None else 0.0
                ventas_efectivo = resultado[2] if resultado[2] is not None else 0.0
                total_efectivo = resultado[3] if resultado[3] is not None else 0.0
                ventas_transferencia = resultado[4] if resultado[4] is not None else 0.0
                total_transferencia = resultado[5] if resultado[5] is not None else 0.0

                etiqueta_resultado.config(

                    text=(
                        f"Ventas en {fecha}: {cantidad_ventas}\n"
                        f"Total_general: ${total_ventas:.2f}\n"
                        f"Ventas por Efectivo: {ventas_efectivo} (Total: ${total_efectivo:.2f})\n"
                        f"Ventas por transferencia: {ventas_transferencia} (Total: ${total_transferencia:.2f})"

                    )
                )

                def Guardar_cierre():

                    try:
                        if total_ventas == 0 or total_efectivo < 0 or total_transferencia < 0:
                            messagebox.showwarning("Datos invalidos", " Datos incorrectos, revisa fechas y valores.")
                            return

                        confirmacion = messagebox.askyesno("confirmar cierre", " ¿Estas seguro de realizar el Cierre?")
                        if not confirmacion:
                            return

                        hora_actual = datetime.now().strftime("%H:%M:%S")

                        conexion = mysql.connector.connect(

                            host="127.0.0.1",
                            user="root",
                            password="",
                            database="Tomas_pizza",
                            port="3306"
                        )

                        cursor = conexion.cursor()

                        # incertar los datos en la tabla cierre Mysql

                        consulta_verificar = "SELECT COUNT(*) FROM cierre WHERE Ventas_fecha = %s"
                        cursor.execute(consulta_verificar, (fecha,))
                        resultado_verificacion = cursor.fetchone()

                        if resultado_verificacion[0] > 0:
                            messagebox.showwarning("Cierre duplicado", "Este cierre ya esta registrado")
                        else:
                            consulta_insert = """INSERT INTO cierre (Ventas_fecha, Total_general, Ventas_Efectivo, Ventas_transferencia) VALUES (%s, %s, %s, %s)"""
                            cursor.execute(consulta_insert, (fecha, total_ventas, total_efectivo, total_transferencia))
                            conexion.commit()
                            messagebox.showinfo("Cierre guardado", "El cierre esta guardado en la base de datos.")

                            boton_registrar_pedido.config(state="disabled")

                        conexion.close()

                    except mysql.connector.Error as err:
                        messagebox.showerror("Error al guardar cierre",
                                             f"Error al guardar el cierre en la base de datos: {err}")

                boton_guardar_cierre.config(command=Guardar_cierre)

                conexion.close()

            except mysql.connector.Error as err:
                messagebox.showerror("Error en la base de datos", f"Error al consultar la base de datos: {err}")
        else:
            messagebox.showwarning("Fecha inválida", "Por favor, ingresa una fecha válida.")

    def verificar_estado_boton():
        try:
            conexion = mysql.connector.connect(
                host="127.0.0.1",
                user="root",
                password="",
                database="Tomas_pizza",
                port="3306"
            )
            cursor = conexion.cursor()

            consulta = "SELECT MAX(Ventas_fecha) FROM cierre"
            cursor.execute(consulta)
            resultado = cursor.fetchone()
            ultima_fecha_cierre = resultado[0]


            fecha_actual = date.today().strftime("%Y-%m-%d")

            if ultima_fecha_cierre is None or str(ultima_fecha_cierre) < fecha_actual:
                boton_registrar_pedido.config(state="normal")

            conexion.close()

        except  mysql.connector.Error as err:
            messagebox.showerror("Error", f"No se puede verificar el estado del boton: {err}")

    verificar_estado_boton()

    # Botón para seleccionar la fecha
    boton_fecha = tk.Button(Ventana, text="CONSULTAR FECHA", command=consultar_ventas)
    boton_fecha.configure(fg="black", bg="#FDF5E6", font=("Open Sans", 10), width=15)
    boton_fecha.place(x=55, y=100)

    etiqueta_resultado = tk.Label(Ventana, text="RESULTADO", font=("Open Sans", 10), fg="black", bg="#FDF5E6")
    etiqueta_resultado.place(x=100, y=230)

    boton_guardar_cierre = tk.Button(Ventana, text="GUARDAR CIERRE")
    boton_guardar_cierre.configure(fg="black", bg="#FDF5E6", font=("Open Sans", 10), width=15)
    boton_guardar_cierre.place(x=180, y=380)

    def cambiar_color_hover(boton):
        boton.config(bg="gray")

    def restaurar_color(boton):
        boton.config(bg="#FDF5E6")

    boton_fecha.bind("<Enter>", lambda event: cambiar_color_hover(boton_fecha))
    boton_fecha.bind("<Leave>", lambda event: restaurar_color(boton_fecha))

    boton_guardar_cierre.bind("<Enter>", lambda event: cambiar_color_hover(boton_guardar_cierre))
    boton_guardar_cierre.bind("<Leave>", lambda event: restaurar_color(boton_guardar_cierre))

    # Boton limpiar consulta

    def limpiar_consulta():
        etiqueta_resultado.config(text="RESULTADO")

    boton_limpiar = tk.Button(Ventana, text="LIMPIAR CONSULTA", command=limpiar_consulta)
    boton_limpiar.configure(fg="black", bg="#FDF5E6", font=("Open Sans", 10), width=15)
    boton_limpiar.place(x=180, y=420)

    volver = tk.Button(Ventana, text="VOLVER", command=volver)
    volver.config(fg="black", bg="#FDF5E6", font=("Open Sans", 10), width=15)
    volver.place(x=180, y=460)

    def cambiar_color_hover(boton):
        boton.config(bg="gray")

    def restaurar_color(boton):
        boton.config(bg="#FDF5E6")

    boton_limpiar.bind("<Enter>", lambda event: cambiar_color_hover(boton_limpiar))
    boton_limpiar.bind("<Leave>", lambda event: restaurar_color(boton_limpiar))

    volver.bind("<Enter>", lambda event: cambiar_color_hover(volver))
    volver.bind("<Leave>", lambda event: restaurar_color(volver))

    Ventana.iconbitmap(
        r"C:\Users\Diego Zamora\OneDrive\Documentos\Adsi 2024\repositorio\Tomas-pizza\recursos\logoico.ico")

    Ventana.mainloop()