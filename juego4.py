import random

TAM = 5
BARCOS = 5


def crear_tablero():
    return [[0 for j in range(TAM)] for i in range(TAM)]


def mostrar_tableros(tablero_jugador, tablero_ia_oculto):
    print("\n")
    print("      TU TABLERO DE BARCOS")
    print("   0  1  2  3  4")
    for i in range(TAM):
        print(f"{i}  " + "  ".join(str(x) for x in tablero_jugador[i]))

    print("-" * 30)
    print("    TABLERO DE DISPAROS A IA")
    print("   0  1  2  3  4")
    for i in range(TAM):
        print(f"{i}  " + "  ".join(str(x) for x in tablero_ia_oculto[i]))
    print("=" * 30 + "\n")


def quedan_barcos(tablero):
    for i in range(TAM):
        for j in range(TAM):
            if tablero[i][j] == 1:
                return True
    return False


def colocar_barcos_ia(tablero):
    barcos_colocados = 0
    while barcos_colocados < BARCOS:
        fila = random.randint(0, TAM - 1)
        columna = random.randint(0, TAM - 1)
        if tablero[fila][columna] == 0:
            tablero[fila][columna] = 1
            barcos_colocados += 1


def colocar_barcos_jugador(tablero):
    print(f"Coloca tus {BARCOS} barcos")
    barcos_colocados = 0
    while barcos_colocados < BARCOS:
        try:
            print(f"Barco N° {barcos_colocados + 1}")
            fila = int(input("Introduce fila (0-4): "))
            columna = int(input("Introduce columna (0-4): "))

            if 0 <= fila < TAM and 0 <= columna < TAM:
                if tablero[fila][columna] == 0:
                    tablero[fila][columna] = 1
                    barcos_colocados += 1
                else:
                    print("Casilla ocupada")
            else:
                print("Deben ser entre 0 y 4.")
        except ValueError:
            print("Introduce un numero valido")


tablero_jugador = crear_tablero()
tablero_ia_real = crear_tablero()
tablero_ia_disparos = crear_tablero()

colocar_barcos_ia(tablero_ia_real)
colocar_barcos_jugador(tablero_jugador)
