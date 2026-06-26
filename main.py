import random
import pyttsx3
puntaje = 0
archivo = open("puntaje.txt", "a")

nombre = ""
y = 1
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
    archivo2.close()

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
        hablar("2 para juego2")
        hablar("3 para juego3")
        hablar("4 para juego4")
        hablar("0 para salir")
        y = int(input())
        if y == 1:
            hablar("Has seleccionado el juego matematico")
            juego_matematico()
        elif y == 2:
            hablar("Has seleccionado el juego 2")
        elif y  == 3:
            hablar("Has seleccionado el juego 3")
        elif y == 4:
            hablar("Has seleccionado el juego 4")
        elif y  == 0:
            hablar("Saliendo...")
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