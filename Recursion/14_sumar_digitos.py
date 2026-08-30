import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from utils import limpiar
from validaciones import validar_numero
from math import floor

def sumar_digitos(num):
    if num <= -1: num = abs(num)

    if num <= 1: return num
    else:
        resultado = num % 10
        return sumar_digitos(floor(num / 10)) + resultado

# main
limpiar()

numero = validar_numero("Ingrese el numero para sumar sus digitos: ")

print(f"la cantidad de digitos de {numero} es igual a: {sumar_digitos(numero)}")