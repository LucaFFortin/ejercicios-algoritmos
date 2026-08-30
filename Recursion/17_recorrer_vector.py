import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from utils import limpiar
from validaciones import validar_string, validar_numero

def recorrer_recursivo(vector):
    if (len(vector) <= 1):
        print(vector[0])
    else:
        item = vector[-1]
        print(item)
        return recorrer_recursivo(vector[:-1])

# main
limpiar()

array = []

while(True):
    opcion = validar_numero("Opciones: 1 = ingresar elemento, 0 = salir: ")

    while opcion not in [0, 1]:
        opcion = validar_numero("Opcion incorrecta, use una de las opciones: 1 = ingresar elemento, 0 = salir: ")

    if opcion == 0: break

    elemento = validar_string("Ingrese el elemento a guardar: ")
    array.append(elemento)
        

if (len(array) == 0):
    print("No se an ingresado elementos, se cancela la ejecucion del programa.")
else:
    print("El recorrido del array de manera inversa es:")
    recorrer_recursivo(array)