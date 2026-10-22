# Calentamiento (variables, input, sintaxis)


# 1. Crea 4 variables: nombre, edad, altura y es_estudiante. Imprime cada una junto a su type().
nombre = "harrys"
edad = 21
altura = 1.78
es_estudiante = True
print(type(nombre))
print(type(edad))
print(type(altura))
print(type(es_estudiante))
print("-" * 40)

# 2. Tienes a = 5 y b = 9. Intercambia sus valores sin perder ninguno. Bonus: investiga cómo se hace en una sola línea en Python.
a = 5
b = 9

c = a # cree otra variable para guardar el valor que se iba a borrar
a = b
b = c

print(a , b)
print("-" * 40)

# 3. Pide dos números con input() y muestra su suma. Ojo con el tipo que devuelve input().
n = int(input("ingrese un numero: "))
nn = int(input("ingrese un sumero para sumarlo con el anterior: "))
print(n + nn)

print("-" * 40)

# 4. Pide el año de nacimiento y muestra la edad aproximada que tiene este año (2026).

edad = int(input("ingrese tu edad para adivinar tu anio de nacimiento: "))
anio_actual = 2026
print(anio_actual - edad)