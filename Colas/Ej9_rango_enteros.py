"""
Dada una cola de valores enteros calcular su rango y contar cuántos elementos negativos hay.
"""
import sys
from pathlib import Path
import random
import math

sys.path.append(str(Path(__file__).resolve().parent.parent))

from validaciones import validar_numero
from tda_colas import Cola, nodoCola, arribo, atencion, mover_al_final, cola_vacia, barrido, en_frente, tamanio

enteros = Cola()
negativos = Cola()

def validar_numero2(entrada):
    numero = 0
    while True:
        try:
            entrada = input(entrada)
            numero = int(entrada)
            return numero
        except:
            print("El numero ingresado es incorrecto, por favor ingrese otro.")

cantidad = validar_numero("Ingrese la cantidad de numeros a añadir a la cola: ")
maximo = 0
minimo = 0
primero = True
for i in range (0, cantidad):
    numero = math.floor(random.random() * random.randint(-1000, 1000))
    if (primero):
        maximo = numero
        minimo = numero

        primero = False
    else:
        if (numero > maximo): maximo = numero
        if (numero < minimo): minimo = numero

    if (numero < 0): arribo(negativos, numero)
    arribo(enteros, numero)

if (cantidad > 0):
    rango = maximo - minimo
    print(f"El rango de los numeros es de: {rango}.")
    print(f"El numero maximo fue: {maximo}")
    print(f"El numero minimo fue: {minimo}")

print(f"La cantidad de numeros negativos es: {tamanio(negativos)} numeros.")
