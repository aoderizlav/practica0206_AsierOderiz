def binario(numero_decimal):
    """
    Función que convierta un número decimal en binario
    Parametros:
    -numero_decimal: numero usado para convertirlo en decimal
    Salidas:
    -Devuelve un numero decimal en binario
    """
    binario = 0
    multiplo = 1
    while numero_decimal != 0:
        binario = binario + numero_decimal % 2 * multiplo
        numero_decimal //= 2
        multiplo *= 10
    return binario
numero_decimal = int(input("Numero decimal: \n"))
print(binario(numero_decimal))
help(binario)

def decimal(numero_binario):
    """
        Función que convierta un número binario en decimal
        Parametros:
        -numero-binario: numero usado para convertirlo en binario
        Salidas:
        -Devuelve un numero binario en decimal
    """
    decimal = 0
    for posicion, digito in enumerate(numero_binario[::-1]):
        decimal += int(digito) * 2 ** posicion
    return decimal
numero_binario = input("Numero binario: \n")
print(decimal(numero_binario))
help(decimal)


