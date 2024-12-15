import tkinter as tk
import os
from tkinter import filedialog,messagebox
from time import strftime
import mysql.connector

contador_impresiones = 0

def conectar_db():
    return mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="Tomas_pizza",
        port = "3306"

    )

#coneccion a la base de datos
def guardar_en_bd(modo_pago,total_general,vegetariana,carnes,peperoni,pollo,bbq,bebidas,boton):
    try:
        conn = conectar_db()
        cursor = conn.cursor()
        query ="INSERT INTO ventas (modo_pago,total_general,vegetariana,carnes,peperoni,pollo,bbq,bebidas)VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
        datos = (modo_pago,total_general,vegetariana,carnes,peperoni,pollo,bbq,bebidas)
        cursor.execute(query,datos)
        conn.commit()
        cursor.close()

        print("Datos ingresados a la base de Datos.")
        boton.config(state=tk.DISABLED)
        messagebox.showinfo("Pago Realizado","El Pago Se Realizo Exitosamente")
    except mysql.connector.Error as err:
        print(f"Error:{err}")
        messagebox.showerror("Error", f"Hubo Un Error Al Guarar Los Datos:{err}")


def generar_factura(ventana, modo_pago, total_general, vegetariana, carnes, peperoni, pollo, bbq, bebidas):
    global contador_impresiones
    contador_impresiones += 1


    factura = f"Factura de Venta\n\n"
    factura += f"Fecha: {strftime('%Y-%m-%d')}\n"
    factura += f"Hora: {strftime('%H:%M:%p')}\n"
    factura += f"Forma de pago: {modo_pago}\n\n"

    if vegetariana > 0:
        factura += f"VEGETARIANA: {vegetariana}\n"
    if carnes > 0:
        factura += f"CARNES: {carnes}\n"
    if peperoni > 0:
        factura += f"PEPERONI: {peperoni}\n"
    if pollo > 0:
        factura += f"POLLO: {pollo}\n"
    if bbq > 0:
        factura += f"BBQ: {bbq}\n"
    if bebidas > 0:
        factura += f"BEBIDAS: {bebidas}\n"

    factura += f"\nTotal: ${total_general:.2f}\n"

    # Imprimir directamente la factura directamente a la impresora
    try:
        archivo_temporal = "temp_factura.txt"
        with open(archivo_temporal, 'w') as f:
            f.write(factura)
        os.system(f'notepad.exe /p "{archivo_temporal}"')
        messagebox.showinfo("Factura Impresa", "La Factura se esta Imprimiendo.")
        os.remove(archivo_temporal)
    except Exception as e:
        messagebox.showinfo("Error al Imprimir", "Impresora no encontrada revise coneccion")



def abrirCierreVentas(ventana_pago_pedido, modo_pago, total_general, vegetariana, carnes, peperoni, pollo, bbq, bebidas):
    Ventana = tk.Toplevel(ventana_pago_pedido)
    Ventana.title("ventana Tomas")
    Ventana.geometry(f"520x600+400+50")
    Ventana.configure(bg="#FDF5E6")
    Ventana.resizable(False, False)

    Ventana.title()
    etiqueta_total = tk.Label(Ventana, text="CIERRE DE VENTAS")
    etiqueta_total.config(fg="red", bg="#FDF5E6", font=("Open Sans", 20, "bold"))
    etiqueta_total.pack()


    def volver():
        Ventana.destroy()
        ventana_pago_pedido.deiconify()


# FECHA Y HORA


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

    y_pos = 250
    if vegetariana > 0:
        etiqueta_vegetariana = tk.Label(Ventana, text=f"VEGETARIANA: {vegetariana}")
        etiqueta_vegetariana.configure(fg="black", bg="#FDF5E6", font=("Open Sans", 10))
        etiqueta_vegetariana.place(x=50, y=y_pos)
        y_pos += 20

    if carnes > 0:
        etiqueta_vegetariana = tk.Label(Ventana, text=f"CARNES: {carnes}")
        etiqueta_vegetariana.configure(fg="black", bg="#FDF5E6", font=("Open Sans", 10))
        etiqueta_vegetariana.place(x=50, y=y_pos)
        y_pos += 20

    if peperoni > 0:
        etiqueta_vegetariana = tk.Label(Ventana, text=f"PEPERONI: {peperoni}")
        etiqueta_vegetariana.configure(fg="black", bg="#FDF5E6", font=("Open Sans", 10))
        etiqueta_vegetariana.place(x=50, y=y_pos)
        y_pos += 20

    if pollo > 0:
        etiqueta_vegetariana = tk.Label(Ventana, text=f"POLLO: {pollo}")
        etiqueta_vegetariana.configure(fg="black", bg="#FDF5E6", font=("Open Sans", 10))
        etiqueta_vegetariana.place(x=50, y=y_pos)
        y_pos += 20

    if bbq > 0:
        etiqueta_vegetariana = tk.Label(Ventana, text=f"BBQ: {bbq}")
        etiqueta_vegetariana.configure(fg="black", bg="#FDF5E6", font=("Open Sans", 10))
        etiqueta_vegetariana.place(x=50, y=y_pos)
        y_pos += 20

    if bebidas > 0:
        etiqueta_vegetariana = tk.Label(Ventana, text=f"BEBIDAS: {bebidas}")
        etiqueta_vegetariana.configure(fg="black", bg="#FDF5E6", font=("Open Sans", 10))
        etiqueta_vegetariana.place(x=50, y=y_pos)
        y_pos += 20


    Ventana.title()

    etiqueta_total = tk.Label(Ventana, text="FORMA DE PAGO")
    etiqueta_total.config(fg="red", bg="#FDF5E6", font=("Open Sans", 15, "bold"))
    etiqueta_total.place(x=50, y=98)

    #Etiqueta valor pago y valor total

    Ventana.title()
    etiqueta_pago = tk.Label(Ventana, text="VALOR TOTAL")
    etiqueta_pago.config(fg="red", bg="#FDF5E6", font=("Open Sans", 15, "bold"))
    etiqueta_pago.place(x=330, y=98)

# etiqueta  forma de pago
    etiqueta_forma_pago = tk.Label(Ventana, text=f"FORMA DE PAGO: {modo_pago}")
    etiqueta_forma_pago.config(fg="black", bg="#FDF5E6", font=("Open Sans", 13, "bold"))
    etiqueta_forma_pago.place(x=50, y=150)

# Etiqueta validacion forma de pago
    etiqueta_pago_seleccionado = tk.Label(Ventana, text=f"{modo_pago}:")
    etiqueta_pago_seleccionado.configure(fg="black", bg="#FDF5E6", font=("Open Sans", 13, "bold"))
    etiqueta_pago_seleccionado.place(x=53, y=200)

  # etiqueta total de la Compra
    etiqueta_valor_total = tk.Label(Ventana, text=f"${total_general}")
    etiqueta_valor_total.configure(fg="black", bg="#FDF5E6", font=("Open Sans", 13, "bold"))
    etiqueta_valor_total.place(x=350, y=200)


    boton_precio = tk.Button(Ventana, text="REALIZAR PAGO", font=("Open Sans", 10), bg="#a6a6a6", width=15,command=lambda: guardar_en_bd(modo_pago,total_general,vegetariana,carnes,peperoni,pollo,bbq,bebidas,boton_precio))
    boton_precio.place(x=210, y=400)

    boton_cierre = tk.Button(Ventana, text="IMPRIMIR FACTURA",command=lambda: generar_factura(Ventana, modo_pago, total_general, vegetariana, carnes,peperoni, pollo, bbq, bebidas))
    boton_cierre.configure(fg="black", bg="#a6a6a6", font=("Open Sans", 10), width=15)
    boton_cierre.place(x=210, y=450)

    volver = tk.Button(Ventana, text="VOLVER", command=volver)
    volver.configure(fg="black", bg="#a6a6a6", font=("Open Sans", 10), width=15)
    volver.place(x=210, y=500)


    Ventana.iconbitmap(r"C:\Users\Diego Zamora\OneDrive\Documentos\Adsi 2024\repositorio\Tomas-pizza\recursos\logoico.ico")
    Ventana.mainloop()