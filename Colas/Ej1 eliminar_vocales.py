import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))
from tda_colas import Cola, nodoCola, arribo, atencion, mover_al_final, cola_vacia, barrido, en_frente, tamanio
from validaciones import validar_string

cdatos = Cola()
cola_no_vocales = Cola()

# ingreso de datos
letra = input('Ingrese un caracter o presione enter para salir: ')
while (letra != ''):
    if (len(letra) > 1):
        print("Solo debe ingresar una sola letra.")
    else:
        arribo(cdatos, letra)
    letra = input('Ingrese un caracter o presione enter para salir: ')

# se sacan todos los datos de la cola y se guardan en una cola auxiliar
# toda letra no vocal es ingresada a una cola aparte
caux = Cola()
while (not cola_vacia(cdatos)):
    letra = atencion(cdatos)
    if letra.upper() not in ['A', 'E', 'I', 'O', 'U']:
        arribo(cola_no_vocales, letra)
    arribo(caux, letra)

while (not cola_vacia(caux)):
    letra = atencion(caux)
    arribo(cdatos, letra)

# si hay datos, los imprimimos, sino avisamos que no hay datos y cancelamos la ejecucion
if (not cola_vacia(cola_no_vocales)):
    print('Datos de la cola sin vocales')
    barrido(cola_no_vocales)
    # pregunta si quiere ver las colas de entrada y salida, si es positivo las imprime por consola.
    opcion = validar_string("Desea ver las colas de entrada y salida? SI = ver, NO = no ver: ")
    if (opcion.lower() == "si"):
        print("cola de caracteres totales: ")
        barrido(cdatos)
        print("cola sin vocales: ")
        barrido(cola_no_vocales)
else:
    print("La cola de datos esta vacia, se cancelo la ejecución.")

