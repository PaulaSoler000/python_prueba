#condicionales

# if
my_condition = True

if my_condition:  # Es lo mismo que if my_condition == True:
    print("Se ejecuta la condición del if") # si es igual al valor se ejecuta el print, en el caso contrario este no se muestra

print("La ejecución continúa")

my_condition = 5 * 2

if my_condition == 10:
    print("Se ejecuta la condición del segundo if")

print("La ejecución continúa")

if my_condition > 10:
    print("Se ejecuta la condición del tercer if")

print("----------------------------")

# if, elif, else

if my_condition > 10:
    print("Es  mayor que 10")
else:
    print("Es menor o igual que 10")

my_condition = 5 * 5

if my_condition > 10 and my_condition < 20:
    print("Es mayor que 10 y menor que 20")
elif my_condition == 25:
    print("Es igual a 25")
else:
    print("Es menor o igual que 10 o mayor o igual que 20 o distinto de 25")

print("La ejecución continúa")

print("----------------------------")

# Condicional con ispección de valor

my_string = ""

if not my_string:
    print("Mi cadena de texto es vacía")

if my_string == "Mi cadena de textoooooo":
    print("Estas cadenas de texto coinciden")