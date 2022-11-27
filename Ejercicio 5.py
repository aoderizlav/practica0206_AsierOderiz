def cuadrados (lista_numeros):
    """
    Funcion que muestra una lista de numeros y devuelve otra lista con sus cuadrados
    Parametros:
    -lista_numeros: numeros de la lista usados para calcular sus cuadrados
     Salidas:
     -Devuelve ota lista con sus cuadrados
    """
    lista_cuadrado = []
    for numero_cuadrado in lista_numeros:
        exp = numero_cuadrado ** 2
        lista_cuadrado.append(exp)
    return lista_cuadrado

lista_numeros = []
while True:
    num = float(input("Introduce una lista de numeros: \n"))
    if num == 0:
        break
    lista_numeros.append(num)
print(cuadrados(lista_numeros))
help(cuadrados)
