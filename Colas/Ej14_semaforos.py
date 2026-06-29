"""
Realizar un algoritmo que permita realizar las siguientes funciones:
a. cargar semáforos de una rotonda y sus respectivos tiempos de encendido en verde –cargue
al menos tres semáforos–.
b. simular el funcionamiento de los semáforos cargados (cola circular).
c. debe mostrar por pantalla el cambio de colores y el número del semáforo.
"""
import sys
from pathlib import Path
import time
import os

sys.path.append(str(Path(__file__).resolve().parent.parent))

from tda_colas import Cola, nodoCola, arribo, atencion, mover_al_final, cola_vacia, barrido, en_frente, tamanio
from validaciones import validar_string, validar_numero

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_rotonda(rotonda, activo, color, siguinte):
    # muestra todos los semaforos, cambia de color el semaforo activo y el siguiente semaforo cuando el activo esta a punto de apagarse
    limpiar_pantalla()
    print("Simulacion de rotonda")

    cola_aux = Cola()
    while not cola_vacia(rotonda):
        numero, tiempo = atencion(rotonda)
        # print(numero, activo, tamanio(rotonda))
        if numero == activo:
            estado = color
        # si el semaforo activo esta a punto de apagarse, se muestra como el semaforo siguiente comienza a iniciar
        elif (siguinte is not None and numero == siguinte):
            estado = "🟡 AMARILLO      "
        else:
            estado = "🔴 ROJO          "
        print(f"Semáforo {numero}:  {estado}  ({tiempo}s en verde)")
        arribo(cola_aux, (numero, tiempo))

    while not cola_vacia(cola_aux):
        arribo(rotonda, atencion(cola_aux))
    print()

rotonda = Cola()
def agregar_semaforo():
    id = tamanio(rotonda) + 1
    tiempo = validar_numero("Ingrese la cantidad de tiempo en verde del semaforo en segundos: ")

    arribo(rotonda, (id, tiempo))   

TIEMPO_AMARILLO = 2

while(True):
    opcion = validar_numero("Opciones: 1 = agregar un semaforo, 0 = Ejecutar la simulacion: ")

    if (opcion == 1):
        agregar_semaforo()
    elif (opcion == 0):
        if (tamanio(rotonda) < 3):
            print("Debe ingresar como minimo 3 semaforos para poder ejecutar la simulación.")
        else:
            break
    else:
        print("Opcion invalida.")

tamanio_rotonda = tamanio(rotonda)
total = tamanio_rotonda
contador = 0

while contador < total:
    numero, tiempo_verde = en_frente(rotonda)
    proximo_numero = (numero % tamanio_rotonda) + 1      
    es_ultimo = contador == total - 1

    for t in range(tiempo_verde, 0, -1):
        # previene que en la ultima iteracion de la simulacion se comience a activar el siguiente semaforo
        if (t <= TIEMPO_AMARILLO):
            siguinte = None if es_ultimo else proximo_numero
            mostrar_rotonda(rotonda, numero, f"🟡 AMARILLO ({t}s) ", siguinte)
        else:
            mostrar_rotonda(rotonda, numero, f"🟢 VERDE    ({t}s) ", None)

        time.sleep(1)
    # pone todos los semaforos en rojo en la ultima iteracion, finalizando la simulación
    else:
        mostrar_rotonda(rotonda, numero, f"🔴 ROJO          ", None)

    mover_al_final(rotonda)
    contador += 1