import tkinter as tk
import tkinter.font as tkFont

pasajeros = []
ciudades = []

root = tk.Tk()
root.title("Sistema de pasajeros")
root.resizable(False,False)
font_sans = tkFont.Font(family="Helvetica", size=12)

def actualizar_lista_pasajeros():
    text_pasajeros_actuales.delete(1.0, tk.END)

    for pasajero in pasajeros:
        nombre_pasajero, cedula_pasajero, ciudad_pasajero = pasajero
        texto_pasajero_formateado = f"Nombre: {nombre_pasajero}\nCedula: {cedula_pasajero}\nCiudad: {ciudad_pasajero}\n--------------------\n"
        text_pasajeros_actuales.insert(tk.END, texto_pasajero_formateado)

def actualizar_lista_ciudades():
    text_ciudades_actuales.delete(1.0, tk.END)

    for ciudad in ciudades:
        nombre_ciudad, nombre_pais = ciudad
        texto_ciudades_formateado = f"Ciudad: {nombre_ciudad}\nPais: {nombre_pais}\n--------------------\n"
        text_ciudades_actuales.insert(tk.END, texto_ciudades_formateado)


def limpiar_celdas():
    label_pasajero_nuevo_nombre.grid_forget()
    label_pasajero_nuevo_cedula.grid_forget()
    label_pasajero_nuevo_ciudad.grid_forget()
    label_ciudad_nueva.grid_forget()
    label_pais_nuevo.grid_forget()
    btn_confirmar_ciudad.grid_forget()
    btn_confirmar_pasajero.grid_forget()
    entry_ciudad_nueva.grid_forget()
    entry_pais_nuevo.grid_forget()
    entry_pasajero_nuevo_nombre.grid_forget()
    entry_pasajero_nuevo_cedula.grid_forget()
    entry_pasajero_nuevo_ciudad.grid_forget()
    label_advertencia.grid_forget()

def confirmar_pasajero():
    nombre_pasajero = entry_pasajero_nuevo_nombre.get()
    cedula_pasajero_texto = entry_pasajero_nuevo_cedula.get() 
    ciudad_pasajero = entry_pasajero_nuevo_ciudad.get()
    try:
        cedula_pasajero = int(cedula_pasajero_texto)
    except ValueError:
        label_advertencia.grid(row=9, columnspan=2, sticky="ewns")
        return
    
    for pasajero in pasajeros:
        if cedula_pasajero == pasajero[1]:
            label_advertencia.grid(row=9, columnspan=2, sticky="ewns")
            label_advertencia.config(text="La cedula ya se encuentra registrada")
            return

    if not nombre_pasajero or not ciudad_pasajero:
        label_advertencia.grid(row=9, columnspan=2, sticky="ewns")
        return
    
    label_advertencia.config(text="Todos los campos deben estar diligenciados correctamente")
    tupla_pasajero = (nombre_pasajero, cedula_pasajero, ciudad_pasajero)
    pasajeros.append(tupla_pasajero)
    print(pasajeros)
    limpiar_celdas()
    actualizar_lista_pasajeros()


def confirmar_ciudad():
    nombre_ciudad = entry_ciudad_nueva.get()
    nombre_pais = entry_pais_nuevo.get()
    if not nombre_ciudad or not nombre_pais:
        label_advertencia.grid(row=8, columnspan=2, sticky="ewns")
        return
    
    tupla_ciudad = (nombre_ciudad, nombre_pais)
    ciudades.append(tupla_ciudad)
    print(ciudades)
    limpiar_celdas()
    actualizar_lista_ciudades()
    

def agregar_ciudad():
    limpiar_celdas()
    for entry in entries:
        entry.delete(0, tk.END)
    label_ciudad_nueva.grid(row=5,column=0)
    label_pais_nuevo.grid(row=6,column=0)
    entry_ciudad_nueva.grid(row=5,column=1, sticky="ewns")
    entry_pais_nuevo.grid(row=6,column=1, sticky="ewns")
    btn_confirmar_ciudad.grid(row=7, columnspan=2, sticky="ewns")

def agregar_pasajero():
    limpiar_celdas()
    for entry in entries:
        entry.delete(0, tk.END)
    label_pasajero_nuevo_nombre.grid(row=5,column=0)
    label_pasajero_nuevo_cedula.grid(row=6, column=0)
    label_pasajero_nuevo_ciudad.grid(row=7, column=0)
    entry_pasajero_nuevo_nombre.grid(row=5, column=1, sticky="ewns")
    entry_pasajero_nuevo_cedula.grid(row=6,column=1, sticky="ewns")
    entry_pasajero_nuevo_ciudad.grid(row=7, column=1, sticky="ewns")
    btn_confirmar_pasajero.grid(row=8, columnspan=2, sticky="ewns")

# Labels de text
label_pasajeros_actuales = tk.Label(root, text="Pasajeros", font=font_sans)
label_ciudades_actuales = tk.Label(root, text="Ciudades", font=font_sans)
label_pasajero_nuevo_nombre = tk.Label(root, text="Nombre", font=font_sans)
label_pasajero_nuevo_cedula = tk.Label(root, text="Cedula", font=font_sans)
label_pasajero_nuevo_ciudad = tk.Label(root, text="Ciudad", font=font_sans)
label_ciudad_nueva = tk.Label(root, text="Ciudad", font=font_sans)
label_pais_nuevo = tk.Label(root, text="Pais", font=font_sans)
label_advertencia = tk.Label(root, text="Todos los campos deben estar diligenciados correctamente", font=font_sans)

# Entries
entry_pasajero_nuevo_nombre = tk.Entry(root, font=font_sans)
entry_pasajero_nuevo_cedula = tk.Entry(root, font=font_sans)
entry_pasajero_nuevo_ciudad = tk.Entry(root, font=font_sans)
entry_ciudad_nueva = tk.Entry(root, font=font_sans)
entry_pais_nuevo = tk.Entry(root, font=font_sans)
entries = [entry_pasajero_nuevo_nombre,
           entry_pasajero_nuevo_cedula,
           entry_pasajero_nuevo_ciudad,
           entry_ciudad_nueva,
           entry_pais_nuevo]

# Mostrar informacion
text_pasajeros_actuales = tk.Text(root, wrap=tk.WORD, font=font_sans)
text_ciudades_actuales = tk.Text(root, wrap=tk.WORD, font=font_sans)

# Botones
btn_agregar_pasajero = tk.Button(root, text="Agregar Pasajero", font=font_sans, command=agregar_pasajero)
btn_agregar_ciudad = tk.Button(root, text="Agregar Ciudad", font=font_sans, command=agregar_ciudad)
btn_buscar_por_cedula = tk.Button(root, text="Buscar Persona", font=font_sans)
btn_cuantos_viajan_ciudad = tk.Button(root, text="Cantidad de personas en ciudad", font=font_sans)
btn_cuantos_viajan_pais = tk.Button(root, text="Cantidad de personas en pais", font=font_sans)
btn_cancelar = tk.Button(root, text="Cancelar", font=font_sans, command=limpiar_celdas)
btn_confirmar_pasajero = tk.Button(root, text="Confirmar", font=font_sans, command=confirmar_pasajero)
btn_confirmar_ciudad = tk.Button(root, text="Confirmar", font=font_sans, command=confirmar_ciudad)


# Configuracion de componentes
text_pasajeros_actuales.config(width=30, height=10)
text_ciudades_actuales.config(width=30, height=10)
text_pasajeros_actuales.config(state="normal")
text_ciudades_actuales.config(state="normal")
text_pasajeros_actuales.bind("<Key>", "break")
text_ciudades_actuales.bind("<Key>", "break")
btn_agregar_pasajero.config(cursor="hand2")
btn_agregar_ciudad.config(cursor="hand2")  
btn_buscar_por_cedula.config(cursor="hand2")  
btn_cuantos_viajan_ciudad.config(cursor="hand2")  
btn_cuantos_viajan_pais.config(cursor="hand2")
btn_confirmar_pasajero.config(cursor="hand2")
btn_confirmar_ciudad.config(cursor="hand2")
btn_cancelar.config(cursor="hand2")

# Despliegue de componentes
label_pasajeros_actuales.grid(row=0,column=0)
text_pasajeros_actuales.grid(row=1,column=0)
label_ciudades_actuales.grid(row=0,column=1)
text_ciudades_actuales.grid(row=1,column=1)
btn_agregar_pasajero.grid(row=2, column=0, sticky="ewns")
btn_agregar_ciudad.grid(row=2, column=1, sticky="ewns")
btn_buscar_por_cedula.grid(row=3, column=0, sticky="ewns")
btn_cuantos_viajan_ciudad.grid(row=3, column=1, sticky="ewns")
btn_cuantos_viajan_pais.grid(row=4, column=1 ,columnspan=2, sticky="ewns")
btn_cancelar.grid(row=4, column=0, sticky="ewns")

root.mainloop()