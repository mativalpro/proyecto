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

