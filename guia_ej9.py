from List_ import List
import random

lista_alumnos = List([
    {
        'nombre': 'Ana',
        'apellido': 'Gómez',
        'legajo': '1001'
    },

    {
        'nombre': 'Bruno',
        'apellido': 'Martínez',
        'legajo': '1002'
    },

    {
        'nombre': 'Carla',
        'apellido': 'López',
        'legajo': '1003'
    },

    {
        'nombre': 'Diego',
        'apellido': 'Fernández',
        'legajo': '1004'
    },

    {
        'nombre': 'Elena',
        'apellido': 'Pérez',
        'legajo': '1005'
    },

    {
        'nombre': 'Facundo',
        'apellido': 'Rodríguez',
        'legajo': '1006'
    },

    {
        'nombre': 'Gabriela',
        'apellido': 'Ramírez',
        'legajo': '1007'
    },

    {
        'nombre': 'Hugo',
        'apellido': 'Sánchez',
        'legajo': '1008'
    },

    {
        'nombre': 'Ivana',
        'apellido': 'Silva',
        'legajo': '1009'
    },

    {
        'nombre': 'Joaquín',
        'apellido': 'Molina',
        'legajo': '1010'
    },

    {
        'nombre': 'Karen',
        'apellido': 'Torres',
        'legajo': '1011'
    },

    {
        'nombre': 'Lucas',
        'apellido': 'Ruiz',
        'legajo': '1012'
    },

    {
        'nombre': 'Marina',
        'apellido': 'Vega',
        'legajo': '1013'
    },

    {
        'nombre': 'Nicolás',
        'apellido': 'Cruz',
        'legajo': '1014'
    },

    {
        'nombre': 'Olivia',
        'apellido': 'Díaz',
        'legajo': '1015'
    },

    {
        'nombre': 'Pablo',
        'apellido': 'Ramos',
        'legajo': '1016'
    },

    {
        'nombre': 'Quimey',
        'apellido': 'García',
        'legajo': '1017'
    },

    {
        'nombre': 'Rocío',
        'apellido': 'Navarro',
        'legajo': '1018'
    },

    {
        'nombre': 'Santiago',
        'apellido': 'Ibarra',
        'legajo': '1019'
    },

    {
        'nombre': 'Tamara',
        'apellido': 'Castro',
        'legajo': '1020'
    }
])

notas_alumnos = List()

from datetime import datetime, timedelta

materias = ['Algoritmos y estructuras de datos', 'Programacion orientada a objetos', 'Calculo II', 'Ingenieria de Software I', 'Matematica discreta']
fechas_base = datetime(2025, 6, 1)

#agregar 3 notas de examenes a cada alumno
for alumno in lista_alumnos:
    legajo = alumno['legajo']
    notas = []
    for i in range(3):
        materia = random.choice(materias)
        nota = random.randint(1, 10)
        fecha = (fechas_base + timedelta(days=random.randint(0, 20))).strftime('%d/%m/%y')
        notas.append([legajo, materia, nota, fecha])
    alumno['notas'] = notas
    notas_alumnos.append(notas)

#ordenar por apellido
def ordenar_por_apellido(item): #crear criterio
    return (item['apellido'])

lista_alumnos.add_criterion('apellido', ordenar_por_apellido) #agregar criterio

lista_alumnos.sort_by_criterion('apellido') #ordenar por criterio

#alumnos que no desaprobaron ningun parcial
def alumnos_sin_desaprobados(lista):
    temp = List()
    for alumno in lista:
      notas = alumno['notas']
      if all(nota[2] > 5 for nota in notas):
        temp.append({alumno['nombre'], alumno['apellido']})
    if temp:
        print('alumnos que no desaprobaron ningun examen:')
        temp.show()
    else: print('todos los alumnos desaprobaron al menos un examen')

#agregar promedios
def promedio(lista):
   for alumno in lista:
        notas = alumno['notas']
        prom = sum(nota[2] for nota in notas) / len(notas)
        alumno['promedio'] = prom 

#promedios mayores a 8,89
def promedios_altos(lista):
    temp = List()
    for alumno in lista:
        if alumno['promedio'] > 8.89:
            temp.append(f'alumno: {alumno['nombre']} {alumno['apellido']}, promedio: {alumno['promedio']}')
    if temp:
        print('alumnos con promedio mayor a 8,89:')
        temp.show()
    else: print('no hay alumnos con promedio mayor a 8,89')        

#apellidos que comienzan con L
def apellidos_con_L(lista):
    temp = List()
    for alumno in lista:
        if alumno['apellido'].startswith('L'):
          temp.append(alumno)  
    if temp:
        print('alumnos cuyo apellido comienza con L:')
        temp.show()
    else: print('no hay alumnos cuyo apellido comienze con L')

#lista promedios
def promedios(lista):
    temp = List()
    for alumno in lista:
        temp.append(f'alumno:{alumno['apellido']} {alumno['nombre']}, promedio: {[alumno['promedio']]}')
    temp.show()   

#alumnos que rindieron algortimos y estructuras de datos
def AyEdD(lista):
    temp = List()
    for alumno in lista:
        for nota in alumno['notas']:
            if nota[1] == 'Algoritmos y estructuras de datos':
                temp.append(f"{alumno['apellido']} {alumno['nombre']} - Nota: {nota[2]}")
                break  # si ya encontramos que rindió, no hace falta seguir revisando más notas
    if temp:
        print('Alumnos que rindieron Algoritmos y estructuras de datos:')
        temp.show()
    else:
        print('Ningún alumno rindió Algoritmos y estructuras de datos')  

#parciales aprobados de un alumno indicado por el usuario
def alumno_indicado(lista):
    print('Ingrese el nombre del alumno que desea buscar:')
    apellido_buscado = input('Apellido: ').strip().capitalize()#strip quita los espacios en blanco y capitalize hace la primer letra mayuscula
    nombre_buscado = input('Nombre: ').strip().capitalize()

    # Definir criterio de búsqueda por (apellido, nombre)
    def criterio_apellido_nombre(item):
        return (item['apellido'], item['nombre'])

    lista.add_criterion('apellido_nombre', criterio_apellido_nombre)

    # Usar búsqueda binaria con el criterio
    indice = lista.search((apellido_buscado, nombre_buscado), 'apellido_nombre')

    if indice is not None:
        alumno = lista.get_element_by_index(indice)
        print(f"\nAlumno encontrado: {alumno['apellido']} {alumno['nombre']}")
        print('Legajo:', alumno['legajo'])
        print('Notas:')
        
        total = len(alumno['notas'])
        aprobados = sum(1 for nota in alumno['notas'] if nota[2] > 5)

        for nota in alumno['notas']:
            print(f"  Materia: {nota[1]}, Nota: {nota[2]}, Fecha: {nota[3]}")

        porcentaje = (aprobados / total) * 100
        print(f"\nPorcentaje de parciales aprobados: {porcentaje:.2f}%")
    else:
        print('No se encontró un alumno con ese nombre y apellido')


#ejecucion 
promedio(lista_alumnos)
alumnos_sin_desaprobados(lista_alumnos) 
print()
promedios_altos(lista_alumnos)  
print()
apellidos_con_L(lista_alumnos)
print()
promedios(lista_alumnos)
print()
AyEdD(lista_alumnos) 
print()
alumno_indicado(lista_alumnos)   