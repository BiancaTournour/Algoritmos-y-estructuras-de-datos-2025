from List_ import List

from superheroes_data import SuperheroesData

superheroes = SuperheroesData.get_superheroes()

#a) eliminar el nodo de linterna verde
def eliminar_personaje(lista, buscado):
    for personaje in lista:
        if personaje['alias'] == buscado:
            print('datos del personaje a eliminar:')
            print(personaje)
            lista.delete_value(buscado, 'alias')
            break

#b) mostrar año de aparicion
def aparicion(lista, buscado):
    def criterio(item):
        return item['alias']
    lista.add_criterion('alias', criterio)

    index = lista.search(buscado, 'alias')
    if index is not None:
        personaje = lista[index]
        print(f'el personaje {personaje['alias']} hizo su aparicion en el anio {personaje['first_appearance']}')
    else: print(f'personaje {personaje['alias']} no econtrado')

#c) cambiar la casa de un personaje
def cambiar_casa(lista, buscado, asignada):
    def criterio(item):
        return item['alias']
    lista.add_criterion('alias', criterio)

    index = lista.search(buscado, 'alias')
    if index is not None:
        personaje = lista[index]
        personaje['publisher'] = asignada
        print(f'la casa del personaje {personaje['alias']} fue cambiada')
        print(personaje)
    else: print(f'no se encontro al personaje {personaje['alias']} en la lista')

#d) personajes que en su bio muestran palabras especificas
def filtrar_por_bio(lista, palabras_buscadas):
    for personaje in lista:
        for palabra in palabras_buscadas:
         if palabra in personaje['short_bio']:
            print(f'-{personaje['alias']}')
            break

#e) mostrar nombre y casa de los aparecidos antes de cierto año
def antes_de(lista, anio):
    temp = List() #utilizo una lista temporal para imprimir luego los personajes de manera mas prolija
    for personaje in lista:
        if personaje['first_appearance'] < anio:
            temp.append(f'personaje: {personaje['alias']}, anio de aparicion: {personaje['first_appearance']}')  
    if temp:
        print(f'personajes aparecidos antes del anio {anio}')
        temp.show()   
    else: print(f'no se encontraron personajes aparecidos antes del anio {anio}')  

#f) mostrar casa a la que pertenece un personaje especifico
def casa_de_pertenencia(lista, buscado):
    encontrado = False
    for personaje in lista:
        if personaje['alias'] == buscado:
            encontrado = True
            print(f'el personaje {personaje['alias']} pertenece a la casa {personaje['publisher']}')
    if encontrado == False:
        print(f'el personaje {buscado} no fue encontrado en la lista')          

#g) mostrar toda la informacion de un personaje buscado
def info(lista, buscado):
    encontrado = False
    for personaje in lista:
        if personaje['alias'] == buscado:
            encontrado = True
            print(personaje)
    if encontrado == False:
        print(f'el personaje {buscado} no fue encontrado en la lista')  

#h) personajes con una inicial especifica
def inicial(lista, iniciales):
    for personaje in lista:
     for letra in iniciales:
         if personaje['alias'].startswith(letra):
            print(f'-{personaje['alias']}')
            break           

#i) superherores por casa de comic
def por_casas(lista):
    cont_marvel = 0
    cont_DC = 0
    otras = 0
    for personaje in lista:
        if personaje['publisher'] == 'Marvel':
            cont_marvel += 1
        elif personaje['publisher'] == 'DC':
            cont_DC += 1
        else: otras += 1

    print(f'hay {cont_marvel} personajes de la casa Marvel, {cont_DC} de la casa DC y {otras} de otras casas de comics')    


#ejecucion
#a)
eliminar_personaje(superheroes, 'Green Lantern')
print()
#b)
aparicion(superheroes, 'Wolverine')
print()
#c)
cambiar_casa(superheroes, 'Doctor Strange', 'Marvel')
print()
#d)
palabras = ['suit', 'armor']
print('personajes con la palabra traje/suit o armadura/armor en su bio:')
filtrar_por_bio(superheroes, palabras)
print()
#e)
antes_de(superheroes, 1963)
print()
#f)
casa_de_pertenencia(superheroes, 'Captain Marvel')
casa_de_pertenencia(superheroes, 'Wonder Woman')
print()
#g)
info(superheroes, 'Flash')
info(superheroes, 'Star-Lord')
print()
#h)
print('personajes con inicial b, m o s:')
iniciales = ['B', 'M', 'S']
inicial(superheroes, iniciales)
print()
#i)
por_casas(superheroes)

