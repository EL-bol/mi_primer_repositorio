
#Nombre: rectangulo_Hueco
#Descripcion: Algoritmoque dibuja un rectangulo
#Autor: Moran Vargas Santiago
#Fecha: 05 de Noviembre del 2025

simbolo= str(input("Ingrese el símbolo"))

#Pedir la base y verificar
base = int(input("Ingrese la base del rectángulo: "))

while base<= 0:
    base = int(input("Ingrese la base del rectángulo: "))


#Pedir la altura y verificar
altura = int(input("Ingrese la altura del rectángulo: "))

while altura <= 0:
    altura = int(input("Ingrese la base del rectángulo: "))


#Dibujar la primer linea
for i in range (1,base+1) :
    print("*", end="")

print("")

#Dibujar el medio
for i in range(1,altura-1):
    print(simbolo, end="")
    for j in range(1,base-1):
        print (" ", end="")

    print(simbolo)


#Dibujar la ultima línea
for i in range (1,base+1) :
    print(simbolo, end="")