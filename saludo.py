#Nombre del archivo: saludo.py
#Descripcion: hola mundo
#Autor: Moran Vargas Santiago
#Fecha: 28 de Octubre del 2025

nombre = "Cami"
edad = 17
peso = 50.7777777

print('holaaaa jdskajd')

print(nombre,", tienes",edad,"años y pesas", peso,"Kg." )

#formas de alterar los espacios entre elementos
print("{0:25}{1:8}{2:12}".format("NOMBRE","EDAD","PESO"))
print("%25s%8d%12.2e" %(nombre,edad,peso))

#leer algo
nombre = input("escribre tu nombre: ")

#leer algo y restringir una variable aun solo tipo
nombre = str(input("escribre tu nombre: "))

print(nombre)