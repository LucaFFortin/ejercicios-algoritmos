"""
Utilizando una lista doblemente enlazada, cargar una palabra carácter a carácter, y determinar 
si la misma es un palíndromo, sin utilizar ninguna estructura auxiliar.
"""
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from validaciones import validar_string
from utils import limpiar

# agremamos un puntero al elemento previo de la lista para crear los nodos de la lista doblemente enlazada
class nodoListaEnlazada(object):
    """Clase nodo lista doblemente enlazada."""
    
    info, sig, prev = None, None, None

# agregamos un puntero que guarda el ultimo elemento de la lista
class ListaEnlazada(object):
    """Clase lista doblemente enlazada"""
    
    def __init__(self):
        """Crea una lista doblemente enlazada vacia"""
        self.inicio = None
        self.final = None
        self.tamanio = 0

# creamos una funcion de insercion que guarde correctamente los elementos de forma secuencial
def insertar(lista, dato):
    """Insertar el dato pasado en la lista doblemente enlazada."""
    nodo = nodoListaEnlazada()
    nodo.info = dato
    if (lista.inicio is None):
        lista.inicio = nodo
        lista.final = nodo
    else:
        nodo.prev = lista.final
        lista.final.sig = nodo
        lista.final = nodo
    lista.tamanio += 1

# limpiamos la pantalla anterior
limpiar()

# entrada de datos
entrada = validar_string("Ingrese la palabra a validar: ")

# dividimos la entrada en caracteres y los ingresamos a la lista
lista_enlazada = ListaEnlazada()
for i in entrada.lower():
    insertar(lista_enlazada, i)

# iteramos el inicio y final de la lista a la vez para compararlos y asi verificar si la entrada es un palindromo o no.
inicio = lista_enlazada.inicio
final = lista_enlazada.final
es_palindromo = True

while (inicio is not None and final is not None):
    if (inicio.info != final.info):
        es_palindromo = False
        break
    inicio = inicio.sig
    final = final.prev

if (es_palindromo):
    print("Es palindromo.")
else:
    print("No es palindromo")
    
    