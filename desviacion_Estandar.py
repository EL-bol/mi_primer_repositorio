#Nombre: desviacion_Estandar
#Descripción: Algoritmo que determina la desviacion estandar de un conjunto de números
#Autor: Morán Vargas Santiago
#Fecha: 07 de Noviembre del 2025


import math

print("Algoritmo que calcula la desviación estandar.")

#Solicitar cantidad de datos y verificar lo ingresado
cantidad = int(input("Ingrese la cantidad de datos: "))

while cantidad < 2 :
    print("Error: Ingrese un número mayor a 2.")
    cantidad = int(input("Ingrese la cantidad de datos: "))


datos = []  # lista vacía para guardar los valores

promedio = 0

for i in range(cantidad):
    datos.append(float(input("Ingrese el elemento "+str(i+1)+": " )))

    promedio = promedio + datos[i]

#Calcular el promedio

promedio = promedio / cantidad

#Calcular la desviación


for i in range(cantidad):
    desviacion = desviacion + ((datos[i] - promedio) ** 2)


resultado = math.sqrt(desviacion / (cantidad-1))


print("La desviacion estandar es: ",resultado)


#Programa que haga suma, resta, multiplicacion normal y por escalar y norma(magnitud) de vectores
#(1,2,3,4,5 en ese orden) Y agrega una opcion de terminar el programa 
