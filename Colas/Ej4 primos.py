"""
Dada una cola de números cargados aleatoriamente, eliminar de ella todos los que no sean primos.
"""
from tda_colas import Cola, nodoCola, arribo, atencion, mover_al_final, cola_vacia, barrido, en_frente, tamanio
import random
import math

cola = Cola()
cola_primos = Cola()

# funcion que verifica que un numero sea primo
def es_primo(n):
    base = math.sqrt(n)
    contador = math.floor(base)
    
    while (contador >= 2):
        if (n % contador == 0):
            return False
        contador -= 1
    return True

# se ingresan 100 datos aleatorios de entre 1 y 100 (por temas de optimizacion de la funcion)
for i in range(100):
    numero = random.randint(0, 100)
    arribo(cola, numero)

# se imprime la cola de numeros aleatorios
print("Cola de numeros aleatorios: ")
barrido(cola)

# se extraen y guardan solo los numeros primos en una cola aparte
while (not cola_vacia(cola)):
    numero = atencion(cola)
    if (es_primo(numero)): arribo(cola_primos, numero)

# imprimimos la cola de primos
print("Cola dejando solo los numeros primos: ")
barrido(cola_primos)
