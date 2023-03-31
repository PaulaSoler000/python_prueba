# funciones

def my_function():
    print("Esta es una función")


my_function()
my_function()
my_function()

print("-----------------------")


# Función con parámetros de entrada/argumentos

def sum_two_values(first_value, second_value):
    # no hace falta especificar (first_number:int) porque el tipado es dinámico
    # no podemos forzar a que un objeto sea de un tipo de dato concreto
    print(first_value + second_value)


sum_two_values(5, 7)
sum_two_values(52323, 74343)
sum_two_values("5", "7")  # son textos, las cadenas de textos no pueden hacer todas las operaciones
sum_two_values(1.4, 5.2)

print("-----------------------")


# Función con parámetros de entrada/argumentos y retorno

def sum_two_values_with_return(first_value, second_value):
    return first_value + second_value


my_result = sum_two_values_with_return(10, 5)  # no hace nada


def sum_two_values_with_return(first_value, second_value):
    return first_value + second_value


my_result = sum_two_values(1.4, 5.2)
print(my_result)

my_result = sum_two_values_with_return(10, 5)
print(my_result)


def sum_two_values_with_return(first_value, second_value):
    my_sum = first_value + second_value
    return my_sum


print("-----------------------")


# Función con parámetros de entrada/argumentos por clave

def print_name(name, surname):
    print(f"{name} {surname}")


print_name("Paula", "Soler")

print_name(surname="Soler", name="Pino")  # cambiar el orden

print("-----------------------")


# Función con parámetros de entrada/argumentos por defecto

def print_name_with_default(name, surname, alias="Sin alias"):
    # asignar un valor por defecto, si no le pasas el alias va a seguir funcionando
    print(f"{name} {surname} {alias}")


print_name_with_default("Paula", "Soler")
print_name_with_default("Paula", "Soler", "Pino")

print("-----------------------")


# Función con parámetros de entrada/argumentos arbitrarios

def print_upper_texts(*texts):  # el asterisco sirve para pasar múltiples textos
    print(type(texts))
    for text in texts:
        print(text.upper())


print_upper_texts("Hola", "Python", "Paula")
print_upper_texts("Hola")
