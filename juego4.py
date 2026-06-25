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

print("\n¡Empieza la batalla!")

while quedan_barcos(tablero_jugador) and quedan_barcos(tablero_ia_real):
    mostrar_tableros(tablero_jugador, tablero_ia_disparos)

    print("Tu turno de disparo ")
    tiro_valido = False
    while not tiro_valido:
        try:
            fila = int(input("Fila a disparar (0-4): "))
            columna = int(input("Columna a disparar (0-4): "))

            if 0 <= fila < TAM and 0 <= columna < TAM:
                if tablero_ia_disparos[fila][columna] in (2, 3):
                    print("Ya disparaste ahí. Intenta otra casilla.")
                    continue

                if tablero_ia_real[fila][columna] == 1:
                    print("impacto")
                    tablero_ia_real[fila][columna] = 3
                    tablero_ia_disparos[fila][columna] = 3
                else:
                    print("Agua")
                    tablero_ia_disparos[fila][columna] = 2
                tiro_valido = True
            else:
                print("Coordenadas inválidas.")
        except ValueError:
            print("Introduce un numero valido")

    if not quedan_barcos(tablero_ia_real):
        break

    print("\nTurno IA")
    ia_tiro_valido = False
    while not ia_tiro_valido:
        fila_ia = random.randint(0, TAM - 1)
        columna_ia = random.randint(0, TAM - 1)

        if tablero_jugador[fila_ia][columna_ia] in (0, 1):
            if tablero_jugador[fila_ia][columna_ia] == 1:
                print(f"IA Disparo en ({fila_ia},{columna_ia}) Impacto")
                tablero_jugador[fila_ia][columna_ia] = 4
            else:
                print(f"IA Disparo en ({fila_ia},{columna_ia}) Agua")
                tablero_jugador[fila_ia][columna_ia] = 2
            ia_tiro_valido = True

mostrar_tableros(tablero_jugador, tablero_ia_disparos)
if not quedan_barcos(tablero_ia_real):
    print("¡Ganaste la partida!")
else:
    print("La IA hundió todos tus barcos.")