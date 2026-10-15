# OPERADORES

# operadores aritmeticos:
# suma (+)
print(7 + 2)

# resta (-)
print(7 - 2)

# multiplicacion (*)
print(7 * 2)

# division (/) # una cosa de la division es que siempre devuelve un float, no entero
print(7 / 2)

# division entera (//) # aqui redondea hacia abajo, no hacia arriba
print(7 // 2)

# modulo (%) devuelve lo que queda una division
print(7 % 2)

# potencia (**)
print(7 ** 2)

# algo que nos pueda servir un poco mas adelante es que podemos usar (+) y (*) con cadenas de texto
print("ja" * 5)
print("hola" + "como" + "estas")


# Asignacion:
# es igual (=)
x = 10
print(x)

# es igual mas(+=)
x += 3
print(x)

# es igual menos (-=)
x -= 1
print(x)

# es igual por(*=)
x *= 2
print(x)

# es igual division
x /= 4
print(x)

# Comparacion
# siempre devulven False o True
# igual a (==)
print(5 == 5)

# distinto de (!=)
print(5 != 5)

# mayor que (>)
print(5 > 6)

# menor que (<)
print(5 < 6)

# mayor o igual que (>=)
print(5 >= 6)

# menor o igual que (<=)
print(5 <= 6)

# Logicos
edad = 20

# su salida siempre va hacer verdadera si las 2 son verdaderas, si una es falsa entonces todo sera falso
print(edad >= 18 and edad <= 19)

# su salida sera verdadera si al menos 1 en verdadera
print(edad >= 17 or edad <= 19)

# not solo invierte si valor
z = False
y = True
print(not z)
print(not y)


# Identidad

# is	¿son el mismo objeto?
# is not	¿son objetos distintos?

a = [1, 2]
b = [1, 2]
a == b      # True  (mismo contenido)
a is b      # False (objetos distintos en memoria)


# Pertenencia

# in	¿está dentro de...?
# not in	¿no está dentro de...?

print("py" in "python")      # True
print(3 in [1, 2, 3])        # True
print("x" not in "abc")      # True








