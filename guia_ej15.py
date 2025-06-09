from List_ import List

lista_entrenadores = List([
    {
        'entrenador': 'Ash Ketchum',
        'torneos ganados': 3,
        'batallas perdidas': 20,
        'batallas ganadas': 100,
        'pokemons': List([
            {'nombre': 'Pikachu', 'nivel': 50, 'tipo': 'Eléctrico', 'subtipo': None},
            {'nombre': 'Charizard', 'nivel': 70, 'tipo': 'Fuego', 'subtipo': 'Volador'}
        ])
    },
    {
        'entrenador': 'Misty',
        'torneos ganados': 1,
        'batallas perdidas': 12,
        'batallas ganadas': 55,
        'pokemons': List([
            {'nombre': 'Staryu', 'nivel': 35, 'tipo': 'Agua', 'subtipo': None},
            {'nombre': 'Psyduck', 'nivel': 30, 'tipo': 'Agua', 'subtipo': 'Psíquico'}
        ])
    },
    {
        'entrenador': 'Brock',
        'torneos ganados': 2,
        'batallas perdidas': 15,
        'batallas ganadas': 60,
        'pokemons': List([
            {'nombre': 'Onix', 'nivel': 45, 'tipo': 'Roca', 'subtipo': 'Tierra'},
            {'nombre': 'Geodude', 'nivel': 40, 'tipo': 'Roca', 'subtipo': 'Tierra'}
        ])
    },
    {
        'entrenador': 'Gary Oak',
        'torneos ganados': 4,
        'batallas perdidas': 10,
        'batallas ganadas': 80,
        'pokemons': List([
            {'nombre': 'Blastoise', 'nivel': 75, 'tipo': 'Agua', 'subtipo': None},
            {'nombre': 'Arcanine', 'nivel': 68, 'tipo': 'Fuego', 'subtipo': None}
        ])
    },
    {
        'entrenador': 'Erika',
        'torneos ganados': 3,
        'batallas perdidas': 8,
        'batallas ganadas': 40,
        'pokemons': List([
            {'nombre': 'Vileplume', 'nivel': 55, 'tipo': 'Planta', 'subtipo': 'Veneno'},
            {'nombre': 'Tangela', 'nivel': 50, 'tipo': 'Planta', 'subtipo': None}
        ])
    },
    {
        'entrenador': 'Lt. Surge',
        'torneos ganados': 2,
        'batallas perdidas': 6,
        'batallas ganadas': 45,
        'pokemons': List([
            {'nombre': 'Raichu', 'nivel': 60, 'tipo': 'Eléctrico', 'subtipo': None},
            {'nombre': 'Electabuzz', 'nivel': 58, 'tipo': 'Eléctrico', 'subtipo': None}
        ])
    },
    {
        'entrenador': 'Sabrina',
        'torneos ganados': 5,
        'batallas perdidas': 5,
        'batallas ganadas': 90,
        'pokemons': List([
            {'nombre': 'Alakazam', 'nivel': 70, 'tipo': 'Psíquico', 'subtipo': None},
            {'nombre': 'Mr. Mime', 'nivel': 60, 'tipo': 'Psíquico', 'subtipo': 'Hada'}
        ])
    },
    {
        'entrenador': 'Koga',
        'torneos ganados': 2,
        'batallas perdidas': 9,
        'batallas ganadas': 52,
        'pokemons': List([
            {'nombre': 'Weezing', 'nivel': 55, 'tipo': 'Veneno', 'subtipo': None},
            {'nombre': 'Muk', 'nivel': 53, 'tipo': 'Veneno', 'subtipo': None}
        ])
    },
    {
        'entrenador': 'Giovanni',
        'torneos ganados': 6,
        'batallas perdidas': 7,
        'batallas ganadas': 110,
        'pokemons': List([
            {'nombre': 'Rhydon', 'nivel': 75, 'tipo': 'Tierra', 'subtipo': 'Roca'},
            {'nombre': 'Nidoking', 'nivel': 72, 'tipo': 'Veneno', 'subtipo': 'Tierra'}
        ])
    },
    {
        'entrenador': 'Cynthia',
        'torneos ganados': 8,
        'batallas perdidas': 2,
        'batallas ganadas': 130,
        'pokemons': List([
            {'nombre': 'Garchomp', 'nivel': 85, 'tipo': 'Dragón', 'subtipo': 'Tierra'},
            {'nombre': 'Lucario', 'nivel': 80, 'tipo': 'Lucha', 'subtipo': 'Acero'}
        ])
    }
])

#obtener pokemones de un determinado entrenador
def entrenador_buscado(lista):
    entrenador = input('Ingrese el nombre del entrenador que busca: ')

    # Agregamos el criterio para buscar por entrenador
    def criterio_entrenador(item):
        return item['entrenador'].lower()

    lista.add_criterion('entrenador', criterio_entrenador)

    index = lista.search(entrenador.lower(), 'entrenador')
    if index is not None:
        entrenador_info = lista.get_element_by_index(index)
        cantidad = len(entrenador_info['pokemons'])
        print(f"El entrenador {entrenador_info['entrenador']} tiene {cantidad} Pokémon(s)")
    else:
        print('El entrenador indicado no se encuentra en la lista')

#entrenadores con mas de 3 torneos ganados
def entrenadores_torneos(lista):
    temp = List()
    for entrenador in lista:
        if entrenador['torneos ganados'] >= 3:
            temp.append(f'entrenador: {entrenador['entrenador']}, torneos ganados: {entrenador['torneos ganados']}')
    if temp:
        print('entrenadores con 3 o mas torneos ganados:') 
        temp.show()
    else: print('no hay entrenadores con 3 o mas torneos ganados')       

#pokemon de mayor nivel del entrenador con mas torneos ganados
def mejor_entrenador_pokemon(lista):
    max_torneos = 0
    mejor_entrenador = None

    for entrenador in lista: #mejor entrenador en la lista
        if entrenador['torneos ganados'] > max_torneos:
            max_torneos = entrenador['torneos ganados']
            mejor_entrenador = entrenador

    max_nivel = 0
    max_pokemon = None
    for pokemon in mejor_entrenador['pokemons']: #mejor pokemon del entrenador
        if pokemon['nivel'] > max_nivel:
            max_nivel = pokemon['nivel']
            max_pokemon = pokemon['nombre']

    print(f"El entrenador con más torneos ganados es {mejor_entrenador['entrenador']}, y su Pokémon de mayor nivel es {max_pokemon}")

#mostrar todos los datos de un entrenador y sus pokemons    
def entrenador_indicado(lista):
    entrenador = input('Ingrese el nombre del entrenador del que desea saber los datos: ')

    # Agregamos el criterio para buscar por entrenador
    def criterio_entrenador(item):
        return item['entrenador'].lower()

    lista.add_criterion('entrenador', criterio_entrenador)

    index = lista.search(entrenador.lower(), 'entrenador')
    if index is not None:
        entrenador_info = lista.get_element_by_index(index)
        print(f"entrenador: {entrenador_info['entrenador']}, torneos ganados: {entrenador_info['torneos ganados']}, batallas ganadas: {entrenador_info['batallas ganadas']}, batallas perdidas: {entrenador_info['batallas perdidas']}, pokemons: {entrenador_info['pokemons']}")
    else:
        print('El entrenador indicado no se encuentra en la lista')

        

#ejecucion
entrenador_buscado(lista_entrenadores)    
print()
entrenadores_torneos(lista_entrenadores)
print()
mejor_entrenador_pokemon(lista_entrenadores)
print()
entrenador_indicado(lista_entrenadores)