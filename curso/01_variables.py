# variables

mi_string_variable = "mi string"  # esta es la forma correcta de nombrar una variable
print(mi_string_variable)

mi_int = 5
print(mi_int)

mi_int_a_str = str(mi_int)  # cambia el int a string
print(mi_int_a_str)
print(type(mi_int_a_str))

mi_bool = False
print(mi_bool)

print(mi_string_variable, mi_int, mi_bool)
print(type(print("comentario")))  # tipo "nonetype"

print("Este es el valor de:", mi_bool)

# funciones del sistema
print(len(mi_string_variable))  # cuenta los caracteres con espacios

# variables en una sola linea (no es aconsejable mezclar variables)
name, surname, alias, age = "Mario", "García", "MarioGarcia", 20
print("Me llamo:", name, surname, ", mi edad es:", age, "y mi alias es:", alias)

# input (no es habitual utilizarlo)
"""
al ser una variable se sobreescribe el valor
"""
"""
name = input('¿Cuál es tu nombre? ')
age = input('¿Cuántos años tienes? ')

print(name)
print(age)
"""

"""
cambiamos su tipo (python no tiene un tipado fuerte, 
el problema es que se puede sobreescribir una variable sin querer)
"""
name = 20
age = "Mario"
print(name)
print(age)

# forzamos el tipo
address: str = "mi direccion"
address: int = 32
print(address)
print(type(address))
