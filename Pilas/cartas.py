from pilas import Pila, apilar, desapilar, pila_vacia, en_cima, tamanio, barrido
import random

mazo = Pila()
pila_oro = Pila()
pila_basto = Pila()
pila_espada = Pila()
pila_copa = Pila()

while tamanio(mazo) < 48:

    numero = random.randint(1, 12)
    palo = random.choice(["oro", "basto", "espada", "copa",])
    carta = [palo, numero]
        
    carta_existe = False
    paux = Pila()
    while (not pila_vacia(mazo)):
        dato = desapilar(mazo)
        apilar(paux, dato)

    while (not pila_vacia(paux)):
        dato = desapilar(paux)
        if (dato == carta): carta_existe = True
        apilar(mazo, dato)

    if (not carta_existe): apilar(mazo, carta)

print("Cartas en el mazo:")
barrido(mazo)

while pila_vacia(mazo) == False:
    carta = desapilar(mazo)

    if carta[0] == "oro":
        apilar(pila_oro, carta)
    elif carta[0] == "basto":
        apilar(pila_basto, carta)
    elif carta[0] == "espada":
        apilar(pila_espada, carta)
    else:
        apilar(pila_copa, carta)

def ordenar_cartas_palo (pila, palo):
    pila_auxiliar = Pila()
    while pila_vacia(pila) == False:
        carta = desapilar(pila)

        while pila_vacia(pila_auxiliar)== False and (en_cima(pila_auxiliar)[1] > carta[1]):
            apilar(pila, desapilar(pila_auxiliar))
        apilar(pila_auxiliar, carta)
    while pila_vacia(pila_auxiliar) == False:
        apilar(pila, desapilar(pila_auxiliar))

    print(f"Pila de {palo} ordenada:")

    barrido(pila)


ordenar = input("que pila quiere ordenar: oro, basto, espada, copa: ").lower()
if ordenar == "oro":
    ordenar_cartas_palo(pila_oro, ordenar)
elif ordenar == "basto":
    ordenar_cartas_palo(pila_basto, ordenar)
elif ordenar == "espada":
    ordenar_cartas_palo(pila_espada, ordenar)
elif ordenar == "copa":
    ordenar_cartas_palo(pila_copa, ordenar)
else:
    print("El palo ingresado no es reconocido por el sistema.")