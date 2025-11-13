
#Solicitar base del triángulo
base=input("Introduce la base del triángulo: ")

#validar que sean números positivos
while base <= 0 :
    print("Error: escribe un número positivo.")

    base=input("Introduce la base del triángulo: ")


#Validar altura del triángulo
altura=input("introduce la altura del triángulo: ")

#Validar que sean números positivos
while altura <= 0 :
    print("Error: escribe un número positivo.")

    altura=input("introduce la altura del triángulo: ")

#Calcular e imprimir el resultado
area = base * altura

print("El área del triangulo es: ", area)