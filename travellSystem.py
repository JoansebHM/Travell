import tkinter as tk

pasajeros = []
ciudades = []

def clean_cells():
    label_nombre.grid_forget()
    entry_nombre.grid_forget()
    label_cedula.grid_forget()
    entry_cedula.grid_forget()
    label_ciudad.grid_forget()
    entry_ciudad.grid_forget()
    label_ciudad_nueva.grid_forget()
    entry_ciudad_nueva.grid_forget()
    label_pais.grid_forget()
    entry_pais.grid_forget()
    entry_nombre.delete(0, tk.END)
    entry_cedula.delete(0, tk.END)
    entry_ciudad.delete(0, tk.END)
    entry_ciudad_nueva.delete(0, tk.END)
    entry_pais.delete(0, tk.END)

def agregar_pasajero():
    clean_cells()
    label_nombre.grid(row=0,column=3)
    entry_nombre.grid(row=0, column=4)
    label_cedula.grid(row=1, column=3)
    entry_cedula.grid(row=1, column=4)
    label_ciudad.grid(row=2, column=3)
    entry_ciudad.grid(row=2, column=4)
    try:
        nombre = entry_nombre.get()
        cedula = int(entry_cedula.get())
        ciudad = entry_ciudad.get()
        tupla_pasajeros = (nombre, cedula, ciudad)
        pasajeros.append(tupla_pasajeros)
        listbox_pasajeros.insert(tk.END, f"{nombre} - {cedula} - {ciudad}")
        clean_cells()
    except ValueError:
        pass

def agregar_ciudad():
  label_ciudad_nueva.grid(row=0, column=3)
  entry_ciudad_nueva.grid(row=0, column=4)
  label_pais.grid(row=1, column=3)
  entry_pais.grid(row=1, column=4)

  try:
    ciudad = entry_ciudad_nueva.get()
    pais = entry_pais.get()
    tupla_ciudades = (ciudad, pais)
    ciudades.append(tupla_ciudades)
    listbox_ciudades.insert(tk.END, f"{ciudad} - {pais}")
    # Call clean_cells to clear entry fields after adding city
    clean_cells()
  except ValueError:
    pass





def update_listbox_ciudades():
    for ciudad, pais in ciudades:
        listbox_ciudades.insert(tk.END, f"{ciudad} - {pais}")

def destino_pasajero():
    cedula = int(entry_cedula_buscar.get())
    for nombre, cedula_, ciudad in pasajeros:
        if cedula_ == cedula:
            label_destino.config(text=f"El pasajero {nombre} viaja a {ciudad}")
            break

root = tk.Tk()
root.title("Gestión de Pasajeros")

label_nombre = tk.Label(root, text="Nombre:")
entry_nombre = tk.Entry(root)
label_cedula = tk.Label(root, text="Cédula:")
entry_cedula = tk.Entry(root)
label_ciudad = tk.Label(root, text="Ciudad:")
entry_ciudad = tk.Entry(root)

button_agregar_pasajero = tk.Button(root, text="Ingresar Pasajero", command=agregar_pasajero)
button_agregar_pasajero.grid(row=0,column=2)

button_agregar_ciudad = tk.Button(root, text="Agregar Ciudad", command=agregar_ciudad)
button_agregar_ciudad.grid(row=1, column=2)
button_buscar_destino = tk.Button(root, text="Buscar Destino", command=destino_pasajero)
button_buscar_destino.grid(row=2, column=2)

label_destino = tk.Label(root, text="Viajes")
label_destino.grid(row=0,column=0)

listbox_pasajeros = tk.Listbox(root)
listbox_pasajeros.grid(row=1,column=0)

label_ciudades = tk.Label(root, text="Ciudades")
label_ciudades.grid(row=0,column=1)

listbox_ciudades = tk.Listbox(root)
listbox_ciudades.grid(row=1, column=1)

label_ciudad_nueva = tk.Label(root, text="Nueva Ciudad:")
entry_ciudad_nueva = tk.Entry(root)

label_pais = tk.Label(root, text="País:")
entry_pais = tk.Entry(root)

label_cedula_buscar = tk.Label(root, text="Cédula a buscar:")
entry_cedula_buscar = tk.Entry(root)

root.mainloop()
