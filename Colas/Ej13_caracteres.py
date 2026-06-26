"""
Dada una cola de 50000 caracteres generados aleatoriamente realizar las siguientes actividades:
a. separarla en dos colas una con dígitos y otra con el resto de los caracteres.
b. determinar cuántas letras hay en la segunda cola.
c. determinar además si existen los caracteres “?” y “#”.
"""
import random
import math
from tda_colas import Cola, nodoCola, arribo, atencion, mover_al_final, cola_vacia, barrido, en_frente, tamanio

# Letras minúsculas del alfabeto oficial 
LETRAS_MINUSCULAS = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
    'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

# Letras mayúsculas del alfabeto oficial
LETRAS_MAYUSCULAS = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
    'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]

# Vocales con acento agudo
VOCALES_ACENTUADAS_MIN = ['á', 'é', 'í', 'ó', 'ú']
VOCALES_ACENTUADAS_MAY = ['Á', 'É', 'Í', 'Ó', 'Ú']

NUMEROS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# Vocales con diéresis
VOCALES_DIERESIS_MIN = ['ü']
VOCALES_DIERESIS_MAY = ['Ü']

# Todas las letras unificadas en una variable
LETRAS_TOTAL = (
    LETRAS_MINUSCULAS 
    + LETRAS_MAYUSCULAS 
    + VOCALES_ACENTUADAS_MIN 
    + VOCALES_ACENTUADAS_MAY 
    + VOCALES_DIERESIS_MIN 
    + VOCALES_DIERESIS_MAY
)

# Signos de puntuación y entonación comunes y exclusivos
SIGNOS_ESPANOL = [
    '¿', '?', '¡', '!', '.', ',', ';', ':', '-', '(', ')', '"', '»', '«', '#'
]

# Todos los caracteres posibles, combinando las listas anteriores
TODOS_LOS_CARACTERES = (
    LETRAS_MINUSCULAS 
    + LETRAS_MAYUSCULAS 
    + VOCALES_ACENTUADAS_MIN 
    + VOCALES_ACENTUADAS_MAY 
    + VOCALES_DIERESIS_MIN 
    + VOCALES_DIERESIS_MAY
    + SIGNOS_ESPANOL
    + NUMEROS
)

char_resto = Cola()
digitos = Cola()
existe_simbolo = False
contador_letras = 0

while (tamanio(char_resto) < 50000):
    caracter = random.choice(TODOS_LOS_CARACTERES)
    if (caracter in ['?', '#']):
        existe_simbolo = True
    if (caracter in NUMEROS):
        arribo(digitos, caracter)
    else:
        if (caracter in LETRAS_TOTAL):
            contador_letras += 1
        arribo(char_resto, caracter)

barrido(char_resto)
print(tamanio(char_resto))