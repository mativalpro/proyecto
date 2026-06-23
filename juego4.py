import random

TAM = 5
BARCOS = 5


# Crear tablero
def crear_tablero():

    matriz = [[0 for j in range(TAM)] for i in range(TAM)]

    return matriz


# Quedan barcos
def quedan_barcos(tablero):

    for i in range(TAM):
        for j in range(TAM):

            if tablero[i][j] == 1:
                return True

    return False


# Ganador
def ganador(tablero_jugador, tablero_ia):

    if not quedan_barcos(tablero_ia):
        return "Jugador"

    if not quedan_barcos(tablero_jugador):
        return "IA"

    return None


# Colocar barcos IA
def colocar_barcos_ia(tablero):

    barcos_colocados = 0

    while barcos_colocados < BARCOS:

        fila = random.randint(0, TAM - 1)
        columna = random.randint(0, TAM - 1)

        if tablero[fila][columna] == 0:

            tablero[fila][columna] = 1
            barcos_colocados += 1


tablero_jugador = crear_tablero()
tablero_ia = crear_tablero()


colocar_barcos_ia(tablero_ia)

from flask import Flask, request, jsonify

app = Flask(__name__)
barcos_colocados = 0

@app.route("/colocar_barco", methods=["POST"])
def colocar_barco():

    datos = request.get_json()

    fila = datos["fila"]
    columna = datos["columna"]

    if tablero_jugador[fila][columna] == 0:

        tablero_jugador[fila][columna] = 1

        return jsonify({
            "resultado": "colocado"
        })

    return jsonify({
        "resultado": "ocupado"
    })

turno = True
juego_activo = True


while juego_activo:

    if turno:

        fila = int(input("Fila ataque: "))
        columna = int(input("Columna ataque: "))

        if tablero_ia[fila][columna] == 1:

            tablero_ia[fila][columna] = 2
            print("Impacto")

        elif tablero_ia[fila][columna] == 0:

            tablero_ia[fila][columna] = 4
            print("Agua")

        turno = False

    else:

        fila = random.randint(0, TAM - 1)
        columna = random.randint(0, TAM - 1)

        if tablero_jugador[fila][columna] == 1:

            tablero_jugador[fila][columna] = 3
            print("La IA impactó")

        elif tablero_jugador[fila][columna] == 0:

            tablero_jugador[fila][columna] = 4
            print("La IA falló")

        turno = True

    resultado = ganador(
        tablero_jugador,
        tablero_ia
    )

    if resultado is not None:

        print("Ganador:", resultado)

        juego_activo = False