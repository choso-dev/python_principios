# hablemos de variables ejejej
# una variables es como una caja donde almaxacenas algun tio de datos
# nombre = valor

Myvariables = "my variable de cadena de texto"
print(Myvariables)

# tipo de formas de nombrar una variable(esta se recomienda para python)
# 1. snake-case = mi_variable_favorita
# 2. camel-case = miVariableFavorita
# 3. pascal-case = MiVariableFavorita
# 4. kebab-case =  mi-variable-favorita
my_variables =  "my variable de cadena de texto"


# variables con diferentes tipos de datos 
# string
mi_string = "este es un texto"

# entero
mi_entero = 5

# float
mi_flotante = 1.77

# booleano
mi_bool = False




# concatenacion de cadenas 
print("hola", "yo", "soy", "python")
# tambien lo podemos hacer con varias variables
print(mi_string, mi_entero, mi_flotante, mi_bool) # podemos mezclar varias variables o argumentos separandolos por ,



# funcines integradas de python
# str() convertir en texto
print(str(mi_entero))

# int() convertir en entero
print(int(mi_flotante))

# float() convertir en flotante
print(float(mi_entero))

#len() contar cuantos elementos tiene una string
print(len(mi_string)) #cuenta cuantos elementos


# variables en un sola linea(aunque se puede hacer no es muy buena practica ok?)
nombre, apellido, alias, edad = "harry", "gonlez", "choso", 20
print("me llamo:", nombre, apellido, ". me dicen: ", alias, "y tengo", edad)


# input() solicitar datos por la consola
primer_nombre = input("cual es tu primer nombre: ")
edad = input("cuantos anios tenes:")


print("tu nombre es:", primer_nombre)
print("y tienes", edad)







