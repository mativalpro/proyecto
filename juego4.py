import random

def crear_tablero():
    matriz = [[0 for j in range(5)] for i in range(5)]
    return matriz

def quedan_barcos(matriz):
    for i in range(5):
        for j in range(5):
            if matriz[i][j] == 1:
                return True
    return False
