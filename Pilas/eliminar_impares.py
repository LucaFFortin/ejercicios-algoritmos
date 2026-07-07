import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from validaciones import validar_numero, validar_string
from pilas import nodoPila, Pila, apilar, desapilar, pila_vacia, barrido

def eliminar_impares(pila):
    paux = Pila()
    while (not pila_vacia(pila)):
        dato = desapilar(pila)
        if (dato % 2 == 0):
            apilar(paux, dato)
            
    print("Datos que quedaron en la pila")
    while (not pila_vacia(paux)):
        dato = desapilar(paux)
        print(dato)
        apilar(pila, dato)

# main
print("Ingrese los datos de la Pila:")
pila = Pila()
while(True):
    # se mantiene input porque
    nodo = input("Ingrese el dato que quiere guardar en la pila: ")
    salir = validar_string("Si desea salir ingrese la letra S, sino ingrese otra cosa: ")
    if (salir == "S"): break
    try:
        nodo = int(nodo)
        apilar(pila, nodo)
    except:
        print("Debes ingresar un numero valido.")

print("Pila antes de eliminar los impares: ")
barrido(pila)

eliminar_impares(pila)
