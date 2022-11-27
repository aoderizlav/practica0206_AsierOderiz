def area_circulo(radio):
    """
    Funcion que calcula el adea de unc circulo
    Parametros:
    -radio: es el radio que se usa para calcular el area
    Salidas:
    -Devuelve el area de un circulo
     """
    return 3.14 * radio **2
print(area_circulo(4))
help(area_circulo)

def volumen_cilindro(altura):
    """
    Funcion que calcula el volumne de un cilindro
    Parametros:
        -altura: es la altura que se usa para calcular el volumen
    Salidas:
        -Devuelve el volumen de un cilindro
    """
    area = area_circulo(4)
    return area * altura
print(volumen_cilindro(2))
help(volumen_cilindro)
