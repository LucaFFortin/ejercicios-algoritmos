import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from utils import limpiar
from validaciones import validar_numero

def busqueda_secuencial_centinela(valor_buscado, lista, posicion=1):

    # if (len(lista) == 1): print(f"No se encontro el valor buscado: {valor_buscado}.")
    # else:
    #     elemento = lista[0]

    #     if (elemento == valor_buscado): print(f"Se encontro el valor {valor_buscado}.")
        
    #     busqueda_secuencial_centinela(valor_buscado, lista[1:])

    if (lista[0] == valor_buscado): return posicion
    else: return busqueda_secuencial_centinela(valor_buscado, lista[1:], posicion = posicion + 1)

# main
limpiar()

array = [1,2,3,4000]

# while(True):
#     opcion = validar_numero("Opciones: 1 = ingresar elemento, 0 = salir: ")

#     while opcion not in [0, 1]:
#         opcion = validar_numero("Opcion incorrecta, use una de las opciones: 1 = ingresar elemento, 0 = salir: ")

#     if opcion == 0: break

#     elemento = validar_numero("Ingrese el elemento a guardar: ")
#     array.append(elemento)
        
valor_buscado = validar_numero("Ingrese el valor a comparar en la lista: ")

array.append(valor_buscado)

if (len(array) == 1):
    print("No se an ingresado elementos, se cancela la ejecucion del programa.")
else:
    posicion = busqueda_secuencial_centinela(valor_buscado, array)
    if (len(array) == posicion): print(f"No se encontro el elemento en la lista.")
    else: print(f"Se encontro el elemento en la posicion {posicion}")