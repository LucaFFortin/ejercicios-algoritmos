"""
Modificar las funciones de arribo y atención del TDA cola para adaptarlo a una cola circular,
que no necesite la función mover al final; y desarrollar un función que permita realizar un barrido
de dicha estructura respetando el principio de funcionamiento de la cola.
"""
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from tda_colas import Cola, nodoCola, arribo, atencion, mover_al_final, cola_vacia, barrido, en_frente, tamanio
from validaciones import validar_numero

# el primer dato es ingresado en el frente, hacemos que el nodo apunte a frente y 
# que el final de la cola apunte al nodo
# si es el segundo, hacemos que el nodo anterior apunte al nuevo nodo, que el nodo apunte al frente
# y que el final de la cola apunte al nodo actual
def arribo_circular(cola, dato):
    """Arriba el dato al final de la cola circular."""
    nodo = nodoCola()
    nodo.info = dato
    if cola.frente is None:
        cola.frente = nodo
        nodo.sig = cola.frente       
    else:
        cola.final.sig = nodo
        nodo.sig = cola.frente       
    cola.final = nodo
    cola.tamanio += 1

# si no hay datos en la cola, imprimios none para indicar que no hay datos
# si el dato actual de la cola es unico, hacemos que los punteros frente y final de la cola apunten a none
# sino hacemos que el frente de la cola apunte al siguiente elemento y que el siguiente elemento al final apunte al frente
def atencion_circular(cola):
    """Atiende el elemento en el frente de la cola circular y lo devuelve."""
    if cola_vacia(cola):
        return
    dato = cola.frente.info
    if cola.frente == cola.final:    
        cola.frente = None
        cola.final = None
    else:
        cola.frente = cola.frente.sig
        cola.final.sig = cola.frente 
    cola.tamanio -= 1
    return dato

def mover_al_final_circular(cola):
    """Hace que los punteros cola.final y cola.frente apunten al nodo siguiente y devuelve el dato que estaba en el frente"""
    cola.final = cola.frente         
    cola.frente = cola.frente.sig    

def barrido_circular(cola):
    """Muestra el contenido de la cola circular"""
    # si no hay datos, se lo indicamos al usuario
    if cola_vacia(cola):
        print("No hay datos en la cola circular.")
        return
    n = tamanio(cola)
    # sino, imprimimos los datos de la cola
    for _ in range(n):
        dato = en_frente(cola)
        print(dato)
        mover_al_final_circular(cola) 

cola = Cola()
# punto de entrada de la aplicacion para usar las funciones
while(True):
    opcion = validar_numero("Opciones: 1 - Agregar un dato, 2 - Eliminar un dato, 3 - recorrer la estructura, 0 - Salir: ")
    if (opcion == 1):
        dato = input("Escriba el dato a ingresar: ")
        arribo_circular(cola, dato)
    if (opcion == 2):
        dato = atencion_circular(cola)
        print(dato)
    if (opcion == 3):
        barrido_circular(cola)
    if (opcion == 0): break
    