from List_ import List

from lista_starwars import starwars_data

jedis = starwars_data.get_jedis()

#a) listado ordenado por nombre y especie
def ordenar(lista):
    def criterio(item):
        return (item['name'], item['species'])
    lista.add_criterion(('name_species'), criterio)
    lista.sort_by_criterion('name_species')

#b) mostrar la info de personajes buscados
def info(lista, buscado):
    encontrado = False
    for personaje in lista:
        if personaje['name'] == buscado:
            encontrado = True
            print(personaje)
    if encontrado == False:
        print(f'el personaje {buscado} no fue encontrado en la lista')      

#c)mostrar los padawans de un personaje si tiene
def padawans(lista, buscado):
    for personaje in lista:
        if personaje['name'] == buscado:
         if personaje['padawans'] is not None:
            print(f'los padawans de {personaje['name']} son {personaje['padawans']}')
         else: print(f'el personaje {personaje['name']} no tiene padawans')

#d) mostrar jedis por especie
def por_especie(lista, especie):
    temp = List() #lista temporal para mostrar los personajes buscados
    for personaje in lista:
        if personaje['species'] == especie:
            temp.append(personaje['name'])

    if temp:
        print(f'personajes de especie {especie}:')
        temp.show()
    else: print(f'no hay personajes de la especie {especie} en la lista')    

#e) listar por inicial
def por_inicial(lista, inicial):
    temp = List()
    for personaje in lista:
        if personaje['name'].startswith(inicial):
            temp.append(personaje['name'])

    if temp:
        print(f'personaje con inicial {inicial}:')
        temp.show()
    else: print(f'no hay personajes con inicial {inicial} en la lista')                

#f) jedis que usaron mas de un color de sable
def jedis_sables(lista):
    temp = List()
    for personaje in lista:
        if personaje['lightsaber_colors'] is not None and len(personaje['lightsaber_colors']) > 1:
            temp.append(personaje['name'])

    if temp:
        print('personajes que usaron mas de un color de sable de luz:') 
        temp.show()
    else: print('ningun personaje de la lista utilizo mas de un color de sable de luz')       

#g) buscar sable por color
def sable_por_color(lista, colores):
    for personaje in lista:
        if personaje['lightsaber_colors'] is not None:
            for color in colores:
                if color in personaje['lightsaber_colors']:
                    print(personaje['name'])
                    break 


#ejecucion
#a)
ordenar(jedis)
#b)
info(jedis, 'Ahsoka Tano')
info(jedis, 'Kit Fisto')  
print()
#c)
padawans(jedis, 'Yoda')
padawans(jedis, 'Luke Skywalker')
print()
#d)
por_especie(jedis, 'Human')
print()
por_especie(jedis, "Twi'lek")
print()
#e)
por_inicial(jedis, 'A')
print()
#f)
jedis_sables(jedis)
print()
#g)
colores = ['Yellow', 'Violet']
print('personajes con sables de color amarillo o violeta:')
sable_por_color(jedis, colores)
print()
#h)
padawans(jedis, 'Qui-Gon Jinn')
padawans(jedis, 'Mace Windu')