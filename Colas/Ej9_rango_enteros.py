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

# se pide ingresar un numero que indica la cantidad de numeros a generar aleatoriamente
cantidad = validar_numero("Ingrese la cantidad de numeros a añadir a la cola: ")
maximo = 0
minimo = 0
primero = True

# si se ingreso una cantidad menor a 1 se cancela la ejecucion.
if (cantidad <= 0):
    print("La cantidad de numero a generar debe ser mayor o igual a 1.")
else:    
    # se generan e ingresan los numeros dentro de una cola
    # se calculan los maximos y minimos de esa funcion
    for i in range (0, cantidad):
        numero = math.floor(random.random() * random.randint(-1000, 1000))
        # si es el primer numero entonces asiganmos ese valora maximo y minimo
        if (primero):
            maximo = numero
            minimo = numero

            primero = False
        # sino los calculamos
        else:
            if (numero > maximo): maximo = numero
            if (numero < minimo): minimo = numero

    # si el numero es negativo lo ingresamos a una cola de negativos
    if (numero < 0): arribo(negativos, numero)
    arribo(enteros, numero)

    # calculamos el rango
    rango = maximo - minimo

    # imprimimos los datos solicitados por el ejercicio
    print(f"El rango de los numeros es de: {rango}.")
    print(f"El numero maximo fue: {maximo}")
    print(f"El numero minimo fue: {minimo}")
    print(f"La cantidad de numeros negativos es: {tamanio(negativos)} numeros.")
