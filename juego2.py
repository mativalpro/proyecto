import random

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