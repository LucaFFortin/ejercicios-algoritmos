from pilas import nodoPila, Pila, apilar, desapilar, pila_vacia, en_cima, tamanio, barrido

def lista_a_pila(lista, pila):
    for i in lista:
        nodo = i
        apilar(pila, nodo)

def ver_palabra_inversa(cadena):
    lista = list(cadena)
    pila = Pila()
    lista_a_pila(lista, pila)
    lista = []
    while (not pila_vacia(pila)):
        x = desapilar(pila)
        lista.append(x)

    return "".join(lista)

# main
entrada = input("Ingrese la palabra a invertir: ")
print(f"La palabra invertida es: {ver_palabra_inversa(entrada)}")