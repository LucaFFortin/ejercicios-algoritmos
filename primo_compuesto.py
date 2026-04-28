import math

# Método 1: Fórmula de Wilson
def es_primo_wilson(n):
    return math.factorial(n - 1) % n == n - 1

print("primos con formula de wilson")
print("2 es primo?", es_primo_wilson(2))
print("3 es primo?", es_primo_wilson(3))
print("4 es primo?", es_primo_wilson(4))
print("5 es primo?", es_primo_wilson(5))
print("6 es primo?", es_primo_wilson(6))

# Método 2: Por bucle (Raíz cuadrada)
def es_primo(n):
    base = math.sqrt(n)
    contador = math.floor(base)
    
    while (contador >= 2):
        if (n % contador == 0):
            return False
        contador -= 1
    return True

print("primos por bucle")
print("2 es primo?", es_primo(2))
print("3 es primo?", es_primo(3))
print("4 es primo?", es_primo(4))
print("5 es primo?", es_primo(5))
print("11 es primo?", es_primo(11))