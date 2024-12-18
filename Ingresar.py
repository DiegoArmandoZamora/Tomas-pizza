import tkinter as tk
from tkinter import ttk
from tkinter import *
from Bienvenida import abrir_bienvenida
import bcrypt
import messagebox
import mysql.connector
from PIL import Image, ImageTk
import Bienvenida


# conexion base de datos

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
        messagebox.showerror("Error de coneccion",f"Error:{err}")
        return None

    # verificacion de usuario Administrador de contaseñas

def verificar_usuario(username,password):
    try:
        db = conectar_db()
        if db:
            cursor = db.cursor(dictionary=True)
            query = "SELECT * FROM usuarios WHERE usuario = %s AND contraseña = %s"
            cursor.execute(query,(username,password))
            result = cursor.fetchone()
            db.close()

            if result:
                return result
            else:
                return None

    except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error al validar credenciales: {err}")
    return None

# limpiar registro de usuario

def login():
    username = user_entry.get()
    password = password_entry.get()

    if username == "" or password == "":
        error_label.config(text="Por favor, ingrese usuario y contraseña", fg="red")
    else:
        usuario = verificar_usuario(username, password)
        if usuario:
            user_entry.delete(0,tk.END)
            password_entry.delete(0,tk.END)
            ventana.withdraw()
            abrir_bienvenida(ventana,usuario)
        else:
            error_label.config(text="Usuario o contraseña incorrectos", fg="red")

# Ventana
ventana = tk.Tk()
ventana.title("Ingreso al sistema")
ventana.geometry(f"500x600+400+50")
ventana.config(bg="#FDF5E6")
ventana.resizable(False, False)

# Crear un marco para el formulario de login1
frame_login = tk.Frame(ventana, padx=20, pady=20)
frame_login.pack(side="right", expand=True, fill="both")
frame_login.place(x=160, y=180)
frame_login.config(bg="#FDF5E6")

# Usuario
user_label = tk.Label(frame_login, text="USUARIO", font=("Open Sans", 10))
user_label.place(x=160, y=150)
user_label.config(bg="#FDF5E6")
user_label.pack()

# Cuadro usuario
user_entry = ttk.Entry(frame_login, font=("Open Sans", 12), width=15)
user_entry.pack(pady=5)

# Contraseña
password_label = tk.Label(frame_login, text="CONTRASEÑA", font=("Open", 10))
password_label.place(x=200, y=150)
password_label.config(bg="#FDF5E6")
password_label.pack()

# Cuadro contraseña
password_entry = ttk.Entry(frame_login, font=("Open Sans", 12), width=15, show="*")
password_entry.pack(pady=5)

# Boton ingresar
botoni = tk.Button(text="INGRESAR", command=login)
botoni.place(x=200, y=320)
botoni.config(width=12, bg="#FDF5E6")

label = Label(ventana, text="INGRESE AQUI SUS DATOS", background="#FDF5E6", font=("Open Sans", 20, 'bold'),
              fg="#f5402e",
              bg="#FDF5E6")
label.pack()
label.place(x=70, y=110)

# Mensaje de error
error_label = tk.Label(ventana, text="", font=("Open Sans", 10))
error_label.config(bg="#FDF5E6")
error_label.pack(pady=(5, 0))
error_label.place(x=150, y=380)

redes = Label(ventana, text="Encuéntranos en nuestras redes sociales", background="#FDF5E6", font=("Open Sans", 13),
              fg="black", bg="#FDF5E6")
redes.pack()
redes.place(x=106, y=430)

# Agregar iconos de redes sociales en formato .ico y ajustar el tamaño
facebook_icon = Image.open(r"C:\Users\Diego Zamora\OneDrive\Documentos\Adsi 2024\repositorio\Tomas-pizza\recursos\facebook.ico").resize((30, 30))
x_icon = Image.open(r"C:\Users\Diego Zamora\OneDrive\Documentos\Adsi 2024\repositorio\Tomas-pizza\recursos\twitter.ico").resize((30, 30))
instagram_icon = Image.open(r"C:\Users\Diego Zamora\OneDrive\Documentos\Adsi 2024\repositorio\Tomas-pizza\recursos\instagram.ico").resize((30, 30))

facebook_icon = ImageTk.PhotoImage(facebook_icon)
x_icon = ImageTk.PhotoImage(x_icon)
instagram_icon = ImageTk.PhotoImage(instagram_icon)

icon_frame = tk.Frame(ventana, bg="#FDF5E6")
icon_frame.pack()
icon_frame.place(x=170, y=470)

facebook_label = tk.Label(icon_frame, image=facebook_icon, bg="#FDF5E6")
facebook_label.grid(row=0, column=0, padx=10)

x_label = tk.Label(icon_frame, image=x_icon, bg="#FDF5E6")
x_label.grid(row=0, column=1, padx=10)

instagram_label = tk.Label(icon_frame, image=instagram_icon, bg="#FDF5E6")
instagram_label.grid(row=0, column=2, padx=10)

ventana.iconbitmap(r"C:\Users\Diego Zamora\OneDrive\Documentos\Adsi 2024\repositorio\Tomas-pizza\recursos\logoico.ico")
ventana.mainloop()
