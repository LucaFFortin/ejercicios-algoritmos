"""
Utilizando operaciones de cola y pila, invertir el contenido de una pila.
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from tda_colas import Cola, nodoCola, arribo, atencion, mover_al_final, cola_vacia, barrido, en_frente, tamanio
from Pilas.pilas import Pila, apilar, desapilar, pila_vacia, barrido
from validaciones import validar_string


cola = Cola()
pila = Pila()

letra = validar_string('Ingrese un caracter, para salir presione enter sin ingresar caracteres: ')
while (letra != ''):
    apilar(pila, letra)
    letra = validar_string('Ingrese un caracter, para salir presione enter sin ingresar caracteres: ')

print("antes de invertir la pila")
barrido(pila)

while (not pila_vacia(pila)):
    x = desapilar(pila)
    arribo(cola, x)

while (not cola_vacia(cola)):
    x = atencion(cola)
    apilar(pila, x)

print("despues")
barrido(pila)

