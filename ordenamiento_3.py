"""
Ejercicio 3
Dada una lista de personajes de la saga de Star Wars de las que se conoce su nombre,
resolver la siguientes tareas:
a) Listar los personajes ordenados alfabéticamente de manera ascendente
b) Determinar si el personaje "Darth Maul" está cargado y en qué posición se
encuentra;
c) Mostrar la información de los personajes que se encuentran antes y después
de "Hera Syndulla";
d) Listar todos los personajes que comienzan con la letra L;
"""

lista_star_wars = ["Luke Skywalker", "Hera Syndulla", "Aayla Secura", "Ackbar", "Adi Gallia", 
"Agen Kolar", "Agrippa Aldrete", "Ahsoka Tano", "Anakin Skywalker", 
"Anakin Solo", "Asajj Ventress", "Ask Aak", "Attichitcuk", "Atton Rand", 
"Aurra Sing", "Bail Prestor Organa", "Bastila Shan", "BB-8", 
"Ben Skywalker", "Bendu","Jan Kong", "Bib Fortuna", "Biggs Darklighter", 
"Bo Keevil Bo-Katan","Bo Keevil", "Boba Fett", "Boga", "Bossk", "Bulduga", 
"C-21 Highsinger","C-3PO", "Cad Bane", "Yarua", "Chalmun", "Chewbacca", 
"Cincos (CT-27-5555)", "Clon 99", "Cody", "Daka", "Darth Bane", 
"Darth Caedus", "Darth Desolous", "Darth Maul", "Darth Malak", 
"Darth Phobos", "Darth Plagueis", "Darth Revan", "Darth Sidious", 
"Darth Tyranus", "Darth Vader", "Darth Zannah", "Darts D'Nar", 
"Daultay Dofine", "Depa Billaba", "Dengar", "Depa Billaba", "Derrown", 
"Dogma", "Dooku", "Dr. Evazan","Echuu-Shen Jon", "Embo", "Exiliado jedi", 
"Finis Valorum", "Finn","Flix","Freya Fenris", "Galen Marek", 
"Garven Dreis", "Ganodi", "Garnac", "Gasgano", "General Grievous", 
"Greedo", "Griff Halloran", "Gungi", "Gwarm", "Han Solo", "Hype Fazon", 
"IG-88", "Jabba el Hutt", "Jacen Solo","Jace Rucklin", "Jaina Solo", 
"Jango Fett", "Jar Jar Binks", "Jarek Yeager",
"Juno Eclipse", "Katuunko", "Kazdan Paratus", "Kazuda Xiono", 
"Ki-Adi-Mundi", "Kit Fisto", "Kylo Ren", "Lando Calrissian", "Lama Su",
"Leia Organa", "Lumiya", "Lobot", "Lorrino", "Lott Dod",
"Luminara Unduli", "Mace Windu", "Major Vonreg", "Mara Jade Skywalker",
"Maris Brood", "Max Rebo", "Mon Mothma", "Naat Reath", "Neeku Vozo", 
"Nute Gunray", "Obi-Wan Kenobi", "Orson Krennic", "Orka", "Padmé Amidala",
"Plo Koon", "Po Nudo", "Poe Dameron", "Poggle el Menor", "PROXY", "Yoda",
"Qui-Gon Jinn", "Rahm Kota", "Rabé", "R2-D2", "Rex", "Riff Tamson", 
"Riyo Chuchi", "Ruescott Melshi", "Rune Haako", "Rey (Star Wars)", 
"Sabine Wren", "San Hill", "Satine Kryze", "Sei Taria", "Shaak Ti", 
"Shmi Skywalker", "Sifo-Dyas", "Siri Tachi", "Sev'rance Tann", 
"Sheev Palpatine", "Stam Reath", "Sly Moore", "Tam Ryvora", 
"Tía Z Cantinera de Colossus", "Torra Doza", "Tenel Ka", "Snoke", 
"Unkar Plutt", "Visas Marr", "Vergere", "Wat Tambor", "Watto", 
"Wedge Antilles", "Wicket W. Warrick", "Xizor"]

# a) Listar los personajes ordenados alfabéticamente de manera ascendente
def seleccion(lista) :
    """Método de ordenamiento selección"""
    for i in range(0, len(lista)-1) :
        minimo = i
        for j in range(i+1, len(lista)) :
            if (lista[j] < lista[minimo]) :
                minimo = j

        lista[i], lista[minimo] = lista[minimo], lista[i]

seleccion(lista_star_wars)
print(lista_star_wars)
print(" ")

"""
b) Determinar si el personaje "Darth Maul" está cargado y en qué posición se
encuentra;
"""
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

posicion_1 = binaria(lista_star_wars, "Darth Maul")

print(f"Darth Maul está cargado en la qué posición {posicion_1}")
print(" ")

"""
c) Mostrar la información de los personajes que se encuentran antes y después
de "Hera Syndulla";
"""
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

posicion_2 = binaria(lista_star_wars, "Hera Syndulla")

print(f"""Los personajes que se encuentran antes y después de 
      Hera Syndulla son 
      {lista_star_wars[posicion_2-1]}, 
      {lista_star_wars[posicion_2+1]}""")
print(" ")

# d) Listar todos los personajes que comienzan con la letra L;
listaL = []

for personaje in lista_star_wars:
    
    if(personaje[0]=="L"):
        listaL.append(personaje)

print(listaL)