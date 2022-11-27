def media(lista_numeros):
    """
    Funcion que muestra una lista de numeros y devuelve su media
    Parametros:
    -lista_numeros: numeros de la lista usados para calcular su media
     Salidas:
     -Devuelve la media de la lita de numeros
    """
    sumatorio = sum(lista_numeros)
    media = sumatorio / len(lista_numeros)
    return media

lista_numeros = []
while True:
    num = float(input("Introduce una lista de numeros: \n"))
    if num == 0:
        break
    lista_numeros.append(num)
print(media(lista_numeros))
help(media)
