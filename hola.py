import math

# === Datos del pentágono ===
puntos = {
    "A": (2, 0),
    "B": (1, 2),
    "C": (-1, 2),
    "D": (-2, 0),
    "E": (0, -2)
}

# === Vector de traslación ===
angulo = 30  # grados
magnitud = 1  # unidades
T = (
    5 + magnitud * math.cos(math.radians(angulo)),
    -3 + magnitud * math.sin(math.radians(angulo))
)

# === Traslación ===
puntos_trasladados = {}
for nombre, (x, y) in puntos.items():
    x_nuevo = x + T[0]
    y_nuevo = y + T[1]
    puntos_trasladados[nombre + "'"] = (x_nuevo, y_nuevo)

# === Mostrar coordenadas ===
print("=== PENTÁGONO ORIGINAL ===")
for n, (x, y) in puntos.items():
    print(f"{n}: ({x}, {y})")

print("\n=== VECTOR DE TRASLACIÓN TOTAL ===")
print(f"T = ({round(T[0], 3)}, {round(T[1], 3)})")

print("\n=== PENTÁGONO TRASLADADO ===")
for n, (x, y) in puntos_trasladados.items():
    print(f"{n}: ({round(x, 3)}, {round(y, 3)})")

# === Dibujo ASCII ===
# Creamos una cuadrícula de caracteres (tamaño 30x20 aprox)
ancho, alto = 30, 20
grilla = [[" " for _ in range(ancho)] for _ in range(alto)]

def marcar_punto(x, y, simbolo):
    """Coloca un punto en la cuadrícula (con origen en el centro)."""
    cx, cy = ancho // 2, alto // 2
    ix = int(round(cx + x))
    iy = int(round(cy - y))
    if 0 <= ix < ancho and 0 <= iy < alto:
        grilla[iy][ix] = simbolo

# Dibujar puntos originales y trasladados
for n, (x, y) in puntos.items():
    marcar_punto(x, y, "O")
for n, (x, y) in puntos_trasladados.items():
    marcar_punto(x, y, "X")

# === Mostrar dibujo ===
print("\n=== REPRESENTACIÓN ASCII ===")
print("Leyenda: O = original, X = trasladado\n")
for fila in grilla:
    print("".join(fila))
