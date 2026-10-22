"""
Un string(str) es una secuencia de caracateres, que pueden ser letras, numeros, espacios, caracteres y emojis
se pueden crear con comillas simples o dobles, ya igual siempre que que abra y cierre
"""

a = "hola"
b = "python"
print(type(a))
print(type(b))

# para usar comillas dentro de un texto y que se vea a la hora de imprimir
print("espero que se encuentren muy 'bien'")
print('espero que se encuentren muy "bien"')
print("espero que se encuentren muy \"bien\"") # espaciado con \

# 2. caracteres de escape
# la barra \ le da un significado muy importante al caracter que le sigue

# \n salto de linea
print("linea 1 \nlinea 2 \nlinea 3")

# \t tabulacion
print("mi nombre es: \tharrys")

# \\ doble barra para usar 1
print("C:\\home\\user\\documents")

# 3. strign de varias lineas
