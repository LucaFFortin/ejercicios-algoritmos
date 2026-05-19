from pilas import nodoPila, Pila, apilar, desapilar, pila_vacia, en_cima, tamanio, barrido

def lista_a_pila(lista, pila):
    for i in lista:
        nodo = nodoPila()
        nodo.info = i
        apilar(pila, nodo)

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
entrada = list(input("Ingrese el texto a analizar: "))
pila = Pila()
lista_a_pila(entrada, pila)

cont, vocales = contar_vocales(pila)

print(f"La cantidad de vocales es de {cont} vocales")
for i, valor in vocales.items():
    print(f"La letra {i} aparecio {valor} veces.")


