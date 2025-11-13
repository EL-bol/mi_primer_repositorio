#nombre: dia_Semana
#Algoritmo q dice el dia de la semana dependiendo del número ingresado
#Autor: Santiago Moran Vargas
#Fecha: 01 de Noviembre del 2025

dia = 8
while dia > 7 or dia < 0 :
    dia = int(input("Ingrese el dia de la semana (1-7): "))



if dia == 1 :
    print("el dia es domingo.")
elif dia == 2 :
    print("el dia es lunes.")
elif dia == 3 :
    print("el dia es martes.")
elif dia == 4 :
    print("el dia es miercoles.")
elif dia == 5 :
    print("el dia es jueves.")
elif dia == 6 :
    print("el dia es viernes.")
elif dia == 7 :
    print("el dia es sábado.")
