# Juego Reto
# Luis Andrés Casillas                A01645008
import os
import random  

# Indicaciones del juego
print("¡Atención soldado! Te habla tu capitán: ")
print("\n El cabo Ryan está atrapado en medio de infantería nazi y tu misión es ayudarlo a escapar con vida \n Si el soldado no tiene escapatoria, se le considerará caído en combate. ")

# Esta funcion mostrara el tablero donde estara Ryan y los nazis
def tablero(laberinto, lugar_ryan):
    # Las librerias os y os.system se utilizan hacer que el avance de Ryan se vea fluido y no se tenga que imprimir todo el tablero de nuevo. Esta libreria "borra" o limpia el tablero 
    os.system('cls' if os.name == 'nt' else 'clear')
    # Este for crea el tablero iterando en cada fila
    # Como un plano cartesiano, la "x" representa las filas del tablero y la "y" representa el eje vertical o columnas
    for x in range(len(laberinto)):
        for y in range(len(laberinto[x])):
            if (x, y) == lugar_ryan:
                # Ryan
                print("ꆜ", end=" ")  
            elif laberinto[x][y] == 1:
                # Soldado nazi
                print("☬", end="  ")  
            else:
                # Espacio que determina la distancia entre los soldados nazis 
                print(" ", end=" ")  
        print()

# Esta función es para comprobar si Ryan ha sobrevivido y el usuario gano el juego
def ganar_juego(lugar_ryan, coordenada_salida):
    return lugar_ryan == coordenada_salida

# Dimensiones del tablero
filas = 13
columnas = 13

# Crear el laberinto con números aleatorios
laberinto = [[random.randint(0, 1) for _ in range(columnas)] for _ in range(filas)]

# Posición inicial del jugador y posición de salida
lugar_ryan = (0, 0)
coordenada_salida = (filas - 1, columnas - 1)
#coordenada_salida = [[random.randint(0, 1) for _ in range(columnas)] for _ in range(filas)]

# While principal utilizado para el rescate de Ryan
while True:
    tablero(laberinto, lugar_ryan)

    if ganar_juego(lugar_ryan, coordenada_salida):
        print("¡Has rescatado al soldado Ryan!")
        break
    # La variable "accion" representa la accion o decicion que realizará el usuario (subir, bajar, moverse lateralmente o salir del juego)
    accion = input("\n Utiliza las teclas W (arriba), A (izquierda), S (abajo), D (derecha) para moverte,\n o ingresa 'SA' (Soldado atrapado) si el soldado fue eliminado y reiniciar el juego: ").upper()

    if accion == 'SA':
        print("\n ¡El cabo Ryan ha muerto!\n\n Reinicia el juego para una nueva misión.")
        break

    proxima_posicion = lugar_ryan

    if accion == "W" and lugar_ryan[0] > 0:
        proxima_posicion = (lugar_ryan[0] - 1, lugar_ryan[1])
    elif accion == "A" and lugar_ryan[1] > 0:
        proxima_posicion = (lugar_ryan[0], lugar_ryan[1] - 1)
    elif accion == "S" and lugar_ryan[0] < filas - 1:
        proxima_posicion = (lugar_ryan[0] + 1, lugar_ryan[1])
    elif accion == "D" and lugar_ryan[1] < columnas - 1:
        proxima_posicion = (lugar_ryan[0], lugar_ryan[1] + 1)

    if laberinto[proxima_posicion[0]][proxima_posicion[1]] == 0:
        lugar_ryan = proxima_posicion
