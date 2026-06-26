from pilas import nodoPila, Pila, apilar, desapilar, pila_vacia, en_cima, tamanio, barrido

def lista_a_pila(lista, pila):
    for i in lista:
        nodo = i
        apilar(pila, nodo)

def es_palindromo(cadena):
    pila = Pila()
    pila2 = Pila()
    cadena = list(cadena)
    lista_a_pila(cadena, pila2)
    
    cadena.reverse()
    lista_a_pila(cadena, pila)

    palindromo = True

    if (pila.tamanio != pila2.tamanio): palindromo = False

    while (not pila_vacia(pila) and not pila_vacia(pila2)):
        elem1 = desapilar(pila)
        elem2 = desapilar(pila2)
        
        if (not elem1 == elem2): palindromo = False
    
    return palindromo

# main
entrada = input("Ingrese la palabra a verificar: ")
if (entrada == ""):
    print("La entrada esta vacia, no se puede realizar el proceso.")
else:
    resultado = es_palindromo(entrada)
    if (resultado):
        print(f"{entrada} es palindromo")
    else:
        print(f"{entrada} no es palindromo")


