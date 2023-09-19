"""
Ejercicio 4
Se dispone de una lista de películas con la siguiente información: título, año de
estreno, recaudación y valoración del público (de 1 a 5), los cuales debemos procesar
contemplando las siguiente tareas:
a) Realizar un listado ordenado por título de manera ascendente
b) Realizar un listado ordenado por año de lanzamiento de manera ascendente
c) Realizar un listado ordenado por recaudación de manera descendente;
d) Mostrar toda la información de la película que más recaudo;
e) Listar todas las películas que tenga valoración 5;
f) Determinar si la película “Avengers: Infinity War” está en la lista y
mostrar toda su información;
g) Indicar en qué posición se encuentra la película “Star Wars: The Return of
Jedi”;
h) Calcular el total recaudado por las películas que en su título incluyen la
palabra “Avengers”;
i) Mostrar todas las películas que se estrenaron en el año 2017;
j) Listar todas las películas que comienzan con la palabra “Iron”.
"""

lista_peliculas = [
    {'titulo':'Avatar', 'anio_estreno':2009, 'recaudación':2923706026,'valoracion_publico':4},
    {'titulo':'Avengers: Endgame', 'anio_estreno':2019, 'recaudación':2799439100,'valoracion_publico':5},
    {'titulo':'Avatar 2', 'anio_estreno':2022, 'recaudación':2320250281,'valoracion_publico':4},
    {'titulo':'Titanic', 'anio_estreno':1997, 'recaudación':2264743305,'valoracion_publico':4},
    {'titulo':'Star Wars: Episodio VII - El despertar de la Fuerza', 'anio_estreno':2015, 'recaudación':2071310700,'valoracion_publico':5},
    {'titulo':'Avengers: Infinity War', 'anio_estreno':2018, 'recaudación':2052415039,'valoracion_publico':4},
    {'titulo':'Spider-Man: No Way Home', 'anio_estreno':2021, 'recaudación':1921704167,'valoracion_publico':4},
    {'titulo':'Jurassic World', 'anio_estreno':2015, 'recaudación':1671537444,'valoracion_publico':3},
    {'titulo':'El Rey León', 'anio_estreno':2019, 'recaudación':1663075401,'valoracion_publico':4},
    {'titulo':'The  Avengers', 'anio_estreno':2012, 'recaudación':1520538536,'valoracion_publico':4},
    {'titulo':'Fast & Furious 7', 'anio_estreno':2015, 'recaudación': 1515341399,'valoracion_publico':4},
    {'titulo':'Top Gun: Maverick', 'anio_estreno':2022, 'recaudación':1493491858,'valoracion_publico':4},
    {'titulo':'Frozen II', 'anio_estreno':2019, 'recaudación':1450026933,'valoracion_publico':4},
    {'titulo':'Avengers: La era de Ultron', 'anio_estreno':2015, 'recaudación':1402809540,'valoracion_publico':4},
    {'titulo':'Super Mario Bros: La película', 'anio_estreno':2023, 'recaudación':1352294265,'valoracion_publico':4},
    {'titulo':'Black Panther', 'anio_estreno':2018, 'recaudación':1347597973,'valoracion_publico':4},
    {'titulo':'Harry Potter y las Reliquias de la Muerte: parte 2', 'anio_estreno':2011, 'recaudación':1342321665,'valoracion_publico':4},
    {'titulo':'Star Wars: Episodio VIII - Los últimos Jedi', 'anio_estreno':2017, 'recaudación':1332698830,'valoracion_publico':4},
    {'titulo':'Jurassic World: El Reino Caído', 'anio_estreno':2018, 'recaudación':1310466296,'valoracion_publico':4},
    {'titulo':'Frozen', 'anio_estreno':2013, 'recaudación':1281508100,'valoracion_publico':4},
]


# a) Realizar un listado ordenado por título de manera ascendente
def burbuja(lista):
    """Método de ordenamiento burbuja"""
    for i in range(0, len(lista)-1) :
        for j in range(0, len(lista)-i-1) :
            if (lista[j] ['titulo'] > lista[j+1] ['titulo']) :
                lista[j], lista[j+1] = lista[j+1], lista[j]

burbuja(lista_peliculas)
print(lista_peliculas)


# b) Realizar un listado ordenado por año de lanzamiento de manera ascendente
def burbuja(lista):
    """Método de ordenamiento burbuja"""
    for i in range(0, len(lista)-1) :
        for j in range(0, len(lista)-i-1) :
            if (lista[j] ['anio_estreno'] > lista[j+1] ['anio_estreno']) :
                lista[j], lista[j+1] = lista[j+1], lista[j]

burbuja(lista_peliculas)
print(lista_peliculas)


# c) Realizar un listado ordenado por recaudación de manera descendente;
def burbuja(lista) :
    """Método de ordenamiento burbuja"""
    for i in range(0, len(lista)-1) :
        for j in range(0, len(lista)-i-1) :
            if (lista[j] ['recaudación'] < lista[j+1] ['recaudación']) :
                lista[j], lista[j+1] = lista[j+1], lista[j]

burbuja(lista_peliculas)
print(lista_peliculas)

# d) Mostrar toda la información de la película que más recaudo;
print(lista_peliculas[0])

# e) Listar todas las películas que tenga valoración 5;
lista_peliculas_5 = []

for pelicula in lista_peliculas:
    
    if(pelicula['valoracion_publico']==5):
        lista_peliculas_5.append(pelicula)

print(lista_peliculas_5)


"""
f) Determinar si la película “Avengers: Infinity War” está en la lista y
mostrar toda su información;
"""
def secuencial(lista, buscado) :
    """ Metodo de busqueda secuencial """
    posicion = -1
    
    for i in range(0, len(lista)) :
        if (lista[i] == buscado) :
            posicion = i

    return posicion

buscado = 'Avengers: Infinity War'
print(secuencial(lista_peliculas, buscado))


"""
g) Indicar en qué posición se encuentra la película “Star Wars: The Return of
Jedi”;
"""
def secuencial(lista, buscado) :
    """ Metodo de busqueda secuencial """
    posicion = -1
    
    for i in range(0, len(lista)) :
        if (lista[i] == buscado) :
            posicion = i

    return posicion

posicion = secuencial(lista_peliculas, 'Star Wars: The Return of Jedi')

print(f"""la película “Star Wars: The Return of Jedi se encuentra
      en la posicion {posicion}""")


"""
h) Calcular el total recaudado por las películas que en su título incluyen la
palabra “Avengers”;
"""


# i) Mostrar todas las películas que se estrenaron en el año 2017;
lista_peliculas_2017 = []

for pelicula in lista_peliculas:
    
    if(pelicula['anio_estreno']==2017):
        lista_peliculas_2017.append(pelicula)

print(lista_peliculas_2017)


# j) Listar todas las películas que comienzan con la palabra “Iron”.
lista_peliculas_iron = []

for pelicula in lista_peliculas:
    
    if(pelicula['titulo'][0]=='Avatar'):
        lista_peliculas_iron.append(pelicula)

print(lista_peliculas_iron)