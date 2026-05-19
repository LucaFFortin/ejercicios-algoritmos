from pilas import nodoPila, Pila, apilar, desapilar, pila_vacia, barrido

def reemplazar_valor(pila, valor, nuevo_valor):
    paux = Pila()
    while (not pila_vacia(pila)):
        dato = desapilar(pila)
        if (dato.info == valor):
            dato.info = nuevo_valor
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
    apilar(pila, nodo)

valor_a_cambiar = input("Ingrese el valor a cambiar: ")
valor_nuevo = input("Ingrese el nuevo valor: ")

print("Pila antes de cambiar el valor: ")
barrido(pila)

reemplazar_valor(pila, valor_a_cambiar, valor_nuevo)