import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from validaciones import validar_numero
from pilas import Pila, apilar, desapilar, pila_vacia, en_cima, tamanio, barrido


def borrar_elemento(pila, posicion):
    pos = 0

    if (posicion > pila.tamanio): 
        print("posicion incorrecta, es mayor al tamaño de la pila")
        return
    
    if (posicion < 0): 
        print("posicion incorrecta, debe ser mayor a 0")
        return

    paux = Pila()
    while (not pila_vacia(pila)):
        x = desapilar(pila)
        pos += 1
        if (not pos == posicion):
            apilar(paux, x)

    while(not pila_vacia(paux)):
        x = desapilar(paux)
        apilar(pila, x)

# main
print("Ingrese los datos de la Pila:")
pila = Pila()
while(True):
    # se mantiene input porque queremos que ingrese cualquier dato como string
    nodo = input("Ingrese el dato que quiere guardar en la pila: S para salir: ")
    if (nodo == "S"): break
    apilar(pila, nodo)

invalida = False
entrada = validar_numero("Ingrese la posicion del numero a eliminar: ")
if (entrada < 0 or entrada > tamanio(pila)): 
    print("La entrada debe ser un numero mayor a cero y menor al tamaño de la pila.")
    invalida = True

if (not invalida):
    print("Antes de borrar el elemento: ")
    barrido(pila)

    borrar_elemento(pila, entrada)

    print("Despues de borrar el elemento: ")
    barrido(pila)
