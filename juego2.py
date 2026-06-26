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