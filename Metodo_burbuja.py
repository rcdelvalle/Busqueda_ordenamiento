"""
Armar una funcion que se llame rankingConcesionarias(datos) y reciba
un parametro datos que sera un diccionario.
Al invocarla debera ordenar de mayor a menor las concesionarias segun la 
cantidad de ventas.
Finalmente debera imprimir exactamente:
{NOMBRE_CONCESIONARIA} : {VENTAS} ventas
{NOMBRE_CONCESIONARIA} : {VENTAS} ventas
{NOMBRE_CONCESIONARIA} : {VENTAS} ventas
{NOMBRE_CONCESIONARIA} : {VENTAS} ventas
{NOMBRE_CONCESIONARIA} : {VENTAS} ventas
"""

datos = {
    "autos":["FIAT Cronos", "Peugeot 208", "Toyota Hilux", 
             "Volkswagen Amarok", "Chevrolet Cruce"],
    "concesionarias":["Valmotors FIAT", "Kansai Toyota",
                      "Le Meridien Peugeot", "San Jorge", "Dietrich"],
    "registros":[
        {'nro_registro':1, 'nro_concesionaria':2, 'nro_producto':3, 'ventas':14543},
        {'nro_registro':2, 'nro_concesionaria':4, 'nro_producto':5, 'ventas':10605},
        {'nro_registro':3, 'nro_concesionaria':1, 'nro_producto':1, 'ventas':25580},
        {'nro_registro':4, 'nro_concesionaria':5, 'nro_producto':4, 'ventas':12525},
        {'nro_registro':5, 'nro_concesionaria':3, 'nro_producto':2, 'ventas':15282}
    ]
}

"""
Armar una funcion que se llame rankingConcesionarias(datos) y reciba
un parametro datos que sera un diccionario.
"""
def rankingConcesionarias(datos):
    # ordenar de mayor a menor las concesionarias segun la cantidad de ventas.
    burbuja(datos['registros'])

    # Finalmente debera imprimir exactamente:
    imprimirRanking(datos['registros'], datos['concesionarias'])

def burbuja(lista) :
    """Método de ordenamiento burbuja"""
    for i in range(0, len(lista)-1) :
        for j in range(0, len(lista)-i-1) :
            if (lista[j] ['ventas'] < lista[j+1] ['ventas']) :
                lista[j], lista[j+1] = lista[j+1], lista[j]

def imprimirRanking(registros, concesionarias):
    for registro in registros:
        print(f'{concesionarias[registro["nro_concesionaria"]-1]} : {registro["ventas"]} ventas')

rankingConcesionarias(datos)