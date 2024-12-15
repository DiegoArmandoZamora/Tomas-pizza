import tkinter
import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector
import TomaPedido
import CierreCaja
import CompararFechas
import Gastos


# Conexión a la base de datos
def conectar_db():
    try:
        conexion = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",
            database="Tomas_pizza",
            port="3306"
        )
        return conexion
    except mysql.connector.Error as err:
        messagebox.showerror("Error de conexión", f"Error: {err}")
        return None

    # Función para verificar si el usuario existe en la base de datos
def user_exists(username):
        try:
            db = conectar_db()
            cursor = db.cursor()
            query = "SELECT * FROM usuarios WHERE usuario = %s"
            cursor.execute(query, (username,))
            result = cursor.fetchone()
            db.close()

            if result:
                return True
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        return False

    # Función para registrar un nuevo usuario
def open_register_window(Bienvenida):
        register_windows = Toplevel(Bienvenida)
        register_windows.title("Crear Nuevo Usuario")
        register_windows.geometry("400x300")

        username_label = tk.Label(register_windows, text="Usuario")
        username_label.pack(pady=10)
        username_entry = ttk.Entry(register_windows, font=("Open Sans", 12), width=20)
        username_entry.pack(pady=10)

        password_label = tk.Label(register_windows, text="Contraseña")
        password_label.pack(pady=10)
        password_entry = ttk.Entry(register_windows, font=("Open Sans", 12), width=20, show="*")
        password_entry.pack(pady=10)

        def save_user():
            username = username_entry.get()
            password = password_entry.get()

            if username == "" or password == "":
                messagebox.showerror("Error", "Debe Ingresar un Usuario y una Contraseña")
                return

            if not user_exists(username):
                try:
                    db = conectar_db()
                    cursor = db.cursor()
                    query = "INSERT INTO usuarios (usuario, contraseña) VALUES (%s, %s)"
                    cursor.execute(query, (username, password))
                    db.commit()
                    db.close()

                    messagebox.showinfo("Éxito", "Usuario creado exitosamente")
                    register_windows.destroy()
                except mysql.connector.Error as err:
                    messagebox.showerror("Error", f"Error: {err}")
            else:
                messagebox.showerror("Error", "El Usuario ya está Registrado")

        save_button = tk.Button(register_windows, text="Registrar", command=save_user)
        save_button.pack(pady=20)


    # Función para eliminar un usuario
def delete_user(Bienvenida):
        delete_window = Toplevel(Bienvenida)
        delete_window.title("Eliminar Usuario")
        delete_window.geometry("400x200")

        username_label = tk.Label(delete_window, text="Nombre de Usuario")
        username_label.pack(pady=10)
        username_entry = ttk.Entry(delete_window, font=("Open Sans", 12), width=20)
        username_entry.pack(pady=10)

        def confirm_delete():
            username = username_entry.get()

            if username == "":
                messagebox.showerror("Error", "Debe Ingresar un nombre de Usuario")
                return

            try:
                db = conectar_db()
                cursor = db.cursor()
                query = "DELETE FROM usuarios WHERE usuario = %s"
                cursor.execute(query, (username,))
                db.commit()

                if cursor.rowcount > 0:
                    messagebox.showinfo("Éxito", "Usuario eliminado exitosamente")
                else:
                    messagebox.showwarning("Advertencia", "El Usuario No Existe")

                db.close()
                delete_window.destroy()
            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Error al eliminar el usuario: {err}")

        delete_button = tk.Button(delete_window, text="Eliminar Usuario", command=confirm_delete)
        delete_button.pack(pady=20)


def abrir_bienvenida(ventana_login,usuario):
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

    # boton de salida de Bienvenida
    def salir():
        Bienvenida.destroy()
        ventana_login.deiconify()

    boton_salir = tkinter.Button(Bienvenida,text="SALIR", command=salir)
    boton_salir.place(x=190,y=500)
    boton_salir.config(width=15,bg="#FDF5E6")



# validacion si es Administrador

    if usuario and usuario.get('es_administrador',True):
        boton_registrar = tk.Button(Bienvenida, text="CREAR USUARIO", command=lambda: open_register_window(Bienvenida))
        boton_registrar.place(x=190, y=400)
        boton_registrar.config(width=15, bg="#FDF5E6")

        boton_eliminar = tk.Button(Bienvenida, text="ELIMINAR USUARIO", command=lambda: delete_user(Bienvenida))
        boton_eliminar.place(x=190, y=450)
        boton_eliminar.config(width=15, bg="#FDF5E6")


    Bienvenida.iconbitmap(r"C:\Users\Diego Zamora\OneDrive\Documentos\Adsi 2024\repositorio\Tomas-pizza\recursos\logoico.ico")

    Bienvenida.mainloop()
