# strings

my_string = "Mi String"
my_other_string = 'Mi otro String'

print(len(my_string))
print(len(my_other_string))
print(my_string + " " + my_other_string)

my_new_line_string = "Este es un String\ncon salto de línea"
print(my_new_line_string)

my_tab_string = "\tEste es un String con tabulación"
print(my_tab_string)

my_scape_string = "\\tEste es un String \\n escapado"
print(my_scape_string)

print("-----------------")

# Formateo
name, surname, age = "Brais", "Moure", 35

print("Mi nombre es %s %s y mi edad es %d" % (name, surname, age))
print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))  # con format no se pone %s, son con llaves
print("Mi nombre es " + name + " " + surname + " y mi edad es " + str(age))  # forma menos aconsejada
print(f"Mi nombre es {name} {surname} y mi edad es {age}")  # hay que poner una f(formatear) delante para que funcione
"""
%s string
%d int
"""
print("-----------------")

# Desempaqueado de caracteres
language = "python"
a, b, c, d, e, f = language  # hay que poner el total de numeros de caracteres para que funcione
print(a)
print(e)

print("-----------------")

# División
language_slice = language[1:3]  # muestra de la segunda letra hasta la 3 sin  contar la 3
print(language_slice)

language_slice = language[1:]  # muestra desde la sgunda letra hasta el final
print(language_slice)

language_slice = language[-2]  # la segunda desde el final
print(language_slice)

language_slice = language[0:6:2]  # selecciona los caracteres que no se van a mostrar
print(language_slice)

print("-----------------")
# Reverse
reversed_language = language[::-1]  # muestra la cadena al reves
print(reversed_language)

print("-----------------")
# Funciones del lenguaje
print(language.capitalize())  # pone la primera letra en mayuscula
print(language.upper())  # Pone todas las letras en mayusculas
print(language.count("t"))  # cuenta la cantidad de letras
print(language.isnumeric())  # nos dice si es un numero
print("1".isnumeric())
print(language.lower()) # pone la cadena a minuscula
print(language.lower().isupper()) # pasamos a minuscula y despues preguntamos si esta en mayuscula
print(language.startswith("Py")) #python empieza con Py? si mo coincide da false
print("Py" == "py")  # No es lo mismo
