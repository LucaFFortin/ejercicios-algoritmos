"""
Realizar un algoritmo que permita realizar las siguientes funciones:
a. cargar semáforos de una rotonda y sus respectivos tiempos de encendido en verde –cargue
al menos tres semáforos–.
b. simular el funcionamiento de los semáforos cargados (cola circular).
c. debe mostrar por pantalla el cambio de colores y el número del semáforo.
"""

import time
from tda_colas import Cola, nodoCola, arribo, atencion, mover_al_final, cola_vacia, barrido, en_frente, tamanio

import time
import os

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_rotonda(rotonda, activo, color, cambiando):
    # muestra todos los semáforos, cambia de color el semaforo activo y el siguiente semaforo cuando el activo esta a punto de apagarse
    limpiar_pantalla()
    print("Simulacion de rotonda")

    cola_aux = Cola()
    while not cola_vacia(rotonda):
        numero, tiempo = atencion(rotonda)
        if numero == activo:
            estado = color
        # si el semaforo activo esta a punto de apagarse, se muestra como el semaforo siguiente comienza a iniciar
        elif (cambiando and (numero == activo + 1 or (activo == 3 and numero == 1))):
            estado = "🟡 AMARILLO      "
        else:
            estado = "🔴 ROJO          "
        print(f"Semáforo {numero}:  {estado}  ({tiempo}s en verde)")
        arribo(cola_aux, (numero, tiempo))

    while not cola_vacia(cola_aux):
        arribo(rotonda, atencion(cola_aux))
    print()


rotonda = Cola()
arribo(rotonda, (1, 1))
arribo(rotonda, (2, 1))
arribo(rotonda, (3, 1))

TIEMPO_AMARILLO = 2
vueltas = 2
total = tamanio(rotonda) * vueltas
contador = 0

while contador < total:
    numero, tiempo_verde = en_frente(rotonda)
    for t in range(tiempo_verde, 0, -1):
        # previene que en la ultima iteracion de la simulacion se comience a activar el siguiente semaforo
        if (t <= TIEMPO_AMARILLO and contador > (total - tamanio(rotonda) + 1)):
            mostrar_rotonda(rotonda, numero, f"🟡 AMARILLO ({t}s) ", False)
        elif (t <= TIEMPO_AMARILLO):
            mostrar_rotonda(rotonda, numero, f"🟡 AMARILLO ({t}s) ", True)
        else:
            mostrar_rotonda(rotonda, numero, f"🟢 VERDE    ({t}s) ", False)

        time.sleep(1)
    # pone todos los semaforos en rojo en la ultima iteracion, finalizando la simulación
    else:
        mostrar_rotonda(rotonda, numero, f"🔴 ROJO          ", False)

    mover_al_final(rotonda)
    contador += 1