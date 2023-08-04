# ¿Como leer un archivo de excel ?
import pandas
from pandas import DataFrame, unique

# https://www.w3schools.com/python/pandas/pandas_ref_dataframe.asp
ruta_excel = 'PARAMETRIZACIÓN.xlsx'

# 1º Opción. read excel. Solo podrá leer una hoja de excel
hoja_excel = pandas.read_excel(
    io=ruta_excel,  # La ruta de archivo para leerlo

    sheet_name='Catálogo Centros',
    # Para especificar qué hoja dentro del libro quiero leer. En caso de error, ValueError
    # sheet_name=1,  # Para leer la hoja puede ser un Str, un Int para coger la posición o una lista
    # sheet_name=[1,2],  # De esta manera las hojas se convienten en un array de hojas y accedemos a cada una por posicion

    header=0,  # Por defecto el nombre de las columnas está en la primera fila
    # header=None,  # Para cuando no tiene un encabezado específico
    # header=9,  # Esto es para definir en qué fila se encuentra el encabezado
    # header=[9,10],  # El emcabezado puede ser más de una fila combinada.

    dtype='string',  ### Para convertir todos los valores del excel a el tipo str
    keep_default_na=False,  # Los valores que sean nulos o vacíos no aparecerán como NaN
    decimal=',',  ## Para que cuando tengamos un valor decimal como texto, se pueda parsear a número

)

# .convert_dtypes() -> Cambiará el tipo de variable de cad columna a la más eficiente/comun.
# print(hoja_excel.dtypes)

# ### Metodo para leer el LIBRO excel y luego elegir la hoja que quieras.
# libro_excel = pandas.ExcelFile(path_or_buffer=ruta_excel)
# nombre_hojas = libro_excel.sheet_names
#
# # print(libro_excel)
# # print(nombre_hojas)
#
# for hoja in nombre_hojas:
#     hoja_cargada = pandas.read_excel(libro_excel, sheet_name=hoja)
#     print(hoja_cargada.columns)

# ¿Como seleccionar columnas en una hoja de excel?
# Por string -> hoja_excel['CÓDIGO CENTRO']
# Por una lista de string -> hoja_excel[['CÓDIGO CENTRO', 'ÚLTIMO NIVEL']]
# Por int -> hoja_excel[hoja_excel.columns[0]]
# Por una lista de int -> hoja_excel[[hoja_excel.columns[0],hoja_excel.columns[1]]]
# Sacar una nueva variabla para identificar la columna -> columna_a = hoja_excel.columns[0]
# Sacando una nueva variable y utilizandola para apntar a la columna -> hoja_excel[columna_a]

### FILTRAR INFORACION ###
## FILTRAR UNA COLUMNA
# filtro = hoja_excel.loc[hoja_excel[hoja_excel.columns[0]] == 'C13']

# Filtrar varias columnas
# filtro = hoja_excel.loc[
#     (hoja_excel[hoja_excel.columns[0]] != '') &
#     (hoja_excel[hoja_excel.columns[3]] == '')
# ]

# Filtrar con un listado de valores que quieres obtener
# filtro = hoja_excel.loc[
#     (hoja_excel['TIPO DE CENTRO'].isin(['DAG', 'MIXTO'])) &
#     (hoja_excel[hoja_excel.columns[3]] != '')
# ]

# Filtrar con un listado de valores que NO quieres obtener. Este símbolo se usará para decirlo contrario ~
# filtro = hoja_excel.loc[
#     ~(hoja_excel['TIPO DE CENTRO'].isin(['DAG', 'MIXTO'])) &
#     (hoja_excel[hoja_excel.columns[3]] != '')
# ]
# print(filtro)
# comprobacion_any_1 = hoja_excel.isin(['']).any()
# comprobacion_any_2 = hoja_excel['NIVEL SUPERIOR'].isin(['']).any()
# print(comprobacion_any_1)
# print(comprobacion_any_2)

# comprobacion_all_1 = hoja_excel.isin(['']).all()
# comprobacion_all_2 = hoja_excel['NIVEL SUPERIOR'].isin(['']).all()
# print(comprobacion_all_1)
# print(comprobacion_all_2)


# # Quedarme con valores únicos de una columna
# drop_primero: DataFrame = hoja_excel.drop_duplicates(subset=['CRITERIO DE REPARTO'])
#
# ### Tipo de variable SERIES
# drop_segundo = hoja_excel['CRITERIO DE REPARTO'].drop_duplicates()
#
# ### Tipo de variable DATAFRAME
# drop_tercero = hoja_excel[['CRITERIO DE REPARTO']].drop_duplicates()

### LISTAS

hoja_mp_centros = pandas.read_excel(ruta_excel,sheet_name='MP Centros', keep_default_na=False, dtype='string')
hoja_cat_act = pandas.read_excel(ruta_excel,sheet_name='Catálogo Actividades', keep_default_na=False, dtype='string')
lista_codigos_centros_tolist = hoja_excel[hoja_excel.columns[0]].values.tolist()  # Tipo variable list
lista_codigos_centros_unique = hoja_excel[hoja_excel.columns[0]].values.unique()  # Tipo variable es StringArray

listado_codigo_actividades = hoja_cat_act[hoja_cat_act.columns[0]].values.tolist()

listado_codigos_mp_centros = hoja_mp_centros[[hoja_mp_centros.columns[0], hoja_mp_centros.columns[2]]].values.tolist()

# for cen_act in listado_codigos_mp_centros:
# for index, row in hoja_mp_centros.iterrows():
#     centro = row[0]
#     actividad = row[2]
#
#     if centro not in lista_codigos_centros_tolist:
#         print(f"Este centro no se encuentra, {centro}")
#
#     if actividad not in listado_codigo_actividades:
#         print(f"Esta actividad no se encuentra, {actividad}")

# Nº de Unicos nunique()
# numeros_unicos = hoja_mp_centros.nunique()
# print(numeros_unicos)

hoja_valores = pandas.read_excel(ruta_excel, sheet_name='Valores Atributos', keep_default_na=False, dtype='string')
hoja_valores['Valores'] = hoja_valores['Valores'].astype('float')

# print(hoja_valores['Valores'].sum()) # SUMA
# print(hoja_valores['Valores'].max()) # MAXIMO
# print(hoja_valores['Valores'].min()) # MINIMO
# print(hoja_valores['Valores'].mean()) # MEDIA
# print(hoja_valores['Valores'].count()) # Contar el numero de filas, por ejemplo.

# count
# lambda

hoja_valores['COMPROBACION'] = hoja_valores['Valores'].apply(lambda codigo: comprobar_ceros(codigo))
print(hoja_valores['COMPROBACION'])


def comprobar_ceros(codigo):
    print(codigo)
    if codigo == 0:
        return False
    else:
        return True

# group by


# comprobar que una columna existe en la lista de columnas
if "identificador cce" in excel.columns:
    excel['hay cce'] = True
else:
    excel['hay cce'] = False

# Paramos todas las columnas a minúsculas
excel.columns = map(str.lower, excel.columns)