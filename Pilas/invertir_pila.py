from pilas import nodoPila, Pila, apilar, desapilar, pila_vacia, barrido

def invertir_pila(pila):
    paux = Pila()
    while (not pila_vacia(pila)):
        elem = desapilar(pila)
        apilar(paux, elem)
    
    return paux

# main
print("Ingrese los datos de la Pila:")
pila = Pila()
while(True):
    nodo = input("Ingrese el dato que quiere guardar en la pila: S para salir: ")
    if (nodo == "S"): break
    apilar(pila, nodo)

print("Pila antes de invertirla:")
barrido(pila)

print("Pila despues de invertirla: ")
pila = invertir_pila(pila)
barrido(pila)
