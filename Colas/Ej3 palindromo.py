import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from tda_colas import Cola, nodoCola, arribo, atencion, mover_al_final, cola_vacia, barrido, en_frente, tamanio
from Pilas.pilas import Pila, apilar, desapilar, pila_vacia
from validaciones import validar_string


cola = Cola()
pila = Pila()

palabra = validar_string("Ingrese una palabra a analizar si es palindromo: ")
valid = True

for char in palabra:
    arribo(cola, char)
    apilar(pila, char)

while (not cola_vacia(cola) and not pila_vacia(pila)):
    cola_char = atencion(cola)
    pila_char = desapilar(pila)
    if (cola_char != pila_char): valid = False

if (valid): print("La palabra ingresada es palindromo!")
else: print("La palabra ingresada no es un palindromo")