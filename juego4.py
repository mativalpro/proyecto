from flask import Flask, request, jsonify
import random

app = Flask(__name__)

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


# Crear tableros
tablero_jugador = crear_tablero()
tablero_ia = crear_tablero()

# Barcos IA
colocar_barcos_ia(tablero_ia)


# Colocar barcos jugador
@app.route("/colocar_barco", methods=["POST"])
def colocar_barco():

    datos = request.get_json()

    fila = int(datos["fila"])
    columna = int(datos["columna"])

    if tablero_jugador[fila][columna] == 0:

        tablero_jugador[fila][columna] = 1

        return jsonify({
            "resultado": "colocado"
        })

    return jsonify({
        "resultado": "ocupado"
    })


from flask import Flask, request, jsonify
import random

app = Flask(__name__)

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


# Crear tableros
tablero_jugador = crear_tablero()
tablero_ia = crear_tablero()

# Barcos IA
colocar_barcos_ia(tablero_ia)


# Colocar barcos jugador
@app.route("/colocar_barco", methods=["POST"])
def colocar_barco():

    datos = request.get_json()

    fila = int(datos["fila"])
    columna = int(datos["columna"])

    if tablero_jugador[fila][columna] == 0:

        tablero_jugador[fila][columna] = 1

        return jsonify({
            "resultado": "colocado"
        })

    return jsonify({
        "resultado": "ocupado"
    })


# Disparo jugador
@app.route("/disparo", methods=["POST"])
def disparo():

    datos = request.get_json()

    fila = int(datos["fila"])
    columna = int(datos["columna"])

    resultado_jugador = ""

    if tablero_ia[fila][columna] == 1:

        tablero_ia[fila][columna] = 2
        resultado_jugador = "impacto"

    elif tablero_ia[fila][columna] == 0:

        tablero_ia[fila][columna] = 4
        resultado_jugador = "agua"

    else:

        resultado_jugador = "repetido"


    # Turno IA
    fila_ia = random.randint(0, TAM - 1)
    columna_ia = random.randint(0, TAM - 1)

    resultado_ia = ""

    if tablero_jugador[fila_ia][columna_ia] == 1:

        tablero_jugador[fila_ia][columna_ia] = 3
        resultado_ia = "impacto"

    elif tablero_jugador[fila_ia][columna_ia] == 0:

        tablero_jugador[fila_ia][columna_ia] = 4
        resultado_ia = "agua"

    else:

        resultado_ia = "repetido"


    # Verificar ganador
    ganador_partida = ganador(
        tablero_jugador,
        tablero_ia
    )

    return jsonify({

        "resultado_jugador": resultado_jugador,

        "resultado_ia": resultado_ia,

        "fila_ia": fila_ia,
        "columna_ia": columna_ia,

        "ganador": ganador_partida

    })


if __name__ == "__main__":
    app.run(debug=True)


if __name__ == "__main__":
    app.run(debug=True)