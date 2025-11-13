
#Nombre: reloj_Arena
#Descripcion: Algoritmo que dibuja un reloj de arena
#Autor: Moran Vargas Santiago
#Fecha: 06 de Noviembre del 2025

simbolo= str(input("Ingrese el símbolo"))

#Pedir la base y verificar
base = int(input("Ingrese la base del reloj: "))

while base<= 0:
    base = int(input("Ingrese la base del reloj: "))




#Dibujar la primer linea
for i in range (1,base+1) :
    print("*", end="")

print("")


#Dibujar el medio
k = 1
l = 2


# En la parte de "for i in range(base-1,(base+1)//2):" el // significa que 
for i in range(base-1,(base+1)//2):
    print(" ",end="")

    for j in range(1,base-l):

        print (simbolo, end="")

    print("")



#Dibujar la ultima línea
for i in range (1,base+1) :
    print(simbolo, end="")