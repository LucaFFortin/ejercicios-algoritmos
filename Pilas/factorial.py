from pilas import nodoPila, Pila, apilar, desapilar, pila_vacia

def factorial_pila(num):
    paux = Pila()
    for i in range(1, num + 1):
        nodo = nodoPila()
        nodo.info = i
        apilar(paux, nodo)

    acc = 1
    while (not pila_vacia(paux)):
        x = desapilar(paux)
        acc *= x.info

    return acc

# main
entrada = int(input("Ingrese el numero a factorizar: "))
entrada_factorizada = factorial_pila(entrada)
print(f"El numero {entrada} factorizado es: {entrada_factorizada}")


