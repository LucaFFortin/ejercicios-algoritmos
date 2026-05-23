from pilas import nodoPila, Pila, apilar, desapilar, pila_vacia, en_cima, tamanio, barrido

"""
asumiendo que los nodos guardan la informacion de la siguiente manera
Nodo.info: [
    modelo: string,
    pelicula: string,
    estado: [dañado, impecable, destruido]
]
"""
# a
def hulkbuster_utilizado(pila):
    paux = Pila()
    usado = False
    peliculas = []
    while (not pila_vacia(pila)):
        modelo, pelicula, estado = desapilar(pila)
        if (modelo == "Mark XLIV"):
            usado = True
            peliculas.append(pelicula)
        apilar(paux, [modelo, pelicula, estado])

    while (not pila_vacia(paux)):
        modelo, pelicula, estado= desapilar(paux)
        apilar(pila, [modelo, pelicula, estado])
    
    if (not usado):
        print("El modelo Mark XLIV (Hulkbuster) no fue utilizado.") 
        return 
    print("El modelo Mark XLIV (Hulkbuster) fue utilizado en las siguientes peliculas: ")
    for pelicula in peliculas:
        print(pelicula)

# b
def modelos_dañados(pila):
    paux = Pila()
    dañados = []
    while (not pila_vacia(pila)):
        modelo, pelicula, estado = desapilar(pila)
        if (estado == "dañado"):
            dañados.append(modelo)
        apilar(paux, [modelo, pelicula, estado])

    while (not pila_vacia(paux)):
        modelo, pelicula, estado = desapilar(paux)
        apilar(pila, [modelo, pelicula, estado])
    
    if (len(dañados) == 0): 
        print("No hay modelos dañados")
        return 
    print("Estos son los modelos dañados: ")
    for modelo in dañados:
        print(f"Modelo: {modelo}")

# c
def eliminar_modelos_dañados(pila):
    paux = Pila()
    while (not pila_vacia(pila)):
        modelo , pelicula, estado = desapilar(pila)
        if (not estado == "dañado"):
            apilar(paux, [modelo, pelicula, estado])
        print(f"Modelo destuido: {modelo}")

    while (not pila_vacia(paux)):
        modelo, pelicula, estado = desapilar(paux)
        apilar(paux, [modelo, pelicula, estado])

# e
def añadir_modelo(pila, modelo_insertar):
    paux = Pila()
    modelo_en_pila = False
    insertado = False

    if (pila_vacia(pila)):
        apilar(pila, modelo_insertar)
        return

    while (not pila_vacia(pila)):
        modelo , pelicula, estado= desapilar(pila)
        
        if (modelo == modelo_insertar[0] and pelicula == modelo_insertar[1]):
            modelo_en_pila = True
        apilar(paux, [modelo, pelicula, estado])

    while (not pila_vacia(paux)):
        if (not modelo_en_pila and not insertado):
            insertado = True
            apilar(pila, modelo_insertar)
        modelo , pelicula, estado= desapilar(paux)
    apilar(pila, [modelo, pelicula, estado])

    if (not insertado):
        print("El modelo y la pelicula ya estan ingresados esta en la pila")

def mostrar_trajes(pila, modelo_mostrar):
    paux = Pila()
    peliculas = []
    while (not pila_vacia(pila)):
        modelo, pelicula, estado = desapilar(pila)
        if (modelo == modelo_mostrar[0]):
            peliculas.append(pelicula)
        apilar(paux, {"modelo": modelo, "peliculas": peliculas, "estado": estado})

    while (not pila_vacia(paux)):
        modelo , peliculas, estado = desapilar(paux)
        apilar(pila, {"modelo": modelo, "peliculas": peliculas, "estado": estado})

    print(f"El modelo {modelo_mostrar[0]} fue utilizado en las siguientes peliculas: ")
    for pelicula in peliculas:
        print(f"{pelicula}.")

# main
pila = Pila()
while(True):
    entrada = input("Ingrese 1 ingresar un modelo, 2 = revisar si esta hulkbuster, 3 = listar modelos dañados, 4 = eliminar modelos dañados, 5 = mostrar peliculas en las que fue usado un traje, 0 para salir: ")

    if (entrada == "0"): break
    if (entrada == "1"):
        pelicula = input("Ingrese el nombre de la pelicula: ")
        modelo = input("Ingrese el modelo utilizado en la pelicula: ")
        estado = input("Ingrese el estado del modelo: ")
        añadir_modelo(pila, [modelo, pelicula, estado])
    if (entrada == "2"):
        hulkbuster_utilizado(pila)
    if (entrada == "3"):
        modelos_dañados(pila)
    if (entrada == "4"):
        eliminar_modelos_dañados(pila)
    if (entrada == "5"):
        traje = input("Ingrese el modelo a mostrar los trajes utilizados: ")
        mostrar_trajes(pila, traje)
