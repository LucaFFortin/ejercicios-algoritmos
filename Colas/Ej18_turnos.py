"""
Dada una cola con los códigos de turnos de atención (con el formato #@@@, donde # es una
letra de la A hasta la F y “@@@” son tres dígitos desde el 000 al 999), desarrollar un algoritmo
que resuelva las siguientes situaciones:
a. cargar 1000 turnos de manera aleatoria a la cola.
b. separar la cola con datos en dos colas, cola_1 con los turnos que empiezan con la letra A, C
y F, y la cola_2 con el resto de los turnos (B, D y E).
c. determinar cuál de las colas tiene mayor cantidad de turnos, y de esta cuál de las letras
tiene mayor cantidad.
d. mostrar los turnos de la cola con menor cantidad de elementos, cuyo número de turno sea
mayor que 506.
"""
from tda_colas import Cola, nodoCola, arribo, atencion, mover_al_final, cola_vacia, barrido, en_frente, tamanio
import random

# cola para turnos especificos
turnos = Cola()
# cola de turnos con letra A, C y F
cola_1 = Cola()
# cola de turnos con letra B, D y E
cola_2 = Cola()
# cola de turnos para cada letra
turnos_a = Cola()
turnos_b = Cola()
turnos_c = Cola()
turnos_d = Cola()
turnos_e = Cola()
turnos_f = Cola()
# cola de turnos con numero mayor a 506 calculados de la cola menor
turnos_mayor = Cola()

# genera mil turnos con letra y numero aleatorio dentro de los rangos especificados
while tamanio(turnos) < 1000:
    letra = random.choice(["A", "B", "C", "D", "E", "F"])
    numero = random.randint(0, 999) # falta llenar el string para que 0 sea 000

    turno = letra + str(numero)

    # envia a la cola 1 los turnos con la letra A, C y F, y a la cola 2 los turnos con la letra B, D y E
    if (letra in ["A", "C", "F"]): arribo(cola_1, turno)
    else: arribo(cola_2, turno)

    # ingresamos en cada cola de letras su turno correspondiente
    if (letra == "A"): arribo(turnos_a, turno)
    elif (letra == "B"): arribo(turnos_b, turno)
    elif (letra == "C"): arribo(turnos_c, turno)
    elif (letra == "D"): arribo(turnos_d, turno)
    elif (letra == "E"): arribo(turnos_e, turno)
    elif (letra == "F"): arribo(turnos_f, turno)

    arribo(turnos, turno)

# preguntamos cual de las 2 colas de turnos es mas grande 
# e imprimimos cual de sus colas internas es la mas grande y su cantidad de turnos
if (tamanio(cola_1) < tamanio(cola_2)): 
    # calculamos los turnos mayores a 506 de la cola 1
    for _ in range(tamanio(cola_1)):
        turno = en_frente(cola_1)
        if (int(turno[1:]) > 506): arribo(turnos_mayor, turno)
        mover_al_final(cola_1)
    print("La cola 2 tiene una mayor cantidad de turnos que la cola 2.")
    if (tamanio(turnos_b) > tamanio(turnos_d) and tamanio(turnos_b) > tamanio(turnos_e)):
        print(f"La cola de turnos con letra B tiene la mayor cantidad de turnos con {tamanio(turnos_b)}")
    if (tamanio(turnos_d) > tamanio(turnos_b) and tamanio(turnos_d) > tamanio(turnos_e)):
        print(f"La cola de turnos con letra B tiene la mayor cantidad de turnos con {tamanio(turnos_d)}")
    if (tamanio(turnos_e) > tamanio(turnos_b) and tamanio(turnos_e) > tamanio(turnos_d)):
        print(f"La cola de turnos con letra B tiene la mayor cantidad de turnos con {tamanio(turnos_e)}")
else:
    # calculamos los turnos mayores a 506 de la cola 2
    for _ in range(tamanio(cola_2)):
        turno = en_frente(cola_2)
        if (int(turno[1:]) > 506): arribo(turnos_mayor, turno)
        mover_al_final(cola_2)
    print("La cola 1 tiene una mayor cantidad de turnos que la cola 1.")
    if (tamanio(turnos_a) > tamanio(turnos_c) and tamanio(turnos_a) > tamanio(turnos_f)):
        print(f"La cola de turnos con letra B tiene la mayor cantidad de turnos con {tamanio(turnos_a)}")
    if (tamanio(turnos_c) > tamanio(turnos_a) and tamanio(turnos_c) > tamanio(turnos_f)):
        print(f"La cola de turnos con letra B tiene la mayor cantidad de turnos con {tamanio(turnos_c)}")
    if (tamanio(turnos_f) > tamanio(turnos_a) and tamanio(turnos_f) > tamanio(turnos_c)):
        print(f"La cola de turnos con letra B tiene la mayor cantidad de turnos con {tamanio(turnos_f)}")

# imprimimos la cola de turnos segun letra mas grande
if (tamanio(turnos_a) >= tamanio(turnos_b) and
    tamanio(turnos_a) >= tamanio(turnos_c) and
    tamanio(turnos_a) >= tamanio(turnos_d) and
    tamanio(turnos_a) >= tamanio(turnos_e) and
    tamanio(turnos_a) >= tamanio(turnos_f)):
    print(f"La cola turnos_a tiene la mayor cantidad de turnos con {tamanio(turnos_a)} turnos.")
elif (tamanio(turnos_b) >= tamanio(turnos_a) and
      tamanio(turnos_b) >= tamanio(turnos_c) and
      tamanio(turnos_b) >= tamanio(turnos_d) and
      tamanio(turnos_b) >= tamanio(turnos_e) and
      tamanio(turnos_b) >= tamanio(turnos_f)):
    print(f"La cola turnos_b tiene la mayor cantidad de turnos con {tamanio(turnos_b)} turnos.")
elif (tamanio(turnos_c) >= tamanio(turnos_a) and
      tamanio(turnos_c) >= tamanio(turnos_b) and
      tamanio(turnos_c) >= tamanio(turnos_d) and
      tamanio(turnos_c) >= tamanio(turnos_e) and
      tamanio(turnos_c) >= tamanio(turnos_f)):
    print(f"La cola turnos_c tiene la mayor cantidad de turnos con {tamanio(turnos_c)} turnos.")
elif (tamanio(turnos_d) >= tamanio(turnos_a) and
      tamanio(turnos_d) >= tamanio(turnos_b) and
      tamanio(turnos_d) >= tamanio(turnos_c) and
      tamanio(turnos_d) >= tamanio(turnos_e) and
      tamanio(turnos_d) >= tamanio(turnos_f)):
    print(f"La cola turnos_d tiene la mayor cantidad de turnos con {tamanio(turnos_d)} turnos.")
elif (tamanio(turnos_e) >= tamanio(turnos_a) and
      tamanio(turnos_e) >= tamanio(turnos_b) and
      tamanio(turnos_e) >= tamanio(turnos_c) and
      tamanio(turnos_e) >= tamanio(turnos_d) and
      tamanio(turnos_e) >= tamanio(turnos_f)):
    print(f"La cola turnos_e tiene la mayor cantidad de turnos con {tamanio(turnos_e)} turnos.")
else:
    print(f"La cola turnos_f tiene la mayor cantidad de turnos con {tamanio(turnos_f)} turnos.")

# imprimimos la cantidad de turnos cuyo numero es mayor a 506 de la cola
print(f"La cola menor tiene {tamanio(turnos_mayor)} turnos cuyo numero es mayor a 506.")