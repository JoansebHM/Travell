pasajeros = []
ciudades = []
menu = """
----------------------------------------
Seleccione una de las opciones \n
1) Agregar pasajero a la lista de viajeros\n
2) Agregar ciudad a la lista de ciudades\n
3) Ver a qué ciudad viaja un pasajero (por CC)\n
4) Mostrar cantidad de pasajeros que viajan a una ciudad\n
5) Ver a qué país viaja un pasajero (por CC)\n
6) Mostrar cantidad de pasajeros que viajan a un país\n
7) Salir del programa\n
----------------------------------------
"""

def agregarPasajeros(cedula, nombre, ciudad):
    tuplaPasajeros = (nombre, cedula, ciudad)
    pasajeros.append(tuplaPasajeros)
    print(pasajeros)

def agregarCiudad(ciudad, pais):
    tuplaCiudades = (ciudad, pais)
    ciudades.append(tuplaCiudades)
    print(ciudades)

def destinoPasajero(cedula):
    for nombre, cedula_, ciudad in pasajeros:
        if cedula_ == cedula:
            print(f"El pasajero {nombre} viaja a {ciudad}")
            break  

def cantidadPasajerosEnCiudad(ciudad):
    cantPasajerosCiudad = 0
    for nombre, _ , ciudad_ in pasajeros:
        if ciudad_ == ciudad:
            cantPasajerosCiudad += 1
    print(f"La cantidad de pasajeros que viajan a {ciudad} es {cantPasajerosCiudad}")


def destinoPaisPasajero(cedula):
    for nombre, cedula_, ciudad in pasajeros:
        if cedula_ == cedula:
            for ciudad_ , pais in ciudades:
                if ciudad == ciudad_:
                    print(f"El usuario {nombre} viaja a {pais}")
                    break


def cantidadPasajerosEnPais(pais):
    cantPasajerosPais = 0
    for _, _, ciudad in pasajeros:
        for ciudad_, pais_ in ciudades:
            if ciudad == ciudad_ and pais_ == pais:
                cantPasajerosPais += 1
    print(f"La cantidad de pasajeros que viajan a {pais} es {cantPasajerosPais}")

import sys

def main():
    while True:
        opcion = sys.stdin.readline().strip()
        if not opcion:
            break  # Salir del bucle si no hay más líneas
        if opcion == "1":
            nombre = sys.stdin.readline().strip()
            cedula = int(sys.stdin.readline().strip())
            ciudad = sys.stdin.readline().strip()
            agregarPasajeros(cedula, nombre, ciudad)
        elif opcion == "2":
            ciudad = sys.stdin.readline().strip()
            pais = sys.stdin.readline().strip()
            agregarCiudad(ciudad, pais)
        elif opcion == "3":
            cedula = int(sys.stdin.readline().strip())
            destinoPasajero(cedula)
        elif opcion == "4":
            ciudad = sys.stdin.readline().strip()
            cantidadPasajerosEnCiudad(ciudad)
        elif opcion == "5":
            cedula = int(sys.stdin.readline().strip())
            destinoPaisPasajero(cedula)
        elif opcion == "6":
            pais = sys.stdin.readline().strip()
            cantidadPasajerosEnPais(pais)
        elif opcion == "7":
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    pasajeros = []
    ciudades = []
    main()





