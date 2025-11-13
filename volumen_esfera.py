#Nombre: volumen_esfera
#Descripcion: algoritmo q calcula el volumen de un aesfera
#Autor: Moran Vargas Santiago
#Fecha: 30 de octubre del 2025


import math

radio=float(input("Introduce el radio de la esfera:" ))

area = ((4/3) * math.pi) * (radio**3)

print("El volumen de la esfera es: ", area,"u3")