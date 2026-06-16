import random
import pyttsx3
def hablar(texto):
    voz = pyttsx3.init()
    print(texto)
    voz.say(texto)
    voz.runAndWait()
def menu():
    hablar("presione")
    hablar("1 para juego1")
    hablar("2 para juego2")
    hablar("3 para juego3")
    hablar("4 para juego4")
    hablar("0 para salir")
    eleccion = int(input())
    if eleccion == 1:
        hablar("Has seleccionado el juego 1")
    elif eleccion == 2:
        hablar("Has seleccionado el juego 2")
    elif eleccion == 3:
        hablar("Has seleccionado el juego 3")
    elif eleccion == 4:
        hablar("Has seleccionado el juego 4")
    elif eleccion == 0:
        hablar("Saliendo...")
    else:
        hablar("a seleccionado una opcion fuera del menu\npor favor ingrese denuevo su opcion")
print("***************************************************************")
hablar("Bienvenido a (nombre)")
print("***************************************************************")
eleccion = 0


try: 
    menu()
except ValueError:
    hablar("ha ingresado un valor invalido")