#Nombre: menor_2_numeros
#Descripcion: Algoritmo que encuentra el número menor de dos números dados
#Autor: Moran Vargas Santiago
#Fecha: 31 de Octubre del 2025

num1 = float(input("Ingrese el primer número: "))

num2 = float(input("Ingrese el segundo número: "))

if num1 < num2:
    print("El npumero menor es:", num1)
elif num2< num1:
    print("El número menor es: ", num2)
else:
    print("Ambos números son iguales.")