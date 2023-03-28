# operadores

print(4 + 5)
print(4 - 5)
print(4 * 5)
print(4 / 5)
print(10 % 2)  # el resto de la división
print(10 // 3)  # division con un resultado aproximado (resultado = 3)
print(10 / 3)  # resultado = 3.3333333
print(2 ** 3)  # numero elevado a otro número

print(2 ** 3 + 3 - 7 / 1 // 4)

print("Hola" + "Python")  # lo concatena todo
print("Hola " + "Python " + "¿qué tal?")
print("Hola " + str(5))  # forzamos a que el núero se convierta en string

"""
no funcionará
print("Hola" - "Python")
print("Hola " + 5)
print("Hola " * 2.5)
print("Hola " * 2.5 * 2)# no funcionará porque será un float (resultado es 5.0 no 5)
"""
# operaciones mixtas
print("Hola " * 5)
print("Hola " * (2 ** 3))

float = 2.5 * 2
print("Hola " * int(float))

# operadores comparativos
print(3 > 4)
print(3 < 4)
print(3 >= 4)
print(4 <= 4)
print(3 == 4)
print(3 != 4)
print(3 != 4 == 2)

print("-------------------")

# operaciones con cadenas de texto
print("Hola" > "Python")
print("Hola" < "Python")
print("Hola" <= "Python")
print("Hola" >= "Python")
print("Hola" == "Zola")  # se comprueba la ordenación alfabética
print("Hola" != "Python")

print("aaaa" >= "abaa")  # ordenación alfabética por ASCII
print("aaaa" >= "AAAA")  # tiene en cuenta las mayúsculas
print(len("aaaa") >= len("abaa"))  # cuenta caracteres

print("-------------------")

# operadores lógicos
print(3 > 4 and "Hola" > "Python")  # false y false es false
print(3 > 4 or "Hola" > "Python")  # false y false es false
print(3 < 4 and "Hola" < "Python")  # true y true es true
print(3 < 4 or "Hola" > "Python")  # true o false es true
print(3 < 4 or ("Hola" > "Python" and 4 == 4))
# print(3 > 4 not "Hola" > "Python") (da error)
print(not (3 > 4))
