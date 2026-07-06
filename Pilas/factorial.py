import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from validaciones import validar_numero
from pilas import nodoPila, Pila, apilar, desapilar, pila_vacia

def factorial_pila(num):
    paux = Pila()
    for i in range(1, num + 1):
        nodo = i
        apilar(paux, nodo)

    acc = 1
    while (not pila_vacia(paux)):
        x = desapilar(paux)
        acc *= x

    return acc

# main
try:
    entrada = validar_numero("Ingrese el numero a factorizar: ")
    entrada_factorizada = factorial_pila(entrada)
    print(f"El numero {entrada} factorizado es: {entrada_factorizada}")
except:
    print("Se debe ingresar un numero valido.")

