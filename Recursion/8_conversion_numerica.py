import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from utils import limpiar
from validaciones import validar_numero

import math

def conversion_binaria_recursiva(numero):
    if (numero < 0): numero = abs(numero)
    if (numero == 0): return "0"
    if (numero == 1): return "1"
    else: 
        if (numero % 2 == 1): return conversion_binaria_recursiva(math.floor(numero / 2)) + "1"
        else: return conversion_binaria_recursiva(math.floor(numero / 2)) + "0"

# main
limpiar()

numero = validar_numero("Ingrese el numero a convertir en binario: ")

print(f"{numero} en formato binario es: {conversion_binaria_recursiva(numero=numero)}")
