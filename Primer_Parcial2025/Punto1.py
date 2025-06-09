superheroes = ['Capitan America', 'Iron Man', 'Spider Man', 'Hulk', 'Batman', 'Superman', 'Thor', 'Black Widow', 'Flash', 'Wonder Woman', 'Green Lantern', 'Hawkeye', 'Doctor Strange', 'Aquaman', 'Wolverine']

#funcion para buscar recursivamente
def buscar(personaje, lista):
    if not lista:
        print(f'{personaje} no encontrado')
    elif lista[0] == personaje:
        print(f'{personaje} encontrado')
    else:
        buscar(personaje, lista[1:])

#funcion recursiva para listar
def listar_superheroes(lista):
    if not lista:
        return
    print(lista[0])
    listar_superheroes(lista[1:])

#ejecucion
buscar('Capitan America', superheroes)
print()
print('superheroes:')
listar_superheroes(superheroes)        