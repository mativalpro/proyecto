import random
import pyttsx3
def preguntas():

    i = 0
    while i < 10:
        hablar("escribe 'salir' para dejar de jugar en cualquier momento")
        pnum = random.randrange(1,100)
        Pnum2 = random.randrange(1,100)
        Sresultado = str(pnum + Pnum2)
        Rresultado = str(pnum - Pnum2)
        Mresultado = str(pnum * Pnum2)
        pnum = str(pnum)
        Pnum2 = str(Pnum2)
        eleccion = random.randrange(1,3)
        if eleccion == 1:
            hablar("cuanto es " + pnum + "+" + Pnum2)
            respuesta =input().lower()
            if respuesta == Sresultado:
                hablar("has ganado un punto")
            if respuesta == "salir":
                hablar("saliendo del juego")
                i = 10
        if eleccion == 2:
            hablar("cuanto es " + pnum + "-" + Pnum2)
            respuesta = input().lower()
            if respuesta == Rresultado:
                hablar("has ganado un punto")
            if respuesta == "salir":
                hablar("saliendo del juego")
                i = 10
        if eleccion == 3:
            hablar("cuanto es " + pnum + "*" + Pnum2)
            respuesta = input().lower()
            if respuesta == Mresultado:
                hablar("has ganado un punto")
            if respuesta == "salir":
                hablar("saliendo del juego")
                i = 10
        i += 1


def hablar(texto):
    voz = pyttsx3.init()
    print(texto)
    voz.say(texto)
    voz.runAndWait()
def juego_matematico():
    hablar("bienvenido al juego matematico\nresponde preguntas para ganar la maxima cantidad de puntos que puedas")
    hablar("desea jugar?")
    elegir = input().lower()
    if elegir == "si":
        preguntas()
    if elegir == "no":
        hablar("saliendo del juego")
juego_matematico()