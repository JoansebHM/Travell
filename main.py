import tkinter as tk

def mostrar_campos_creacion_usuario():
    label_nombre.grid(row=1, column=0, padx=10, pady=5)
    entry_nombre.grid(row=1, column=1, padx=10, pady=5)
    label_edad.grid(row=2, column=0, padx=10, pady=5)
    entry_edad.grid(row=2, column=1, padx=10, pady=5)
    label_email.grid(row=3, column=0, padx=10, pady=5)
    entry_email.grid(row=3, column=1, padx=10, pady=5)
    button_agregar.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

def ocultar_campos_creacion_usuario():
    label_nombre.grid_forget()
    entry_nombre.grid_forget()
    label_edad.grid_forget()
    entry_edad.grid_forget()
    label_email.grid_forget()
    entry_email.grid_forget()
    button_agregar.grid_forget()

root = tk.Tk()
root.title("Crear Usuario")

# Crear los widgets para la creación de usuario
label_nombre = tk.Label(root, text="Nombre:")
entry_nombre = tk.Entry(root)

label_edad = tk.Label(root, text="Edad:")
entry_edad = tk.Entry(root)

label_email = tk.Label(root, text="Email:")
entry_email = tk.Entry(root)

button_mostrar_campos = tk.Button(root, text="Crear Usuario", command=mostrar_campos_creacion_usuario)
button_agregar = tk.Button(root, text="Agregar", command=ocultar_campos_creacion_usuario)

# Organizar el botón en la ventana
button_mostrar_campos.grid(row=0, column=0, padx=10, pady=5)

# Mostrar la ventana
root.mainloop()
