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
# usadno las triples comillas respetas los saltos de lineas

poema = """hola 
esta es 
mi primera 
clase de 
python"""

print(poema)

# 4. concatenar y repetir
# usar el + solo une un string mas string, no suma, solo pega
print("hola" + " " + "python")
print("5" + "5") # no lo suma, solo pega porque es un string

print("ajjajaja" * 7)
print("-" * 20)
# siempre hay que tener en cuenta que todo lo que le pases a un input sera un string, si queires un entero o decimal tendrias que usar las funciones int() float()

# 5. longitud y pertenencias
texto = "hola Mundo"
print(len(texto)) # cuenta caracteres y espacios

print("Mundo" in texto)
print("comer" not in texto)


# 6. indices
# cada caracter de una cadena de texto tiene un posicion que empiensa por 0
# hola como
# 012345678

presenta = "hola mundo"
print(presenta[0]) # seria la primera letra
print(presenta[3])
print(presenta[7])
print("-" * 30)
# tambien podemos usar numeros negativos pero el -1 empienza desde el ultimo caracter hasta el inicio
print(presenta[-1])
print(presenta[-3])
print(presenta[-8])

# 7. slicing(rebanadas)
# sirve para sacar pesazos de un string con [inicio:fin:paso]
presenta = "hola mundo"

print(presenta[0:4])
print(presenta[5:])
print(presenta[-5:])

print(presenta[ : :2])
print(presenta[ : :3])

print(presenta[2: :2])

# un truquito para invertir 
print(presenta[::-1])

# 8. los string son inmutables
s = "hola"
print(s)
# s[0] = "H" esto nos daria un error porque nos string no se pueden modificar

# lo que se puede hacer es crear un nuevo string y se le cambia en caracter
s = "H" + s[1:] # cpm esto le estamos diciendo que desde que la posicion 0 ya tiene algo y del 1 en adelante sera igual
print(s)


# 9. f-string la forma moderna de armar texto
nombre = "harrys"
edad = "20"

# normalmente hacemos
print("mi nombre es:", nombre, "y tengo", edad, "de edad")

# ahora solo pones un f antes de las "" y por cada varible pones {}
print(f"mi nombre es {nombre} y tengo {edad} de edad")
# y de esta frma puedes darle forma a los de adentro
pi = 3.14159265
n = 1234567
print(f"{pi:.2f}") # con esto le decimos que queremos las los 2 despues de la . ,
print(f"{n:,}")    # y con eto los separamos por miles

print(f"{0.300:.1%}")


# Metodos en string(IMPORTANTES)
