from pilas import Pila, nodoPila, apilar, desapilar, pila_vacia

def ocurrencias_valor(pila, valor):
    paux = Pila()
    cont_ocurrencias = 0
    while (not pila_vacia(pila)):
        dato = desapilar(pila)
        if (dato == valor):
            cont_ocurrencias += 1
        apilar(paux, dato)
    
    while (not pila_vacia(paux)):
        dato = desapilar(paux)
        apilar(pila, dato)
    if (cont_ocurrencias == 0):
        print(f"No se encontraron ocurrecias del valor {valor}.")
    elif (cont_ocurrencias == 1):    
        print(f"Ocurrencias del valor {valor} en la pila es de: {cont_ocurrencias} vez.")
    else:
        print(f"Ocurrencias del valor {valor} en la pila es de: {cont_ocurrencias} veces.")

# main
print("Ingrese los datos de la Pila:")
pila = Pila()
while(True):
    nodo = input("Ingrese el dato que quiere guardar en la pila: S para salir: ")
    if (nodo == "S"): break
    apilar(pila, nodo)

entrada = input("Ingrese el valor que quieres contar: ")
ocurrencias_valor(pila, entrada)

