
import math

# Función que pide los valores de un vector
def pedir_Datos():

    x = int(input("Ingrese la coordenada X: "))
    y = int(input("Ingrese la coordenada Y: "))
    z = int(input("Ingrese la coordenada Z: "))
    
    return x, y, z

#****************************************************************

# Función que suma dos vectores

def suma_Vectores(x1, y1, z1, x2, y2, z2):

    xr = x1 + x2
    yr = y1 + y2
    zr = z1 + z2

    return xr, yr, zr

#****************************************************************

# Función que resta dos vectores

def resta_Vectores(x1, y1, z1, x2, y2, z2):

    xr = x1 - x2
    yr = y1 - y2
    zr = z1 - z2

    return xr, yr, zr

#****************************************************************

# Función que multiplica un vector por escalar

def escalar_Vectores(x, y, z, escalar):

    xr = x * escalar
    yr = y * escalar
    zr = z * escalar

    return xr, yr, zr

#****************************************************************

# Función que obtiene la magnitud de un vector 

def magnitud_Vectores(x, y, z):

    magnitud = math.sqrt((x**2)+(y**2)+(z**2))

    return magnitud

#****************************************************************

#Pedirlos valores del primer vector y llamar a la función
print("Introducir los valores del primer vector:")
x1, y1, z1 = pedir_Datos()


#Pedir valores del segundo vector y llamar a la función
print("\nIntroducir los valores del segundo vector:")
x2, y2, z2 = pedir_Datos()

# Sumar vectores
xr, yr, zr = suma_Vectores(x1, y1, z1, x2, y2, z2)

print(f"\nLa suma de los vectores es: ({xr}, {yr}, {zr})")


#resta de vectores
xr,yr,zr = resta_Vectores(x1,y1,z1,x2,y2,z2)

print(f"\nLa resta de los vectores es: ({xr}, {yr}, {zr})")


#escalar vectores 

escalar = int(input(print("Ingrese el valor a escalar el vector: ")))

xr,yr.zr = escalar_Vectores(x1,y1,z1,escalar)

print(f"\nEl producto por escalar del vector es: ({xr}, {yr}, {zr})")


#Magnitud de vectores

magnitud = magnitud_Vectores(x1,y1,z1)

print(f"la magnitud del vector ({x1}, {y1}, {z1}) es: {magnitud}")

