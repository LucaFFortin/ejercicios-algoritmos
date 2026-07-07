"""
Dada dos colas con valores ordenadas, realizar un algoritmo que permita combinarlas en una
nueva cola. Se deben mantener ordenados los valores sin utilizar ninguna estructura auxiliar,
ni métodos de ordenamiento
"""
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))
from tda_colas import Cola, nodoCola, arribo, atencion, mover_al_final, cola_vacia, barrido, en_frente, tamanio
from validaciones import validar_string, validar_numero
"""
dada 2 colas, comparar el elemento en frente de cada uno e ingresar el mas pequeño de estos
comparar ambos e ingresar en una nueva cola el valor mas pequeño de estos
no hace falta comparar los elementos con los de la cola actual
hay que validar si en algun momento una cola se vacia (en_frente retorna None), en ese caso simplemente se ingresa el resto de elementos de la cola hasta que esta otra este vacia
"""

# determina si una cola esta ordenada retornando un valor booleano
# retorna True si esta ordenado, False si no lo esta
def esta_ordenada(cola):
    ordenada = True
    primero = True
    anterior = 0
    for i in range(0, tamanio(cola)):
        numero = en_frente(cola)
        if (primero):
            anterior = numero
            primero = False
        else: 
            if (numero < anterior):
                ordenada = False
        mover_al_final(cola)

    return ordenada

# Recibe las 2 colas a unificar
# Elige el numero mas pequeño entre los frentes de ambas colas y lo ingresa a la cola unificada
# Cuando una cola se vacia, se ingresan el resto de elementos de la otra cola
caux1 = Cola()
caux2 = Cola()
cola_final = Cola()
def unir_colas_ordenado(cola1, cola2):
    while(not cola_vacia(cola1) or not cola_vacia(cola2)):
        # si la cola1 esta vacia, se ingresan el resto de los datos de la cola2
        if (cola_vacia(cola1)):
            while(not cola_vacia(cola2)):
                numero = atencion(cola2)
                arribo(cola_final, numero)
                arribo(caux1, numero)
                
        # si la cola2 esta vacia, se ingresan el resto de los datos de la cola1
        elif (cola_vacia(cola2)):
            while(not cola_vacia(cola1)):
                numero = atencion(cola1)
                arribo(cola_final, numero)
                arribo(caux2, numero)
        # si ambas colas tienen datos, calculamos cual de estos tiene el dato menor
        else:
            frente_uno = en_frente(cola1)
            frente_dos = en_frente(cola2)

            # si el numero en frente de la cola 1 es mayor al de la cola 2, ingresamos en la cola final el numero de la cola 2
            if (frente_uno > frente_dos):
                numero = atencion(cola2)
                arribo(cola_final, numero)
                arribo(caux2, numero)
            # sino ingresamos el numero de la cola 1
            else:
                numero = atencion(cola1)
                arribo(cola_final, numero)
                arribo(caux1, numero)

    print("Barrido cola final: ")
    barrido(cola_final)

cola1 = Cola()
cola2 = Cola()

# 2 bucles, uno para cada cola, se piden numeros hasta que el usuario desee realizar mas ingresos
while (True):
    numero = validar_numero("Ingrese un numero para la primera cola: ")
    arribo(cola1, numero)
    opcion = validar_string("Ingrese 'si' para ingresar otro numero, 'no' para salir: ")
    while (opcion.lower() not in ["si", "no"]):
        opcion = validar_string("solo puede ingresar los valores: 'si' para ingresar otro numero, 'no' para salir: ")
    if (opcion == "no"): break
while (True):
    numero = validar_numero("Ingrese un numero para la segunda cola: ")
    arribo(cola2, numero)
    opcion = validar_string("Ingrese 'si' para ingresar otro numero, 'no' para salir: ")
    while (opcion.lower() not in ["si", "no"]):
        opcion = validar_string("solo puede ingresar los valores: 'si' para ingresar otro numero, 'no' para salir: ")
    if (opcion == "no"): break

# se valida que las colas no esten vacias porque de esa manera, el algoritmo retornaria una cola vacia y no tendria sentido ejecutarla
if (cola_vacia(cola1) and cola_vacia(cola2)): print("Las colas estan vacias, no se realizo ninguna operación.")
# se valida que ambas colas esten ordenadas, paso necesario por requisito de la ejecucion del algoritmo.
elif (not esta_ordenada(cola1) or not esta_ordenada(cola2)): print("Las colas no estan ordenadas, no se realizo ninguna operación.")
# por ultimo, si se cumplen las condiciones, unificamos las colas en 1 sola
else: unir_colas_ordenado(cola1, cola2)

opcion = validar_string("Desea ver las colas de entrada y salida? SI = ver, NO = no ver: ")
if (opcion.lower() == "si"):
    print("Primera cola de numeros: ")
    barrido(caux1)
    print("Segunda cola de numeros: ")
    barrido(caux2)
    print("Cola final:")
    barrido(cola_final)

    