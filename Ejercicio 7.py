def contador_palabras(texto):
    """
    Es una funcion que crea un diccionario donde la clave es la cantidad de veces que aparece la palabara en el texto
    introducido y cada palabra es una entrada en el diccionario y el es valor
    Parametros:
    -texto: es el texto introducido
     Salidas:
     -dic_frecuencia: es el diccionario que tiene por claves la frecuancia y por el valor las palabras que componen el 
     texto
    """
    palabras = []
    dic_frecuencia = {}
    palabras = texto.split ()
    for i in palabras:
     dic_frecuencia[palabras.count(i)] = i
    return dic_frecuencia

def max_frec(diccionario):
    """
     Esa funcion usa el diccionario creado en la funcion contador_palabras y saca la palabra con mas frecuencia
     (mayor valor de la clave)
     Parametros:
     -diccionario: es la variable donde esta guardada el diccionario de la anterior funcion
     Salidas:
     -diccionario[max(frecuencia]: saca el valor asociada a la clave mas alta del del diccionario
    """
    frecuencia = diccionario.keys()
    return diccionario[max(frecuencia)]

texto = input("Introduzca el texto que quiere contear: \n")
diccionario = contador_palabras(texto)
print(contador_palabras)
help(contador_palabras)
print(max_frec)
help(max_frec)

