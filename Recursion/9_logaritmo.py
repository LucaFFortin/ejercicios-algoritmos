def logaritmo_recursivo(base, exp):
    if (exp == 1): return 0
    else: return 1 + logaritmo_recursivo(base, exp / base)

print(logaritmo_recursivo(2, 8))