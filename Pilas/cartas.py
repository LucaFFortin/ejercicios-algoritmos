from pilas import Pila, apilar, desapilar, pila_vacia, en_cima, tamanio, barrido
import random

mazo = Pila()
pila_oro = Pila()
pila_basto = Pila()
pila_espada = Pila()
pila_copa = Pila()
pila_auxiliar = Pila()

cartas_usadas = []

while tamanio(mazo) < 48:

    numero = random.randint(1, 12)
    palo = random.choice(["oro", "basto", "espada", "copa",])
    carta = [palo, numero]

    if carta not in cartas_usadas:
        cartas_usadas.append(carta)
        apilar(mazo, carta)
        print(carta)


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

ordenar = input("que pila quiere ordenar: oro, basto, espada, copa: ").lower()
if ordenar == "oro":
    while pila_vacia(pila_oro) == False:
        carta = desapilar(pila_oro)

        while pila_vacia(pila_auxiliar)== False and (en_cima(pila_auxiliar)[1] > carta[1]):
            apilar(pila_oro, desapilar(pila_auxiliar))
        apilar(pila_auxiliar, carta)
    while pila_vacia(pila_auxiliar) == False:
        apilar(pila_oro, desapilar(pila_auxiliar))

    print("Pila de oro ordenada:")

    barrido(pila_oro)

elif ordenar == "basto":
    while pila_vacia(pila_basto) == False:
        carta = desapilar(pila_basto)

        while pila_vacia(pila_auxiliar)== False and (en_cima(pila_auxiliar)[1] > carta[1]):
            apilar(pila_basto, desapilar(pila_auxiliar))
        apilar(pila_auxiliar, carta)
    while pila_vacia(pila_auxiliar) == False:
        apilar(pila_basto, desapilar(pila_auxiliar))

    print("Pila de basto ordenada:")

    barrido(pila_basto)

elif ordenar == "espada":
    while pila_vacia(pila_espada) == False:
        carta = desapilar(pila_espada)

        while pila_vacia(pila_auxiliar)== False and (en_cima(pila_auxiliar)[1] > carta[1]):
            apilar(pila_espada, desapilar(pila_auxiliar))
        apilar(pila_auxiliar, carta)
    while pila_vacia(pila_auxiliar) == False:
        apilar(pila_espada, desapilar(pila_auxiliar))

    print("Pila de espada ordenada:")

    barrido(pila_espada)
elif ordenar == "copa":
    while pila_vacia(pila_copa) == False:
        carta = desapilar(pila_copa)

        while pila_vacia(pila_auxiliar)== False and (en_cima(pila_auxiliar)[1] > carta[1]):
            apilar(pila_copa, desapilar(pila_auxiliar))
        apilar(pila_auxiliar, carta)
    while pila_vacia(pila_auxiliar) == False:
        apilar(pila_copa, desapilar(pila_auxiliar))

    print("Pila de copa ordenada:")

    barrido(pila_copa)
else:
    print("Opcion incorrecta.")