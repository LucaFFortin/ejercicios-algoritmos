import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))
from tda_colas import Cola, nodoCola, arribo, atencion, mover_al_final, cola_vacia, barrido, en_frente, tamanio
from validaciones import validar_string

cdatos = Cola()
cola_no_vocales = Cola()

letra = validar_string('Ingrese un caracter ')
while (letra != ''):
    arribo(cdatos, letra)
    letra = validar_string('Ingrese un caracter ')

while (not cola_vacia(cdatos)):
    letra = atencion(cdatos)
    if letra.upper() not in ['A', 'E', 'I', 'O', 'U']:
        arribo(cola_no_vocales, letra)

print('Datos de la cola sin vocales')
barrido(cola_no_vocales)

