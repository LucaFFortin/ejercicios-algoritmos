def serie_recursiva(numero):
    if (numero == 1): return 1
    else: return numero / serie_recursiva(numero - 1)

print(serie_recursiva(2))