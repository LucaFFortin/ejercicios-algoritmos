"""
Un grupo de amigos se reúnen a jugar un juego de dados, suponga que dichos jugadores están 
cargados en una lista de acuerdo a un número asignado de manera aleatoria y su nombre. 
Desarrollar un algoritmo que contemple las siguientes condiciones:
a. simular la tirada de un dado -de seis lados D6- en cada turno del jugador;
b. el orden de turno de los jugadores es el mismo en el que están cargados en la lista;
c. después de que tira el último jugador de la lista debe seguir el primero;
d. el juego termina cuando uno de los jugadores saca un 5, en ese caso mostrar su nombre;
e. Debe modificar el TDA para implementar lista circular
"""
import sys
from pathlib import Path
import random
import time

sys.path.append(str(Path(__file__).resolve().parent.parent))

from validaciones import validar_string
from utils import limpiar
from tda_listas import insertar as insertar_lineal, lista_vacia, eliminar, barrido, tamanio, buscar, criterio, buscar_criterio, insertar_criterio, eliminar_criterio, Lista, nodoLista

# insertar circular, modifica el ingreso para que el ultimo elemento siempre apunte al primero
def insertar(lista, dato):
    """Insertar el dato pasado en la lista circular."""
    nodo = nodoLista()
    nodo.info = dato

    if (lista.inicio is None):
        nodo.sig = lista.inicio
        lista.inicio = nodo
        lista.inicio.sig = nodo
    else:
        ant = lista.inicio
        act = lista.inicio.sig
        while (act is not lista.inicio):
            ant = ant.sig
            act = act.sig
        nodo.sig = act
        ant.sig = nodo

    lista.tamanio += 1

def tirada():
    numero = random.randint(1, 6)
    return numero

# limpiamos la pantalla
limpiar()

# entrada de datos
lista = Lista()

while (True):
    opcion = input("Desea ingresar una persona al juego?, Si para ingresar, No para salir: ").lower()

    if (opcion == "no"): 
        limpiar()
        break
    elif (opcion == "si"):
        dato = validar_string("Ingrese el nombre del jugador: ")
        insertar(lista, dato)        
        limpiar()
    else:    
        limpiar()
        print("La opcion ingresada no esta dentro de las opciones listadas.")

# simulacion del juego
VALOR_GANADOR = 5
ronda = 1
n = tamanio(lista)
cont_jugador = 0
mostrado = False

aux = lista.inicio
while (aux is not None):
    cont_jugador += 1

    # mostramos un mensaje para indicar la ronda
    if (not mostrado):
        print(f"Ronda {ronda}.")
        time.sleep(1)
        mostrado = True

    # simulamos el juego
    numero = tirada()

    if (numero == VALOR_GANADOR):
        print(f"El jugador {aux.info} gano el juego al sacar el numero {VALOR_GANADOR}")
        time.sleep(1)
        break
    else:
        print(f"Turno de {aux.info}, jugo y le salio el numero {numero}.")
        time.sleep(1)

    # una vez finalizada la ronda, modificamos las variables asi se vuelve a mostrar el mensaje
    if (cont_jugador == n):
        cont_jugador = 0
        mostrado = False
        ronda += 1
        limpiar()

    aux = aux.sig
