from List_ import List
from Queue import Queue

from superheroes_data import SuperheroesData

superheroes = SuperheroesData.get_superheroes()

#ordenar la lista por nombre de los personajes
def ordenar_por_nombre(lista):
    def ordenar(item):
        return item['name']
    lista.add_criterion('name', ordenar)
    lista.sort_by_criterion('name')

#determinar posicion de personajes
def determinar_posicion(lista: List, nombre: str) -> int:
    posicion = lista.search(nombre, 'name')
    if posicion is not None:
        print(nombre, 'posicion:', posicion)
    else:
        print(f'El personaje "{nombre}" no está en la lista')

#listar villanos (y guardarlos en una cola)
villanos = Queue()
def mostrar_villanos(lista):
    temp = List()

    for personaje in lista:
        if personaje['is_villain'] == True:
            villanos.arrive(personaje)
            temp.append(f'nombre: {personaje['name']} / alias: {personaje['alias']} / nombre real: {personaje['real_name']} / año de aparicion: {personaje['first_appearance']} / biografia corta: {personaje['short_bio']}')

    if villanos:
        print('villanos:')
        temp.show() 
    else: print('no hay villanos en esta lista')        

#usando la cola mostrar aquellos villanos que aparecieron antes de 1980
def antes_de(anio: int, villanos):
    aux = Queue()

    while villanos:
        personaje = villanos.attention()
        aux.arrive(personaje) #para no perder los datos de la cola y restaurarlos posteriormente

        if personaje['first_appearance'] < anio:
            print(personaje['name'])

    while aux:
        villanos.arrive(aux.attention())  

#listar superheroes que empiezan con Bl, G, My y W
def listar_por_inicial(lista):
    inicial_buscada = ('Bl', 'G', 'My', 'W')
    temp = List()

    for personaje in lista:
        if personaje['name'].startswith(inicial_buscada):
            temp.append(personaje)

    if temp:
        print('personajes con inicial Bl, G, My o W:')
        for personajes in temp:
            print(f'nombre: {personajes['name']}, alias: {personajes['alias']}, nombre real: {personajes['real_name']}') 
    else: print('no hay personajes con las iniciales Bl, G, My o W')      
                           
#ordenar por nombre real
def ordenar_por_nombre_real(lista):
     def ordenar(item):
        return item['real_name']
     lista.add_criterion('real_name', ordenar)
     lista.sort_by_criterion('real_name')   

#listado ordenado por fecha de aparicion de cada superheroe
def ordenar_por_fecha_de_aparicion(lista):
   def ordenar(item):
       return item['first_appearance']
   lista.add_criterion('first_appearance', ordenar)
   lista.sort_by_criterion('first_appearance')

#modificar nombre de Ant man
def modificar_nombre(lista):
 lista.add_criterion('name', lambda x: x['name'].lower())

 index = lista.search('ant man', 'name')
 if index is not None:
    print('nombre:')
    print(lista[index]['name'])  # Ant man
    print('cambio a:')
    lista[index]['name'] = 'Scott Lang'
    print(lista[index]['name'])  # Scott Lang
 else:
    print('El superhéroe no está en la lista')

#Mostrar los personajes que en su biografia incluyan la palabra time-traveling o suit
def mostrar_por_bio(lista):
 buscado = ('time-traveling', 'suit')
 temp = List()

 for personaje in lista:
     if any(palabra in personaje['short_bio'].lower() for palabra in buscado):
         temp.append(f"personaje: {personaje['name']}, biografia: {personaje['short_bio']}") 

 if temp:
     print('Personajes con "time-traveling" o "suit" en su biografía:')
     temp.show()    
 else:
    print('No hay personajes con "time-traveling" o "suit" en su biografía')

#eliminar personaje y mostrar info
def eliminar_personaje(buscado, lista):
    for personaje in lista:
        if personaje['name'] == buscado:
            print('datos del personaje a eliminar:')
            print(personaje)
            lista.delete_value(buscado, 'name')
            break
            
#ejecucion

#ordenamiento por nombre
ordenar_por_nombre(superheroes)

determinar_posicion(superheroes, 'The Thing')
determinar_posicion(superheroes, 'Rocket Raccoon')
print()
mostrar_villanos(superheroes)
print()
print('villanos que aparecieron antes de 1980:')
antes_de(1980, villanos)
print()

#ordenamiento por nombre real
ordenar_por_nombre_real(superheroes)
#ordenamiento por fecha de aparicion
ordenar_por_fecha_de_aparicion(superheroes)

listar_por_inicial(superheroes)
print()
modificar_nombre(superheroes)
print()
mostrar_por_bio(superheroes)
print()
eliminar_personaje('Electro', superheroes)
print()
eliminar_personaje('Baron Zemo', superheroes)