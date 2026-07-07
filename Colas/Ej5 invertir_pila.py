"""
Utilizando operaciones de cola y pila, invertir el contenido de una pila.
"""
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from validaciones import validar_string
from tda_colas import Cola, nodoCola, arribo, atencion, mover_al_final, cola_vacia, en_frente, tamanio
from Pilas.pilas import Pila, apilar, desapilar, pila_vacia, barrido

cola = Cola()
pila = Pila()

# ingreso de datos
letra = validar_string('Ingrese un caracter, para salir presione enter sin ingresar caracteres: ')
while (letra != ''):
    if (letra.isalpha() and len(letra) == 1):
        apilar(pila, letra)
    else:
        print("Debe ingresar una letra sola del abecedario")
    letra = validar_string('Ingrese un caracter, para salir presione enter sin ingresar caracteres: ')

# si hay datos ejecutamos la funcion
if (not pila_vacia(pila)):
    # mostramos la pila antes de invertirla
    print("antes de invertir la pila")
    barrido(pila)

    # invertimos la pila
    while (not pila_vacia(pila)):
        x = desapilar(pila)
        arribo(cola, x)

    while (not cola_vacia(cola)):
        x = atencion(cola)
        apilar(pila, x)

    # mostramos la pila invertida
    print("despues")
    barrido(pila)
else:
    print("No hay datos para realizar la operacion.")
