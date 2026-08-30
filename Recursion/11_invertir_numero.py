import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from utils import limpiar
from validaciones import validar_numero
from math import floor

# el parametro invertido funciona como un acumulador
def invertir_numero_recursivo(num, invertido=0):
    if (num <= -1): num = abs(num)
    
    if (num <= 0): return invertido
    else:
        return invertir_numero_recursivo(floor(num / 10), invertido * 10 + (num % 10))


# main
limpiar()

numero = validar_numero("Ingrese el numero a invertir: ")

print(f"el numero {numero} invertido queda como: {invertir_numero_recursivo(numero)}")