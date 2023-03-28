import pandas
from tqdm import tqdm

"""archivo_excel= "AC_ASIGNATURA.xlsx"

excel_asignatura= pandas.read_excel(archivo_excel)

print(excel_asignatura)"""

# 1º Leer los 2 excel, iterar por cada línea y buscar los elementos vacíos

archivo_excel_aignatura = "AC_ASIGNATURA.xlsx"
archivo_excel_departamento = "AC_ASIGNATURASDEPARTAMENTOS.xlsx"

excel_asignatura = pandas.read_excel(archivo_excel_aignatura, keep_default_na=False)
excel_departamentos = pandas.read_excel(archivo_excel_departamento, keep_default_na=False)

"""
for index, row in tqdm(excel_departamentos.iterrows()):

    columna_departamento= row[0]
    columna_asignatura= row[1]

    if columna_departamento == "":
        print("La asignatura:", columna_asignatura, "no tiene código de departamento")


for index2, row2 in tqdm(excel_asignatura.iterrows()):

    columna_descripcion = row2[2]
    columna_clase= row2[1]

    if columna_descripcion == "":

        print("La fila :", columna_clase, "no tiene descripción")
        #print ("La línea:", index2, "no tiene descripcion")

"""

# 2º cambiar el tipo de dato de una columna -> Pista dtypes o convert_dtype
# para transformar los valores Enteros en Int y no object
"""
print(excel_asignatura.dtypes)

excel_asignatura['CODIGO'] = excel_asignatura['CODIGO'].astype('float64')

print(excel_asignatura.dtypes)

"""

# 3º Buscar en el excel AC_ASIGNATURASDEPARTAMENTOS que los codigos de la columna asignatura existan en el excel
# AC_ASIGNATURA -> Pista una funcion que se llama isin y pasar una columna a to_list()

for index, row in tqdm(excel_departamentos.iterrows()):

    columna_codigo_departamentos = row[1]

    if columna_codigo_departamentos in excel_asignatura['CODIGO']:
        print("encontrado")

