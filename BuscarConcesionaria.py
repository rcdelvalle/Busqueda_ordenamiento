"""
Armar una funcion que se llame buscarConcesionaria() y reciba dos 
parametros (datos, concesionaria) que seran un diccionario y un string.
Al invocarla debera hacer una busqueda binaria para encontrar el indice 
de la concesionaria que se busca, y luego debera realizar una busqueda 
secuencial en los registros para identificar los valores de la concesionaria.
Finalmente debera imprimir exactamente:
Registro Nro: {NRO_REGISTRO}
Concesionaria Nro: {NRO_CONCESIONARIA} - {NOMBRE_CONCESIONARIA}
Producto Nro: {NRO_PRODUCTO} - {NOMBRE_PRODUCTO}
Cantidad vendida: {VENTAS}
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
Armar una funcion que se llame buscarConcesionaria() y reciba dos 
parametros (datos, concesionaria) que seran un diccionario y un string.
"""
def buscarConcesionaria(datos, concesionaria):

    """
    Al invocarla debera hacer una busqueda binaria para encontrar el indice 
    de la concesionaria que se busca
    """
    posicionA = binaria(datos["concesionarias"], concesionaria)

    """
    y luego debera realizar una busqueda secuencial en los registros 
    para identificar los valores de la concesionaria.
    """
    posicionB = secuencial(datos['registros'], posicionA + 1)

    # Finalmente debera imprimir exactamente:
    imprimirDatos(datos['registros'][posicionB], datos['autos'], datos['concesionarias'])

def binaria(lista, buscado) :
    """ Metodo de busqueda binaria """
    posicion = -1
    primero = 0
    ultimo = len(lista) - 1

    while (primero <= ultimo) and (posicion == -1) :
        medio = (primero + ultimo) // 2

        if (lista[medio] == buscado) :
            posicion = medio
        else :
            if (buscado < lista[medio]) :
                ultimo = medio - 1
            else :
                primero = medio + 1

    return posicion

def secuencial(lista, buscado) :
    """ Metodo de busqueda secuencial """
    posicion = -1

    for i in range(0, len(lista)) :
        if (lista[i]['nro_concesionaria'] == buscado) :
            posicion = i

    return posicion

def imprimirDatos(registro, autos, concesionarias):
    # Registro Nro: {NRO_REGISTRO}
    print(f"Registro Nro: {registro['nro_registro']}")

    # Concesionaria Nro: {NRO_CONCESIONARIA} - {NOMBRE_CONCESIONARIA}
    print(f"Concesionaria Nro: {registro['nro_concesionaria']} - {concesionarias[registro['nro_concesionaria']-1]}")
    
    # Producto Nro: {NRO_PRODUCTO} - {NOMBRE_PRODUCTO} 
    print(f"Producto Nro: {registro['nro_producto']} - {autos[registro['nro_producto']-1]}")
    
    # Cantidad vendida: {VENTAS} 
    print(f"Cantidad vendida: {registro['ventas']} ")

buscarConcesionaria(datos, "Dietrich")
