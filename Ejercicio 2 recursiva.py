def factorial(n):
    """
    Esta funcion devuelve el factorial del numero introducido en <numero>
    Entradas:
        -n: numero sobre el que se calcula el factorial
    Salidas:
        -factorial: resultado factorial del numero introducido en <numero>
    """
    if n == 0:
         return 1
    else:
        return n * factorial(n-1)
factorial(7)
print(factorial(7))
help(factorial)
