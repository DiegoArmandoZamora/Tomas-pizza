import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox
import mysql.connector

def abrir_cierre_caja(ventana_Bienvenida):
    Ventana = tk.Toplevel(ventana_Bienvenida)
    Ventana.title("Ventana Tomas")
    Ventana.geometry(f"470x600+400+50")
    Ventana.configure(bg="#FDF5E6")
    Ventana.resizable(False, False)

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
                total_efectivo = resultado[3] if resultado [3] is not None else 0.0
                ventas_transferencia = resultado [4] if resultado [4] is not None else 0.0
                total_transferencia =resultado [5] if resultado [5] is not None else 0.0

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
                        conexion = mysql.connector.connect(

                           host = "127.0.0.1",
                           user = "root",
                           password = "",
                           database = "Tomas_pizza",
                           port = "3306"
                        )

                        cursor = conexion.cursor()

# incertar los datos en la tabla cierre

                        consulta_insert = """INSERT INTO cierre (Ventas_fecha, Total_general, Ventas_Efectivo, Ventas_transferencia) VALUES (%s,%s,%s,%s)"""

                        cursor.execute(consulta_insert, (fecha, total_ventas, total_efectivo, total_transferencia))
                        conexion.commit()

                        messagebox.showinfo("Cierre guardado", "El cierre  esta guardado en la base de datos")
                        conexion.close()

                    except mysql.connector.Error as err:
                        messagebox.showerror("Error al guardar cierre", f"Error al guardar el cierre en la base de datos: {err}")

                boton_guardar_cierre.config(command=Guardar_cierre)

                conexion.close()

            except mysql.connector.Error as err:
                messagebox.showerror("Error en la base de datos", f"Error al consultar la base de datos: {err}")
        else:
            messagebox.showwarning("Fecha inválida", "Por favor, ingresa una fecha válida.")


    # Botón para seleccionar la fecha
    boton_fecha = tk.Button(Ventana, text="INGRESA FECHA", command=consultar_ventas)
    boton_fecha.configure(fg="black", bg="#a6a6a6", font=("Open Sans", 10), width=15)
    boton_fecha.place(x=55, y=100)

    etiqueta_resultado = tk.Label(Ventana, text="RESULTADO", font=("Open Sans", 10), fg="black", bg="#FDF5E6")
    etiqueta_resultado.place(x=100, y=230)

    boton_guardar_cierre = tk.Button(Ventana, text="GUARDAR CIERRE")
    boton_guardar_cierre.configure(fg="black", bg="#a6a6a6", font=("Open Sans", 10), width=14)
    boton_guardar_cierre.place(x=180, y=380)

    volver = tk.Button(Ventana, text="VOLVER", command=volver)
    volver.config(fg="black", bg="#a6a6a6", font=("Open Sans", 10), width=14)
    volver.place(x=180, y=420)

    Ventana.iconbitmap(r"C:\Users\Diego Zamora\OneDrive\Documentos\Adsi 2024\repositorio\Tomas-pizza\recursos\logoico.ico")

    Ventana.mainloop()
