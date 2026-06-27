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

turnos = Cola()
cola_1 = Cola()
cola_2 = Cola()
turnos_a = Cola()
turnos_b = Cola()
turnos_c = Cola()
turnos_d = Cola()
turnos_e = Cola()
turnos_f = Cola()
turnos_mayor = Cola()

while tamanio(turnos) < 1000:
    letra = random.choice(["A", "B", "C", "D", "E", "F"])
    numero = random.randint(0, 999) # falta llenar el string para que 0 sea 000

    turno = letra + str(numero)

    if (letra in ["A", "C", "F"]): arribo(cola_1, turno)
    else: 
        arribo(cola_2, turno)
        if (numero > 506): arribo(turnos_mayor, turno)

    if (letra == "A"): arribo(turnos_a, turno)
    elif (letra == "B"): arribo(turnos_b, turno)
    elif (letra == "C"): arribo(turnos_c, turno)
    elif (letra == "D"): arribo(turnos_d, turno)
    elif (letra == "E"): arribo(turnos_e, turno)
    elif (letra == "F"): arribo(turnos_f, turno)

    arribo(turnos, turno)

if (tamanio(cola_1) > tamanio(cola_2)): print("La cola 1 tiene una mayor cantidad de turnos que la cola 2.")
else: print("La cola 2 tiene una mayor cantidad de turnos que la cola 1.")

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

print(f"La cola menor tiene {tamanio(turnos_mayor)} turnos cuyo numero es mayor a 506.")