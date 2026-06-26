import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from tda_colas import Cola, nodoCola, arribo, atencion, mover_al_final, cola_vacia, barrido, en_frente, tamanio
from Pilas.pilas import Pila, apilar, desapilar, pila_vacia
from validaciones import validar_string

cola = Cola()
pila = Pila()

letra = validar_string('Ingrese un caracter, para salir presione enter sin ingresar caracteres: ')
while (letra != ''):
    arribo(cola, letra)
    letra = validar_string('Ingrese un caracter, para salir presione enter sin ingresar caracteres: ')

print("Cola antes de invertirla:")
barrido(cola)

while (not cola_vacia(cola)):
    x = atencion(cola)
    apilar(pila, x)

while (not pila_vacia(pila)):
    x = desapilar(pila)
    arribo(cola, x)

print("Cola despues de invertirla: ")
barrido(cola)

