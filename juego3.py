import random

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