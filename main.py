import random
import pyttsx3
puntaje = 0
archivo = open("puntaje.txt", "a")

nombre = ""
y = 1
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

def guerra_naval():
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
def ahorcado():
    # Lista con los dibujos del ahorcado (desde 0 hasta 6 errores)
    AHORCADO_DIBUJOS = [
        """
         +---+
         |   |
             |
             |
             |
             |
        =========
        """,
        """
         +---+
         |   |
         O   |
             |
             |
             |
        =========
        """,
        """
         +---+
         |   |
         O   |
         |   |
             |
             |
        =========
        """,
        """
         +---+
         |   |
         O   |
        /|   |
             |
             |
        =========
        """,
        """
         +---+
         |   |
         O   |
        /|\  |
             |
             |
        =========
        """,
        """
         +---+
         |   |
         O   |
        /|\  |
        /    |
             |
        =========
        """,
        """
         +---+
         |   |
         O   |
        /|\  |
        / \  |
             |
        =========
        """
    ]

    print("--- ¡BIENVENIDO AL AHORCADO! ---")

    # --- LEER EL ARCHIVO DE PALABRAS (FORMA BÁSICA) ---
    archivo = open("palabras.txt", "r", encoding="utf-8") #encoding="utf-8" para que lea acentos y ñ correctamente
    palabras = []

    for linea in archivo:
        palabra_limpia = linea.strip()
        if palabra_limpia != "":
            palabras.append(palabra_limpia.lower())

    archivo.close()


    # Seleccionar una palabra al azar usando random.randint
    indice_aleatorio = random.randint(0, len(palabras) - 1)
    palabra_secreta = palabras[indice_aleatorio]

    # Variables de control del juego
    letras_adivinadas = []
    errores = 0
    max_errores = len(AHORCADO_DIBUJOS) - 1

    # Bucle principal del juego
    while errores < max_errores:
        # 1. Mostrar el dibujo según los errores actuales
        print(AHORCADO_DIBUJOS[errores])
    
        # 2. Mostrar la palabra con guiones bajos
        estado_palabra = ""
        for letra in palabra_secreta:
            if letra in letras_adivinadas:
                estado_palabra = estado_palabra + letra + " "
            else:
                estado_palabra = estado_palabra + "_ "
        print("Palabra: " + estado_palabra + "\n")
    
        # 3. Verificar si el jugador ya descubrió toda la palabra
        if "_" not in estado_palabra:
            print("¡Felicidades! Ganaste. La palabra era: " + palabra_secreta.upper())
            break
        
        # 4. Pedir letra al usuario
        intento = input("Ingresa una letra: ").lower().strip()

        # Validar que sea solo una letra
        if len(intento) != 1 or intento.isalpha() == False:
            print("Por favor, ingresa solo una letra válida.")
            continue
        
        # Verificar si ya la había dicho
        if intento in letras_adivinadas:
            print("Ya habías intentado con esa letra. Prueba otra.")
            continue
        
        # Guardar la letra intentada
        letras_adivinadas.append(intento)

        # 5. Comprobar si la letra está en la palabra secreta
        if intento in palabra_secreta:
            print("¡Bien hecho! La letra está en la palabra.")
        else:
            print("¡Incorrecto! Te acercas más a la horca.")
            errores = errores + 1

    # Si llega al límite de errores, pierde
    if errores == max_errores:
        print(AHORCADO_DIBUJOS[errores])
        print("¡Perdiste! Te has quedado sin intentos. La palabra era: " + palabra_secreta.upper())
def rey_chistes():
    print("--- ¡EL REY DEL CHISTE (HUMOR NEGRO)! ---")

    # --- LEER EL ARCHIVO DE CHISTES (FORMA BÁSICA) ---
    archivo = open("chistes.txt", "r", encoding="utf-8")
    chistes = []

    for linea in archivo:
        chiste_limpio = linea.strip()
        if chiste_limpio != "":
            chistes.append(chiste_limpio)

    archivo.close()
    # --------------------------------------------------

    # Seleccionar un chiste al azar usando random.randint
    indice_aleatorio = random.randint(0, len(chistes) - 1)
    chiste_elegido = chistes[indice_aleatorio]

    # Separar la pregunta del remate usando el guion bajo (_)
    if "_" in chiste_elegido:
        partes = chiste_elegido.split("_")
        pregunta = partes[0].strip()
        remate = partes[1].strip()
    else:
        pregunta = chiste_elegido
        remate = "..."

    # Mostrar la pregunta del chiste oscuro
    print("\nPregunta: " + pregunta)

    # El usuario escribe lo que quiera
    input("\nEscribe tu respuesta (o presiona Enter para ver el final): ")

    # Mostrar el remate directo
    print("\n" + "="*50)
    print("RESPUESTA: " + remate)
    print("="*50 + "\n")
def historialP():
    archivo2 = open("puntaje.txt", "r")
    registro = archivo2.readlines()
    for C in registro:
        listo = C.strip().split("_")
        print("nombre: ", listo[0], "puntaje: ", listo[1])
    archivo2.close()
        
def preguntas():
    global puntaje
    i = 0
    hablar("escribe 'salir' para dejar de jugar en cualquier momento")
    while i < 10:
        
        pnum = random.randrange(1,100)
        Pnum2 = random.randrange(1,100)
        Sresultado = str(pnum + Pnum2)
        Rresultado = str(pnum - Pnum2)
        Mresultado = str(pnum * Pnum2)
        pnum = str(pnum)
        Pnum2 = str(Pnum2)
        eleccion = random.randrange(1,4)
        if eleccion == 1:
            hablar("cuanto es " + pnum + "+" + Pnum2)
            respuesta =input().lower() #
            if respuesta == Sresultado:
                hablar("has ganado un punto")
                puntaje += 1
            if respuesta == "salir":
                hablar("saliendo del juego")
                i = 10
        if eleccion == 2:
            hablar("cuanto es " + pnum + "-" + Pnum2)
            respuesta = input().lower()
            if respuesta == Rresultado:
                hablar("has ganado un punto")
                puntaje += 1
            if respuesta == "salir":
                hablar("saliendo del juego")
                i = 10
        if eleccion == 3:
            hablar("cuanto es " + pnum + "*" + Pnum2)
            respuesta = input().lower()
            if respuesta == Mresultado:
                hablar("has ganado un punto")
                puntaje += 1
            if respuesta == "salir":
                hablar("saliendo del juego")
                i = 10
                
        i += 1
    print("tu puntaje final es: ", puntaje)
    nombre = input("ingrese su nombre para guardar su puntaje: ")
    hablar("gracias por jugar " + nombre + " tu puntaje final es: " + str(puntaje))
    archivo.write(nombre + "_" + str(puntaje) + "\n")
    archivo.close()


def juego_matematico():
    hablar("bienvenido al juego matematico\nresponde preguntas para ganar la maxima cantidad de puntos que puedas")
    hablar("desea jugar, ver el historial? o salir")
    elegir = input().lower()
    if elegir == "jugar":
        preguntas()
    if elegir == "salir":
        hablar("saliendo del juego")
    if elegir == "historial":
        historialP()
def hablar(texto):
    voz = pyttsx3.init()
    print(texto)
    voz.say(texto)
    voz.runAndWait()
def menu():
    global y
    while y != 0:
        hablar("presione")
        hablar("1 para juego matematico")
        hablar("2 para jugar ahorcado")
        hablar("3 para jugar rey del chiste")
        hablar("4 para jugar la guerra naval")
        hablar("0 para salir")
        y = int(input())
        if y == 1:
            hablar("Has seleccionado el juego matematico")
            juego_matematico()
        elif y == 2:
            hablar("Has seleccionado el ahorcado")
            ahorcado()
        elif y  == 3:
            hablar("Has seleccionado el rey del chiste")
            rey_chistes()
        elif y == 4:
            hablar("Has seleccionado la guerra naval")
            guerra_naval()
        elif y == 0:
            hablar("Saliendo...")
            y = 0
        else:
            hablar("a seleccionado una opcion fuera del menu\npor favor ingrese denuevo su opcion")
print("***************************************************************")
hablar("Bienvenido a QuadPlay")
print("***************************************************************")
eleccion = 0


try: 
    menu()
    archivo.close()
except ValueError:
    hablar("ha ingresado un valor invalido")