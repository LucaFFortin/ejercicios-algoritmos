"""
Desarrollar un algoritmo para el control de un puesto de peaje (que posee 3 cabinas de cobro), 
que resuelva las siguientes actividades:
a. agregar 30 vehículos de manera aleatoria a las cabinas de cobro, los tipos de vehículos son 
los siguientes:
    I.   automóviles (tarifa $47);
    II.  camionetas (tarifa $59);
    III. camiones (tarifa $71);
    IV.  colectivos (tarifa $64).
b. realizar la atención de las cabinas, considerando las tarifas del punto anterior.
c. determinar qué cabina recaudó mayor cantidad de pesos ($).
d. determinar cuántos vehículos de cada tipo se atendieron en cada cola.
"""
import sys
from pathlib import Path
import random

sys.path.append(str(Path(__file__).resolve().parent.parent))
from tda_colas import Cola, nodoCola, arribo, atencion, mover_al_final, cola_vacia, barrido, en_frente, tamanio
from validaciones import validar_string, validar_numero

primera_cabina = Cola()
segunda_cabina = Cola()
tercera_cabina = Cola()

tarifas = {
    "automovil": 47, 
    "camioneta": 59, 
    "camion": 71, 
    "colectivo": 64
}

datos_pc = {
    "automovil": 0, 
    "camioneta": 0, 
    "camion": 0, 
    "colectivo": 0,
    "total": 0
}

datos_sc = {
    "automovil": 0, 
    "camioneta": 0, 
    "camion": 0, 
    "colectivo": 0,
    "total": 0
}

datos_tc = {
    "automovil": 0, 
    "camioneta": 0, 
    "camion": 0, 
    "colectivo": 0,
    "total": 0
}

for i in range(30):
    cabina = random.randint(1, 3)
    cliente = random.choice(["automovil", "camioneta", "camion", "colectivo"])
    if (cabina == 1):
        arribo(primera_cabina, cliente)
    elif (cabina == 2):
        arribo(segunda_cabina, cliente)
    elif (cabina == 3):
        arribo(tercera_cabina, cliente)

while(True):
    if (not cola_vacia(primera_cabina)):
        cliente = atencion(primera_cabina)
        datos_pc[cliente] += 1
        datos_pc["total"] += tarifas[cliente]
    elif (not cola_vacia(segunda_cabina)):
        cliente = atencion(segunda_cabina)
        datos_sc[cliente] += 1
        datos_sc["total"] += tarifas[cliente]
    elif (not cola_vacia(tercera_cabina)):
        cliente = atencion(tercera_cabina)
        datos_tc[cliente] += 1
        datos_tc["total"] += tarifas[cliente]
    else:
        break

if (datos_pc["total"] > datos_sc["total"] and datos_pc["total"] > datos_tc["total"]):
    print("La cabina que mas ingresos tuvo fue la primera cabina.")
elif (datos_sc["total"] > datos_pc["total"] and datos_sc["total"] > datos_tc["total"]):
    print("La cabina que mas ingresos tuvo fue la segunda cabina.")
elif (datos_tc["total"] > datos_sc["total"] and datos_tc["total"] > datos_pc["total"]):
    print("La cabina que mas ingresos tuvo fue la tercera cabina.")

print(f"En la primera cabina se atendieron: {datos_pc['automovil']} automoviles, {datos_pc['camion']} camiones, {datos_pc["camioneta"]} camionetas y {datos_pc['colectivo']} colectivos.")
print(f"En la segunda cabina se atendieron: {datos_sc['automovil']} automoviles, {datos_sc['camion']} camiones, {datos_sc["camioneta"]} camionetas y {datos_sc['colectivo']} colectivos.")
print(f"En la tercera cabina se atendieron: {datos_tc['automovil']} automoviles, {datos_tc['camion']} camiones, {datos_tc["camioneta"]} camionetas y {datos_tc['colectivo']} colectivos.")