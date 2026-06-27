class nodoCola(object):
    """Clase nodo cola."""
    info, sig = None, None

class Cola(object):
    """Clase cola."""
    def __init__(self):
        """Crear cola vacia."""
        self.frente, self.final = None, None
        self.tamanio = 0    
    
def arribo(cola, dato):
    """Arriba el dato al final de la cola."""
    nodo = nodoCola()
    nodo.info = dato
    if cola.frente is None:
        cola.frente = nodo
    else:
        cola.final.sig = nodo
    cola.final = nodo
    cola.tamanio += 1

def atencion(cola):
    """Atiende el elemento en el frente de la cola y lo devuelve."""
    dato = cola.frente.info
    cola.frente = cola.frente.sig
    if cola.frente is None:
        cola.final = None
    cola.tamanio -= 1
    return dato

def cola_vacia(cola):
    """devuelve true si la cola esta vacia,"""
    return cola.frente is None

def en_frente(cola):
    """devuelve el valor almacenado en el frente de la cola."""
    return cola.frente.info

def tamanio(cola):
    """devuelve el numero de elementos de la cola."""
    return cola.tamanio

def mover_al_final(cola):
    """mueve el elemento del frente de la cola al final."""
    dato = atencion(cola)
    arribo(cola, dato)
    return dato

def barrido(c):
    """muestra el contenido de una cola sin perder datos."""
    cola_aux = Cola()
    while(not cola_vacia(c)):
        dato = atencion(c)
        print(dato)
        arribo(cola_aux, dato)

    while(not cola_vacia(cola_aux)):
        dato = atencion(cola_aux)
        arribo(c, dato)