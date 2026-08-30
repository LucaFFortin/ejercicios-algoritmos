import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from utils import limpiar
from validaciones import validar_string, validar_numero

def recorrer_recursivo(vector):
    if (len(vector) <= 1):
        print(vector[0])
        return vector[0]
    else:
        item = vector[0]
        print(item)
        return recorrer_recursivo(vector[1:])

def recorrer_matriz(matriz):
    if (len(matriz) == 1): recorrer_recursivo(matriz[0])
    else:
        vector = matriz[0]
        recorrer_recursivo(vector)
        recorrer_matriz(matriz[1:])


# main
limpiar()

matriz = []

while(True):
    opcion = validar_numero("Opciones: 1 = ingresar vector, 0 = salir: ")

    while opcion not in [0, 1]:
        opcion = validar_numero("Opcion incorrecta, use una de las opciones: 1 = ingresar vector, 0 = salir: ")

    if opcion == 0: break

    vector = []

    while(True):
        opcion_interna = validar_numero("Opciones: 1 = ingresar elemento al vector, 0 = salir: ")

        while opcion_interna not in [0, 1]:
            opcion_interna = validar_numero("Opcion incorrecta, use una de las opciones: 1 = ingresar elemento al vector, 0 = salir: ")

        if opcion_interna == 0: break

        elemento = validar_string("Ingrese el elemento a guardar: ")
        vector.append(elemento)

    if (len(vector) > 1): matriz.append(vector)

if (len(matriz) == 0):
    print("No se an ingresado elementos, se cancela la ejecucion del programa.")
else:
    print("El recorrido de la matriz es:")
    recorrer_matriz(matriz)