# Strings
# 1. Pide nombre y apellido. Muestra las iniciales (H.G.) y el nombre en formato Apellido, Nombre con cada palabra capitalizada, sin importar cómo lo haya escrito el usuario.
nombre = input("ingrese tu nombre: ")
apellido = input("ingrese tu apellido: ")
print(f"{nombre[0].upper()}. {apellido[0].upper()}.")
print(f"{nombre.lower().capitalize()} {apellido.lower().capitalize()}")


# Pide una frase y muestra cuántas veces aparece la letra “a” y en qué posición aparece por primera vez.
frase = input("escribe una frase: ")
print(f"la frase tiene {frase.count("a")} 'a' y la primera a esta en la posicion[{frase.find("a")}]")



# Limpia esta entrada para que quede Hola Mundo: " hOLA mUNDO ". (Cuidado con los espacios del medio.)
saludo = " hOLA mUNDO "
print(f"{saludo.lstrip().rstrip().lower().capitalize()}")


# Pide una palabra y di si es un palíndromo, sin importar mayúsculas (Ana, Neuquen...).
es = input("ingrese una palabra: ")
se = es[::-1]
print(es in se)



# Pide un correo, por ejemplo harry@gmail.com, y muestra por separado el usuario y el dominio.
correo = input("ingrese tu correo: ")
print(f"el usuario es: {correo.replace("@", " ").replace(" ", " dominio: ")}")


# Pide un texto y muéstralo centrado entre dos líneas de = cuyo largo sea el del texto más 4. Usa f-strings y *.
texto = input("ingrese un texto: ")
largo = len(texto)
print(f"{"=" * (largo + 4)}{texto}{"=" * (largo + 4)}")


# Pide una frase y una palabra a censurar, y reemplaza esa palabra por asteriscos del mismo largo. Ejemplo: "el perro corre", perro → "el ***** corre".

frase = input("ingresame una frase: ")
censura = input("que quieres censurar: ")
largo = len(censura)

print(f"{frase.replace(censura, "*" * largo)}")