print("Algoritmo que calcula combinaciones de N en R")


#Solicitar N y verificar
n = int(input("Ingresa el número  total: "))

while n <= 0 :
    n = int(input("Ingresa el número  total: "))


#Solicitar R y verificar
r = int(input("Ingresa las combinaciones: "))

while r <= 0 or r > n:
    r = int(input("Ingresa las combinaciones: "))


#calcular el factorial de n y de r

nF = 1.0
for i in range (2,n + 1) :
    nF *= i 


rF = 1.0
for i in range (2,r + 1) :
    rF *= i 


#Calcular factorial de NR

nr = 1.0
for i in range (2,(n-r) + 1) :
    nr *= i 

#Calcular el total
total = nF /(rF * nr)

#imprimir el resultado

print("las combinaciones de ", n, " en ", r" son: ",total)

#TAREA el algoritmo de los cuadrados rellenos