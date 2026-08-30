import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from utils import limpiar
from validaciones import validar_numero
import math

def contador_digitos_recursivo(num):
    if (type(num) != type(1)): return "El tipo de dato ingresado es incorrecto."
    
    if (num > 9):
        return 1 + contador_digitos_recursivo(math.floor(num / 10))
    else: return 1

# main
limpiar()

numero = validar_numero("Ingrese el numero a contar los digitos: ")

print(f"la cantidad de digitos de {numero} es igual a: {contador_digitos_recursivo(numero)}")