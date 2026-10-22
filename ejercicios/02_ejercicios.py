# Operadores


# 1. Pide dos números y muestra el resultado de los 7 operadores aritméticos con ellos.
print("ingresaras 2 numeros")
numero_uno = int(input("ingrese el numero 1: "))
numero_two = int(input("ingrese el numero 2: "))

print(numero_uno + numero_two)
print(numero_uno - numero_two)
print(numero_uno * numero_two)
print(numero_uno / numero_two) # mas adelante se tien que correguir el error de aqui
print(numero_uno % numero_two)
print(numero_uno // numero_two)
print(numero_uno ** numero_two)
print("-" * 40)


# 2. Pide un número y muestra True si es par y False si es impar. Usa %.
print("usaremos el numero 2 para este ejercicio")
print(numero_two % 2 == 0)
print("-" * 40)


# 3. Pide una cantidad de segundos y conviértela a horas, minutos y segundos. Ejemplo: 3725 → 1 h, 2 min, 5 s. Usa // y %.
segundos = int(input("ingrese una cantidad se segundos: "))
hora = segundos // 3600
minutos = int((segundos - (hora * 3600)) / 60)
n_segundo = segundos - (hora * 3600) - (minutos * 60)
print(f"{segundos}s seria {hora}:{minutos}:{n_segundo}")
print("-" * 40)

# 3. Pide un precio y un porcentaje de descuento y muestra el precio final con 2 decimales.
precio = int(input("ingrese el precio: "))
descuento = 15
print(f"el producto cuesta {precio} y con el descuento del 15% serian {(descuento * precio) / 100}")


# 4. Pide una edad y muestra con un solo print si está entre 13 y 17 años (inclusive). Luego haz otro que diga si es mayor de edad o menor de 5.
edad = int(input("ingrese una edad: "))
print(f"{edad > 13 and edad < 17}")
