import math

# Método 1: Fórmula de Wilson
def es_primo_wilson(n):
    return math.factorial(n - 1) % n == n - 1

# Método 2: Por bucle (Raíz cuadrada)
def es_primo(n):
    base = math.sqrt(n)
    contador = math.floor(base)
    
    while (contador >= 2):
        if (n % contador == 0):
            return False
        contador -= 1
    return True

# main
entrada = int(input("Ingrese el numero a verificar: "))
print("primos con formula de wilson")
print(es_primo_wilson(entrada))
print("primos por bucle")
print(es_primo(entrada))