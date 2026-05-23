"""Dado un párrafo que finaliza en punto, separar dicho párrafo en tres pilas: vocales, consonantes y otros caracteres que no sean letras (signos de puntuación números, espacios, etc.). Luego utilizando las operaciones de pila resolver las siguientes consignas:
a. cantidad de caracteres que hay de cada tipo (vocales, consonantes y otros);
b. cantidad de espacios en blanco;
c. porcentaje que representan las vocales respecto de las consonantes sobre el total de caracteres del párrafo;
d. cantidad de números;
e. determinar si la cantidad de vocales y otros caracteres son iguales;
f. determinar si existe al menos una z en la pila de consonantes."""
from pilas import nodoPila, Pila, apilar, desapilar, pila_vacia, en_cima, tamanio, barrido


pila_vocales = Pila()
pila_consonantes = Pila()
pila_otros = Pila()

contador_vocales = 0
contador_consonantes = 0
contador_otros = 0
contador_espacios = 0
contador_numeros = 0
contiene_z = False

parrafo = input("Ingrese un parrafo terminado en punto: ")

for caracter in parrafo:

    if caracter.lower() == "a" or caracter.lower() == "e" or caracter.lower() == "i" or caracter.lower() == "o" or caracter.lower() == "u":
        apilar(pila_vocales, caracter)
        contador_vocales += 1

    elif caracter.lower().isalpha():
        apilar(pila_consonantes, caracter)
        contador_consonantes += 1

        if caracter.lower() == "z":
            contiene_z = True

    else:
        apilar(pila_otros, caracter)
        contador_otros += 1

        if caracter == " ":
            contador_espacios += 1

        if caracter.isdigit():
            contador_numeros += 1

total = contador_vocales + contador_consonantes + contador_otros

porcentaje = contador_vocales / contador_consonantes * 100

print("Cantidad de vocales:", contador_vocales)
print("Cantidad de consonantes:", contador_consonantes)
print("Cantidad de otros:", contador_otros)
print("Cantidad de espacios:", contador_espacios)
print("Cantidad de numeros:", contador_numeros)
print("Porcentaje de consonantes sobre vocales es de:", porcentaje, "%")

if contador_vocales == contador_otros:
    print("Vocales y otros son iguales")
else:
    print("Vocales y otros NO son iguales")

if contiene_z == True:
    print("Existe al menos una z")
else:
    print("No existe una z")