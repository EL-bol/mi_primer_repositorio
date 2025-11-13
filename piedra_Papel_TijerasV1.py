#Nombre: piedra_Papel_Tijeras
#Descripcion: Algoritmoque se usa para jugar piedra papel o tijera


from random import randint

print("Elige una opcion")
print("1= Piedra.")
print("2= Papel.")
print("3= Tijetas.")
print("0= Salir.")

# Validar la opción elegida

op = int(input(""))
while op > 3 or op < 0 :
    print("Error: Elige una opción válida.")
    op = int(input(""))

while op != 0 :

    print("El usuario ha elegido:")

    if op == 1 :
        print("Piedra")
    elif op == 2 :
        print("Papel")
    elif op == 3 :
        print("Tijeras.")
    

    #Hacer que la maquina elija una opción
    maq = randint(1,3)

    print("La maquina ha elegido:")

    if maq == 1 :
        print("Piedra")
    elif maq == 2 :
        print("Papel")
    elif maq == 3 :
        print("Tijeras.")

    if op == maq :
        print("Empate...")
    elif (op == 1 and maq == 2) or (op == 2 and maq == 3) or (op == 3 and maq == 1) :
        print("Has perdido :(")
    elif (op == 1 and maq == 3) or (op == 2 and maq == 1) or (op == 3 and maq == 2) :
        print ("Has ganado :)")

    
    print("Jugar de nuevo?...")
    print("Elige una opcion")
    print("1= Piedra.")
    print("2= Papel.")
    print("3= Tijetas.")
    print("0= Salir.")

    # Validar la opción elegida

    op = int(input(""))
    while op > 3 or op < 0 :
        print("Error: Elige una opción válida.")
        op = int(input(""))


