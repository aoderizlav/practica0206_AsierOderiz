def factorial_iterativo(numero):
    """
    Esta funcion devuelve el factorial del numero introducido en <numero>
    Entradas:
        -numero: numero sobre el que se calcula el factorial
    Salidas:
        -fac: resultado factorial del numero introducido en <numero>
    """
    fac = 1
    for n in range(1, numero + 1):
        fac = fac * n
    return fac
print(factorial_iterativo(7))
help(factorial_iterativo)





