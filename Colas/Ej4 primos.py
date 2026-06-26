"""
Dada una cola de números cargados aleatoriamente, eliminar de ella todos los que no sean primos.
"""
from tda_colas import Cola, nodoCola, arribo, atencion, mover_al_final, cola_vacia, barrido, en_frente, tamanio
import random
import math

cola = Cola()
cola_primos = Cola()

def es_primo(n):
    base = math.sqrt(n)
    contador = math.floor(base)
    
    while (contador >= 2):
        if (n % contador == 0):
            return False
        contador -= 1
    return True

for i in range(100):
    numero = random.randint(0, 100)
    arribo(cola, numero)

print("Cola de numeros aleatorios: ")
barrido(cola)

while (not cola_vacia(cola)):
    numero = atencion(cola)
    if (es_primo(numero)): arribo(cola_primos, numero)

print("Cola dejando solo los numeros primos: ")
barrido(cola_primos)
