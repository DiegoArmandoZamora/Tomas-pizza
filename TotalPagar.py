import tkinter as tk
import random
import CierreVentas

contador_pedidos = 0


def abrirPagoPedido(ventana_Pedido,vegetariana, carnes, peperoni, pollo, bbq, bebidas, numero_pedido):
    Ventana = tk.Toplevel(ventana_Pedido)
    Ventana.title("ventana Tomas")
    Ventana.geometry(f"800x600+270+50")
    Ventana.configure(bg="#FDF5E6")
    Ventana.resizable(False, False)


# Numero de pedido

    etiqueta_numero_pedido = tk.Label(Ventana, text=f"NUMERO DE PEDIDO: {numero_pedido}")
    etiqueta_numero_pedido.configure(fg="black", bg="#FDF5E6", font=("Open Sans", 12))
    etiqueta_numero_pedido.place(x=55, y=260)

   # Ventana.title()
    etiqueta_total = tk.Label(Ventana, text="TOTAL A PAGAR")
    etiqueta_total.config(fg="#f5402e", bg="#FDF5E6", font=("Open Sans", 20, "bold"))
    etiqueta_total.pack()

    def cierreVentas():
        Ventana.withdraw()
        CierreVentas.abrirCierreVentas(Ventana, pago, total_general,vegetariana, carnes, peperoni, pollo, bbq, bebidas)

    def volver():
        Ventana.destroy()
        ventana_Pedido.deiconify()

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

    Ventana.title()
    etiqueta_pedido = tk.Label(Ventana, text="PEDIDO SOLICITADO")
    etiqueta_pedido.config(fg="#f5402e", bg="#FDF5E6", font=("Open Sans", 15, "bold"))
    etiqueta_pedido.place(x=50, y=100)

    Ventana.title()
    etiqueta_pagar = tk.Label(Ventana, text="TOTAL PRODUCTOS")
    etiqueta_pagar.config(fg="#f5402e", bg="#FDF5E6", font=("Open Sans", 15, "bold"))
    etiqueta_pagar.place(x=550, y=100)

    Ventana.title()
    etiqueta1 = tk.Label(Ventana, text="UNIDADES")
    etiqueta1.config(fg="#f5402e", bg="#FDF5E6", font=("Open Sans", 15, "bold"))
    etiqueta1.place(x=120, y=700)

    # etiqueta de unidades
    y_pos = 140
    if vegetariana > 0:
        etiqueta_cantidad = tk.Label(Ventana, text=f"PIZZAS VEGETARIANAS: {vegetariana}")
        etiqueta_cantidad.configure(fg="black", bg="#FDF5E6", font=("Open Sans", 10))
        etiqueta_cantidad.place(x=300, y=y_pos)
        y_pos += 20

    if peperoni > 0:
        etiqueta_peperoni = tk.Label(Ventana, text=f"PIZZAS PEPERONI: {peperoni}")
        etiqueta_peperoni.configure(fg="black", bg="#FDF5E6", font=("Open Sans", 10))
        etiqueta_peperoni.place(x=300, y=y_pos)
        y_pos += 20

    if pollo > 0:
        etiqueta_pollo = tk.Label(Ventana, text=f"PIZZAS DE POLLO: {pollo}")
        etiqueta_pollo.configure(fg="black", bg="#FDF5E6", font=("Open Sans", 10))
        etiqueta_pollo.place(x=300, y=y_pos)
        y_pos += 20


    if carnes > 0:
        etiqueta_carnes = tk.Label(Ventana, text=f"PIZZAS DE CARNES: {carnes}")
        etiqueta_carnes.configure(fg="black", bg="#FDF5E6", font=("Open Sans", 10))
        etiqueta_carnes.place(x=300, y=y_pos)
        y_pos += 20


    if bbq > 0:
        etiqueta_bbq = tk.Label(Ventana, text=f"PIZZAS BBQ: {bbq}")
        etiqueta_bbq.configure(fg="black", bg="#FDF5E6", font=("Open Sans", 10))
        etiqueta_bbq.place(x=300, y=y_pos)
        y_pos += 20


    # etiqueta de unidades bebidas
    if bebidas > 0:
        etiqueta_bebidas = tk.Label(Ventana, text=f"CANTIDAD DE BEBIDAS: {bebidas}")
        etiqueta_bebidas.configure(fg="black", bg="#FDF5E6", font=("Open Sans", 10))
        etiqueta_bebidas.place(x=300, y=y_pos)
        y_pos += 20


    # etiqueta de cantidad pizas
    etiqueta_cantidad = tk.Label(Ventana, text="CANTIDAD DE PIZZAS: ")
    etiqueta_cantidad.configure(fg="black", bg="#FDF5E6", font=("Open Sans", 10))
    etiqueta_cantidad.place(x=55, y=180)

    # etiqueta numero de pedido
    etiqueta_pedido = tk.Label(Ventana, text="NUMERO DE PEDIDO: ")
    etiqueta_pedido.configure(fg="black", bg="#FDF5E6", font=("Open Sans", 10))
    etiqueta_pedido.place(x=55, y=340)


    precio_pizza = 25000
    precio_bebida = 3000

    total_pizzas = (vegetariana + carnes + peperoni + pollo + bbq) * precio_pizza
    total_bebidas = bebidas * precio_bebida

    total_general = total_pizzas * precio_bebida


    etiqueta_total_pizas = tk.Label(Ventana, text=f"PRECIO PIZZAS: {total_pizzas}")
    etiqueta_total_pizas.configure(fg="black", bg="#FDF5E6", font=("Open Sans", 10))
    etiqueta_total_pizas.place(x=550, y=170)

    etiqueta_total_bebidas = tk.Label(Ventana, text=f"PRECIO BEBIDAS: {total_bebidas}")
    etiqueta_total_bebidas.configure(fg="black", bg="#FDF5E6", font=("Open Sans", 10))
    etiqueta_total_bebidas.place(x=550, y=230)


    def desplegar_pagos():
        pagos_menu.post(boton_pagos.winfo_rootx(), boton_pagos.winfo_rooty() + boton_pagos.winfo_height())

    def seleccionar_pago(pago):
        etiqueta_pago.config(text=f"PEDIDO PAGADO CON: {pago}", font=("Open Sans", 10))
        etiqueta_pago.place(x=58, y=400)

        CierreVentas.abrirCierreVentas(Ventana, pago, total_general, vegetariana, carnes, peperoni, pollo, bbq, bebidas)

    etiqueta_pago = tk.Label(Ventana, text="")
    etiqueta_pago.configure(fg="black", bg="#FDF5E6", font=("Open Sans", 10))
    etiqueta_pago.place(x=58, y=430)

    boton_pagos = tk.Button(Ventana, text="FORMA DE PAGO", command=desplegar_pagos)
    boton_pagos.configure(fg="black", bg="#a6a6a6", font=("Open Sans", 10))
    boton_pagos.place(x=60, y=400)

    pagos_menu = tk.Menu(Ventana, tearoff=0)
    pagos = ["EFECTIVO", "TRANSFERENCIA"]
    for pago in pagos: pagos_menu.add_command(label=pago, command=lambda p=pago: seleccionar_pago(p))

    # precio total
    total_general = total_pizzas + total_bebidas
    etiqueta_precio_total = tk.Label(Ventana, text=f"PRECIO TOTAL: {total_general}")
    etiqueta_precio_total.configure(fg="black", bg="#FDF5E6", font=("Open sans", 10))
    etiqueta_precio_total.place(x=600, y=300)

    etiqueta_total = tk.Label(Ventana, text="PRECIO TOTAL: ")
    etiqueta_total.configure(fg="black", bg="#FDF5E6", font=("Open Sans", 10))
    etiqueta_total.place(x=550, y=300)


    boton_precio = tk.Button(Ventana, text="REALIZAR PAGO", command=cierreVentas, width=15, height=1, bg="#a6a6a6",
                             font=("Open Sans", 10))
    boton_precio.place(x=350, y=400)

    volver = tk.Button(Ventana, text="VOLVER", command=volver)
    volver.configure(fg="black", bg="#a6a6a6", font=("Open Sans", 10), width=15)
    volver.place(x=350, y=450)

    Ventana.iconbitmap(r"C:\Users\Diego Zamora\OneDrive\Documentos\Adsi 2024\interface grafica\recursos\logoico.ico")

    Ventana.mainloop()