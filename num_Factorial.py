num = int(input("Escribe el número a sacar el factorial:"))

fact = 1.0
for i in range (2,num + 1) :
    fact = fact * i 

print("El factorial del número es: ", fact )