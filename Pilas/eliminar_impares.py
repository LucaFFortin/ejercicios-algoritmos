from pilas import nodoPila, Pila, apilar, desapilar, pila_vacia, barrido

def eliminar_impares(pila):
    paux = Pila()
    while (not pila_vacia(pila)):
        dato = desapilar(pila)
        if (dato.info % 2 == 0):
            apilar(paux, dato)
            
    print("Datos que quedaron en la pila")
    while (not pila_vacia(paux)):
        dato = desapilar(paux)
        print(dato.info)
        apilar(pila, dato)

# main
print("Ingrese los datos de la Pila:")
pila = Pila()
while(True):
    nodo = nodoPila()
    nodo.info = input("Ingrese el dato que quiere guardar en la pila: S para salir: ")
    if (nodo.info == "S"): break
    nodo.info = int(nodo.info)
    apilar(pila, nodo)

print("Pila antes de eliminar los impares: ")
barrido(pila)

eliminar_impares(pila)
