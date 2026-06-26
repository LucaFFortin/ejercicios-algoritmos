from pilas import nodoPila, Pila, apilar, desapilar, pila_vacia, en_cima, tamanio, barrido

def encontrar_personajes(pila):
    paux = Pila()
    encontrado = False
    personajes = []
    while (not pila_vacia(pila)):
        x = desapilar(pila)
        if (x in ["Leia Organa", "Boba Fett"]):
            encontrado = True
            personajes.append(x )
        apilar(paux, x)

    while (not pila_vacia(paux)):
        x = desapilar(paux)
        apilar(pila, x)
    
    return [encontrado, personajes]


# main
print("Ingrese personajes a la Pila:")
pila = Pila()
while(True):
    nodo  = input("Ingrese el personaje que quiere guardar en la pila: S para salir: ")
    if (nodo  == "S"): break
    apilar(pila, nodo)

encontrado, personajes = encontrar_personajes(pila)
if (encontrado):
    for p in personajes:    
        print(f"Se encontro el personaje: {p}")
else:
    print("No se encontro a Leia Organa ni a Boba Fett")