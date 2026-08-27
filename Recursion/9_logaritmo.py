import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from utils import limpiar
from validaciones import validar_numero
import math


def logaritmo_recursivo(base, exp):
    if (base <= 0 or base == 1 or exp <= 0):
        print("Por definicion, la base debe ser mayor a 0 y diferente de uno, el exponente debe ser mayor a 0")
        return
    
    if (exp <= 1): return 0
    else: return 1 + logaritmo_recursivo(base, math.floor(exp / base))

# main
limpiar()

base = validar_numero("Ingrese el numero base: ")
exponente = validar_numero("Ingrese el exponente de la base: ")

print(f"El logaritmo en base {base} de {exponente} es igual a: {logaritmo_recursivo(base, exponente)}")