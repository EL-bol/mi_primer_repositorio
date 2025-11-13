"""
Nombre del archivo: OperacionesVectoresFunciones.py
Descripción: 
Autor: Juárez Ochoa Javier Octavio
Fecha: 12/11/2025
"""
import math

def suma_vectores(lista_1, lista_2):
    resultado = []
    for i in range(0, len(lista_1)):
        resultado.append(lista_1[i] + lista_2[i])
    return resultado

def resta_vectores(lista_1, lista_2):
    resultado = []
    for i in range(0, len(lista_1)):
        resultado.append(lista_1[i] - lista_2[i])
    return resultado

def producto_elemento_elemento(lista_1, lista_2):
    resultado = []
    for i in range(0, len(lista_1)):
        resultado.append(lista_1[i] * lista_2[i])
    return resultado

def producto_escalar(lista_1, lista_2):
    resultado = 0
    for i in range(0, len(lista_1)):
        resultado += lista_1[i] * lista_2[i]
    return resultado

def magnitud_vector(lista_1):
    suma = 0
    for i in range(0, len(lista_1)):
        suma += vector1[i] ** 2
    suma = math.sqrt(suma)
    return suma

print("Algoritmo que realiza operaciones entre vectores\n")

eleccion = 0
while eleccion != "6":
    
    eleccion = input(
"""
(1) Suma de vectores
(2) Resta de vectores
(3) Producto elemento a elemento
(4) Producto escalar
(5) Magnitud
(6) Salir
""")
    vector1 = []
    vector2 = []
    resultado = []
    
    print("")
    if eleccion == "1" or eleccion == "2" or eleccion == "3" or eleccion == "4":
        tamanio = input("Introduce el tamaño de los vectores: ")
        tamanio = int(tamanio)
        for i in range(0, tamanio):
            vector1.append(input(f"Introduce el elemento #{i + 1} del vector 1: "))
            vector1[i] = float(vector1[i])
        print("")
        for i in range(0, tamanio):
            vector2.append(input(f"Introduce el elemento #{i + 1} del vector 2: "))
            vector2[i] = float(vector2[i])
    elif eleccion == "5":
        tamanio = input("Introduce el tamaño del vector: ")
        tamanio = int(tamanio)
        for i in range(0, tamanio):
            vector1.append(input(f"Introduce el elemento #{i + 1} del vector: "))
            vector1[i] = float(vector1[i])
    
    
    if eleccion == "1":
        print(suma_vectores(vector1, vector2))
    elif eleccion == "2":
        print(resta_vectores(vector1, vector2))
    elif eleccion == "3":
        print(producto_elemento_elemento(vector1, vector2))
    elif eleccion == "4":
        print(producto_escalar(vector1, vector2))
    elif eleccion == "5":
        print(f"Magnitud: {magnitud_vector(vector1)}")