from pilas import Pila, nodoPila, apilar, desapilar, pila_vacia

def ocurrencias_valor(pila, valor):
    paux = Pila()
    cont_ocurrencias = 0
    while (not pila_vacia(pila)):
        dato = desapilar(pila)
        if (dato.info == valor):
            cont_ocurrencias += 1
        apilar(paux, dato)
    
    while (not pila_vacia(paux)):
        dato = desapilar(paux)
        apilar(pila, dato)
    
    print(f"Ocurrencias del valor {valor} en la pila es de: {cont_ocurrencias} veces")

# main
print("Ingrese los datos de la Pila:")
pila = Pila()
while(True):
    nodo = nodoPila()
    nodo.info = input("Ingrese el dato que quiere guardar en la pila: S para salir: ")
    if (nodo.info == "S"): break
    apilar(pila, nodo)

entrada = input("Ingrese el valor que quieres contar: ")
ocurrencias_valor(pila, entrada)

