import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from pilas import Pila, nodoPila, apilar, desapilar, pila_vacia, en_cima, tamanio, barrido
from validaciones import validar_string

# funcion para extraer los elementos de una lista y apilarlos a una pila
def lista_a_pila(lista, pila):
    for i in lista:
        nodo = nodoPila()
        nodo.info = i
        apilar(pila, nodo)

# cuenta las vocales de una pila
def contar_vocales(pila):
    cont = 0
    vocales = {
        "a": 0,
        "e": 0,
        "i": 0,
        "o": 0,
        "u": 0,
    }
    paux = Pila()
    while (not pila_vacia(pila)):
        x = desapilar(pila)
        copy = x.info.lower()
        if (copy in ["a", "e", "i", "o", "u"]):
            cont += 1
            vocales[copy] += 1
        apilar(paux, x)

    while (not pila_vacia(paux)):
        x = desapilar(paux)
        apilar(pila, x)

    return [cont, vocales]

# main
entrada = list(validar_string("Ingrese el texto a analizar: "))
pila = Pila()
lista_a_pila(entrada, pila)

cont, vocales = contar_vocales(pila)

print(f"La cantidad de vocales es de {cont} vocales")
for i, valor in vocales.items():
    print(f"La letra {i} aparecio {valor} veces.")


