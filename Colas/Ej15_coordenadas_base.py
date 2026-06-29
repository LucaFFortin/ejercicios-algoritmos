"""
Suponga que se escapa hacia el planeta tierra en un Caza TIE robado –huyendo de un Destructor
Estelar y necesita localizar la base rebelde más cercana– y se tiene una cola con información
de las bases rebeldes en la tierra de las cuales conoce su nombre, número de flota aérea,
coordenadas de latitud y longitud. Desarrolle un algoritmo que permita resolver las siguientes
tareas una vez que aterrice:
a. determinar cuál es la base rebelde más cercana desde su posición actual.
b. para el cálculo de la distancia deberá utilizar la fórmula de Haversine:
donde r es el radio medio de la tierra en metros (6371000), φ1 y φ2 las latitudes de los
dos puntos –por ejemplo coordenadas actual–, λ1 y λ2 las longitudes de los dos puntos
–coordenadas de la base– ambos expresadas en radianes; para convertir de grados a
radianes utilice la función math.radians(ángulo coordenada).
c. mostrar el nombre y la distancia a la que se encuentran las tres bases más cercanas y determinar
cual tiene mayor flota aérea.
d. determinar la distancia hasta la base rebelde con mayor flota aérea.
"""
import math
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from tda_colas import Cola, nodoCola, arribo, atencion, mover_al_final, cola_vacia, barrido, en_frente, tamanio
from validaciones import validar_numero_flotante, validar_string, validar_numero

# latitud y longitud de la posicion actual
lat_uno = None
lon_uno = None
# colas donde ingresaran: bases ingresadas por el usuario, las bases con su distancia hacia el punto actual y las bases cercanas (3)
bases = Cola()
distancia_bases = Cola()
bases_cercanas = Cola()

# no se estan modificando ningun de las 2 siguientes listas

# valida que la posicion actual este dentro del rango de latitud y longitud conocida
# si es valido, devuelve la latitud y longitud en forma de radianes
def validar_posicion (lat, lon):
    if (-90 <= lat <= 90 and -180 <= lon <= 180):
        return math.radians(lat), math.radians(lon)
    else:
        print("La posicion debe estar los siguientes rangos: latitud: de -90° a 90°, longitud: de -180° a 180°.")
        return None, None

def ingresar_base():
    nombre = validar_string("Ingrese el nombre de la base: ")
    numero_flota = validar_numero("Ingrese el numero de flota: ")
    
    # verificamos que no se pueda ingresar un numero de flota duplicado
    while (True):
        existe = False
        for _ in range(tamanio(bases)):
            base = en_frente(bases)
            if (numero_flota == base[1]):
                existe = True
            mover_al_final(bases)

        if (existe):
            numero_flota = validar_numero("Ese numero de flota existe, ingrese un numero de flota diferente: ")
        else:
            break

    # verificamos que la latitud y longitud esten dentro del rango aceptado
    while (True):
        lat = validar_numero_flotante("Ingrese la latitud en grados de la posicion de la base: ")
        lon = validar_numero_flotante("Ingrese la longitud en grados de la posicion de la base: ")

        lat, lon = validar_posicion(lat, lon)

        if (lat is not None and lon is not None): break

    arribo(bases, [nombre, numero_flota, lat, lon])

# determina la distancia entre la posicion actual y las bases aplicando la formula de haversine
def determinar_distacia():
    for _ in range(tamanio(bases)):
        nombre, numero_flota, lat, lon = en_frente(bases)

        distancia = haversine(lat, lon)

        arribo(distancia_bases, [nombre, numero_flota, distancia])

        mover_al_final(bases)

# determina las 3 bases mas cercanas a la ubicacion actual
def determinar_cercanas():
    caux = Cola()
    # ingresamos la bases que esten en distancia_bases a bases cercanas
    for _ in range(tamanio(distancia_bases)):
        base = en_frente(distancia_bases)
        # si hay menos de 3 bases, simplemente las ingresamos
        if (tamanio(bases_cercanas) < 3):
            arribo(bases_cercanas, base)
        # sino calculamos si la base a ingresar tiene una distancia menor a las bases de que ya estan en la cola
        else:
            arribo(bases_cercanas, base)
            mayor = None
            while (not cola_vacia(bases_cercanas)):
                base_c = atencion(bases_cercanas)

                if (mayor is None):
                    mayor = base_c
                else:
                    if (mayor[2] < base_c[2]):
                        mayor = base_c

                arribo(caux, base_c)
            
            while (not cola_vacia(caux)):
                base = atencion(caux)
                if (base[1] != mayor[1]):
                    arribo(bases_cercanas, base)
        
        mover_al_final(distancia_bases)

# muestra las bases cercanas
def mostrar_bases_cercanas():
    for _ in range(tamanio(bases_cercanas)):
        nombre, _, distancia = en_frente(bases_cercanas)

        print(f"Base {nombre}, esta a una distancia de {int(distancia)} metros de su ubicación actual.")

        mover_al_final(bases_cercanas)

# determina y muestra la base con la flota mayor mas grande entre las ingresadas
def determinar_mayor_flota():
    flota_mayor = []
    primero = True
    for _ in range(tamanio(distancia_bases)):
        base = en_frente(distancia_bases)
        if (primero):
            flota_mayor = base
            primero = False
        else:
            if (flota_mayor[1] < base[1]):
                flota_mayor = base

        mover_al_final(distancia_bases)

    print(f"La base con la flota mayor en general es {flota_mayor[0]} con el numero de flota {flota_mayor[1]}, a una distancia de {int(flota_mayor[2])} metros.")


# determina y muestra la base con la flota mayor mas grande entre las bases cercanas
def determinar_mayor_flota_cercana():
    flota_mayor_cercana = []
    primero = True
    
    for _ in range(tamanio(bases_cercanas)):
        base = en_frente(bases_cercanas)

        if (primero):
            flota_mayor_cercana = base
            primero = False
        else:
            if (flota_mayor_cercana[1] < base[1]):
                flota_mayor_cercana = base

        mover_al_final(bases_cercanas)
    print(f"La base con la flota mayor entre las bases cercanas es {flota_mayor_cercana[0]} con el numero de flota {flota_mayor_cercana[1]}, a una distancia de {int(flota_mayor_cercana[2])} metros.")

# formula de haversine, 
# la latitud y longitud de la posicion actual son variables globales, 
# la latitud y longitud de cada base se ingresan como argumentos cuando se ejecuta la funcion
# retorna la distancia entre la posicion actual y la base en forma de metros como un numero de coma flotante
def haversine(lat, lon):
    RADIO = 6371000 # radio de la tierra en metros
    
    return 2 * RADIO * math.asin(
        math.sqrt(
            math.sin((lat - lat_uno) / 2) ** 2 + 
            math.cos(lat_uno) * math.cos(lat) * math.sin((lon - lon_uno) / 2 ) ** 2 ))

while (lat_uno is None and lon_uno is None):
    lat = validar_numero_flotante("Ingrese la latitud de su ubicacion actual: ")
    lon = validar_numero_flotante("Ingrese la longitud de su ubicacion actual: ")

    lat_uno, lon_uno = validar_posicion(lat, lon)

# ingreso de bases
opcion = validar_string("Desea ingresar bases? Si para ingresar, no para salir: ")
while (True):
    if (opcion.lower() == "si"):
        ingresar_base()
        opcion = validar_string("Desea ingresar mas bases? Si para ingresar, no para salir: ")
    elif (opcion.lower() == "no"):
        break
    else:
        opcion = validar_string("Opcion no reconocida: introduzca: Si para ingresar, no para salir: ")

determinar_distacia()
determinar_cercanas()
mostrar_bases_cercanas()
determinar_mayor_flota_cercana()
determinar_mayor_flota()
