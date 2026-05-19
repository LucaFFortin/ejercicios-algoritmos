from pilas import nodoPila, Pila, apilar, desapilar, pila_vacia, barrido
import random

cartas = Pila()
p_espada, p_basto, p_copa, p_oro = None, None, None, None

def agregar_carta(pila):
    numero = random.randrange(1, 11)
    palo = random.choice(["basto", "oro", "copa", "espada"])
    nodo = nodoPila()
    nodo.info = [numero, palo]
    apilar(pila, nodo)

def separar_palos(pila):
    p_copa = Pila()
    p_basto = Pila()
    p_oro = Pila()
    p_espada = Pila()

    while (not pila_vacia(pila)):
        carta = desapilar(pila)
        if (carta.info[1] == "basto"):
            apilar(p_basto, carta)
        if (carta.info[1] == "oro"):
            apilar(p_oro, carta)
        if (carta.info[1] == "copa"):
            apilar(p_copa, carta)
        if (carta.info[1] == "espada"):
            apilar(p_espada, carta)

    return [p_espada, p_basto, p_copa, p_oro]

def ordenar_palo(cartas):
    lista = []
    while (not pila_vacia(cartas)):
        x = desapilar(cartas)
        lista.append(x.info)
    lista.sort()
    while(len(lista) > 0):
        x = lista.pop()
        nodo = nodoPila()
        nodo.info = x
        apilar(cartas, nodo)

# main
while(True):
    opcion = input("Elige una opcion: 1 - Agregar carta, 2 - separar por palo, 3 - Ordenar palo, 0 para salir: ")
    if (opcion == "0"): break
    elif (opcion == "1"):
        agregar_carta(cartas)
        print("La carta a sido agregada")
        barrido(cartas)
    elif (opcion == "2"):
        p_espada, p_basto, p_copa, p_oro = separar_palos(cartas)
        print("Espada:")
        if (p_espada.tamanio == 0):
            print("No hay cartas")
        else:
            barrido(p_espada)

        print("Basto:")
        if (p_basto.tamanio == 0):
            print("No hay cartas")
        else:
            barrido(p_basto)

        print("Copa:")
        if (p_copa.tamanio == 0):
            print("No hay cartas")
        else:
            barrido(p_copa)

        print("Oro:")
        if (p_oro.tamanio == 0):
            print("No hay cartas")
        else:
            barrido(p_oro)
    elif (opcion == "3"):
        opcion = input("Elige un palo: 1 - Espada, 2 - Basto, 3 - Copa, 4 - Oro: ")
        if (opcion == "1"):
            ordenar_palo(p_espada)
            barrido(p_espada)
        elif (opcion == "2"):
            ordenar_palo(p_basto)
            barrido(p_basto)
        elif (opcion == "3"):
            ordenar_palo(p_copa)
            barrido(p_copa)
        elif (opcion == "4"):
            ordenar_palo(p_oro)
            barrido(p_oro)
    else:
        print("Opcion incorrecta.")

