#Nombre: menor_3_numeros
#Descripcion: Algoritmo que encuentra el número menor de tres números dados
#Autor: Moran Vargas Santiago
#Fecha: 31 de Octubre del 2025

num1 = float(input("Ingrese el primer número: "))

num2 = float(input("Ingrese el segundo número: "))

num3 = float(input("Ingrese el tercer número: "))

menor = num1

if menor >= num2:
    menor = num2
elif menor >= num3:
    menor = num3

print("El número menor es: ", menor)