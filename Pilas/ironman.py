from pilas import nodoPila, Pila, apilar, desapilar, pila_vacia, en_cima, tamanio, barrido

"""
asumiendo que los nodos guardan la informacion de la siguiente manera
Nodo: [
    modelo: string,
    pelicula: string,
    estado: [dañado, impecable, destruido]
]
"""

string_entrada = """Eliga una opcion a realizar: 
1 = ingresar un modelo, 
2 = revisar si esta hulkbuster, 
3 = listar modelos dañados, 
4 = eliminar modelos dañados, 
5 = insertar el modelo Mark LXXXV, 
6 = mostrar peliculas en las que fue usado un traje, 0 para salir: """

estados_trajes = ["dañado", "impecable", "destruido"]

# con requerimiento del item d
def añadir_modelo(pila, modelo_insertar):
    paux = Pila()
    modelo_en_pila = False

    if (pila_vacia(pila)):
        apilar(pila, modelo_insertar)
        return

    while (not pila_vacia(pila)):
        [modelo, pelicula, estado]= desapilar(pila)
        
        if (modelo == modelo_insertar[0] and pelicula == modelo_insertar[1]):
            modelo_en_pila = True
        apilar(paux, [modelo, pelicula, estado])

    if (modelo_en_pila):
        print("El modelo y la pelicula ya estan ingresados esta en la pila")

    while (not pila_vacia(paux)):
        if (not modelo_en_pila):
            modelo_en_pila = True
            apilar(pila, modelo_insertar)
        [modelo, pelicula, estado] = desapilar(paux)
    apilar(pila, [modelo, pelicula, estado])

# a
def hulkbuster_utilizado(pila):
    paux = Pila()
    usado = False
    peliculas = []
    while (not pila_vacia(pila)):
        [modelo, pelicula, estado] = desapilar(pila)
        if (modelo == "Mark XLIV"):
            usado = True
            peliculas.append(pelicula)
        apilar(paux, [modelo, pelicula, estado])

    while (not pila_vacia(paux)):
        [modelo, pelicula, estado] = desapilar(paux)
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
        [modelo, pelicula, estado] = desapilar(pila)
        if (estado == "dañado"):
            dañados.append(modelo)
        apilar(paux, [modelo, pelicula, estado])

    while (not pila_vacia(paux)):
        [modelo, pelicula, estado] = desapilar(paux)
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
        [modelo , pelicula, estado] = desapilar(pila)
        if (not estado == "dañado"):
            apilar(paux, [modelo, pelicula, estado])
        print(f"Modelo destuido: {modelo}")

    if (pila_vacia(paux)):
        print("No hay modelos dañados en la pila, por lo tanto no se eliminaron modelos de esta.")

    while (not pila_vacia(paux)):
        [modelo, pelicula, estado] = desapilar(paux)
        apilar(paux, [modelo, pelicula, estado])

# e
def insertar_Mark_LXXXV(pila):
    paux = Pila()
    modelo_en_pila = False

    if (pila_vacia(pila)):
        apilar(pila, ["Mark LXXXV", "Avengers: Endgame", "Impecable"])
        return

    while (not pila_vacia(pila)):
        [modelo , pelicula, estado] = desapilar(pila)
        
        if (modelo == "Mark LXXXV"):
            modelo_en_pila = True
        apilar(paux, [modelo, pelicula, estado])

    if (modelo_en_pila):
        print("El modelo ya esta ingresado esta en la pila")
        return
    else:
        print("El modelo fue insertado en la pila.")

    while (not pila_vacia(paux)):
        if (not modelo_en_pila):
            modelo_en_pila = True
            apilar(pila, ["Mark LXXXV", "Avengers: Endgame", "Impecable"])
        [modelo, pelicula, estado] = desapilar(paux)
    apilar(pila, [modelo, pelicula, estado])

# f
def mostrar_trajes(pila, pelicula_mostrar):
    paux = Pila()
    modelos = []
    while (not pila_vacia(pila)):
        [modelo, pelicula, estado] = desapilar(pila)
        if (pelicula == pelicula_mostrar):
            modelos.append(modelo)
        apilar(paux, [modelo, pelicula, estado])

    while (not pila_vacia(paux)):
        x = desapilar(paux)
        apilar(pila, x)

    print(f"En la pelicula {pelicula_mostrar} fueron utilizados los siguientes modelos: ")
    for modelo in modelos:
        print(f"Modelo: {modelo}.")

# main
pila = Pila()
while(True):
    entrada = input(string_entrada)

    if (entrada == "0"): break
    elif (entrada == "1"):
        pelicula = input("Ingrese el nombre de la pelicula: ")
        modelo = input("Ingrese el modelo utilizado en la pelicula: ")
        estado = input("Ingrese el estado del modelo (debe estar dentro de estas opciones [dañado, impecable, destruido]): ")

        if (estado.lower() not in estados_trajes):
            print("El estado del traje no esta en las opciones listadas.")
        else:
            añadir_modelo(pila, [modelo, pelicula, estado])
    elif (entrada == "2"):
        hulkbuster_utilizado(pila)
    elif (entrada == "3"):
        modelos_dañados(pila)
    elif (entrada == "4"):
        eliminar_modelos_dañados(pila)
    elif (entrada == "5"):
        insertar_Mark_LXXXV(pila)
    elif (entrada == "6"):
        mostrar_trajes(pila, "Spider-Man: Homecoming")
        mostrar_trajes(pila, "Capitan America: Civil War")
