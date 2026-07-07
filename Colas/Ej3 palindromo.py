import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from tda_colas import Cola, nodoCola, arribo, atencion, mover_al_final, cola_vacia, barrido, en_frente, tamanio
from Pilas.pilas import Pila, apilar, desapilar, pila_vacia, barrido as barrido_pila
from validaciones import validar_string

cola = Cola()
pila = Pila()

palabra = validar_string("Ingrese una palabra a analizar si es palindromo: ")
valid = True

# se ingresan los caracteres uno por uno en una cola y una pila
for char in palabra:
    arribo(cola, char)
    apilar(pila, char)

# se verifica que los caracteres que estan dentro de la cola y la pila sean iguales aunque esten en posiciones opuestas
# se extraen los caracteres y luego se vuelven a guardar en la cola y pila correspondiente.
caux = Cola()
paux = Pila()
while (not cola_vacia(cola) and not pila_vacia(pila)):
    cola_char = atencion(cola)
    pila_char = desapilar(pila)
    if (cola_char != pila_char): valid = False
    arribo(caux, cola_char)
    apilar(paux, pila_char)

while (not cola_vacia(caux) and not pila_vacia(paux)):
    cola_char = atencion(caux)
    pila_char = desapilar(paux)
    arribo(cola, cola_char)
    apilar(pila, pila_char)

if (valid): print("La palabra ingresada es palindromo!")
else: print("La palabra ingresada no es un palindromo")

# si desea ver la entrada y salida, lo imprimimos por pantalla
opcion = validar_string("Desea ver las colas de entrada y salida? SI = ver, NO = no ver: ")
if (opcion.lower() == "si"):
    print("palabra ingresada: ")
    barrido(cola)
    print("palabra invertida: ")
    barrido_pila(pila)