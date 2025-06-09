from List_ import List
from datetime import date, datetime

lista_proyecto = List([{
        'actividad': 'Análisis de requerimientos',
        'costo': 1500,
        'tiempo de ejecución (en días)': 5,
        'fecha de inicio': date(2025, 6, 10),
        'fecha de fin estimada': date(2025, 6, 14),
        'fecha de fin efectiva': date(2025, 6, 13),
        'persona a cargo': 'Laura Gómez'
    },

    {
        'actividad': 'Diseño del sistema',
        'costo': 2000,
        'tiempo de ejecución (en días)': 6,
        'fecha de inicio': date(2025, 6, 15),
        'fecha de fin estimada': date(2025, 6, 20),
        'fecha de fin efectiva': date(2025, 6, 22),
        'persona a cargo': 'Carlos Díaz'
    },

    {
        'actividad': 'Implementación del backend',
        'costo': 3500,
        'tiempo de ejecución (en días)': 10,
        'fecha de inicio': date(2025, 6, 23),
        'fecha de fin estimada': date(2025, 7, 4),
        'fecha de fin efectiva': date(2025, 7, 3),
        'persona a cargo': 'Mariana Torres'
    },

    {
        'actividad': 'Implementación del frontend',
        'costo': 3000,
        'tiempo de ejecución (en días)': 8,
        'fecha de inicio': date(2025, 7, 1),
        'fecha de fin estimada': date(2025, 7, 10),
        'fecha de fin efectiva': date(2025, 7, 12),
        'persona a cargo': 'Diego Ramírez'
    },

    {
        'actividad': 'Pruebas y validación',
        'costo': 1800,
        'tiempo de ejecución (en días)': 5,
        'fecha de inicio': date(2025, 7, 11),
        'fecha de fin estimada': date(2025, 7, 15),
        'fecha de fin efectiva': date(2025, 7, 15),
        'persona a cargo': 'Natalia Suárez'
    },

    {
        'actividad': 'Documentación técnica',
        'costo': 1200,
        'tiempo de ejecución (en días)': 4,
        'fecha de inicio': date(2025, 7, 16),
        'fecha de fin estimada': date(2025, 7, 19),
        'fecha de fin efectiva': date(2025, 7, 18),
        'persona a cargo': 'Federico Ponce'
    },

    {
        'actividad': 'Revisión de código',
        'costo': 1000,
        'tiempo de ejecución (en días)': 3,
        'fecha de inicio': date(2025, 7, 20),
        'fecha de fin estimada': date(2025, 7, 22),
        'fecha de fin efectiva': date(2025, 7, 21),
        'persona a cargo': 'Lucía Fernández'
    },

    {
        'actividad': 'Despliegue en entorno de pruebas',
        'costo': 800,
        'tiempo de ejecución (en días)': 2,
        'fecha de inicio': date(2025, 7, 23),
        'fecha de fin estimada': date(2025, 7, 24),
        'fecha de fin efectiva': date(2025, 7, 24),
        'persona a cargo': 'Gabriel Vázquez'
    },

    {
        'actividad': 'Capacitación al usuario',
        'costo': 1400,
        'tiempo de ejecución (en días)': 4,
        'fecha de inicio': date(2025, 7, 25),
        'fecha de fin estimada': date(2025, 7, 28),
        'fecha de fin efectiva': date(2025, 7, 28),
        'persona a cargo': 'Ana Herrera'
    },

    {
        'actividad': 'Despliegue final en producción',
        'costo': 1600,
        'tiempo de ejecución (en días)': 2,
        'fecha de inicio': date(2025, 7, 29),
        'fecha de fin estimada': date(2025, 7, 30),
        'fecha de fin efectiva': date(2025, 7, 30),
        'persona a cargo': 'Sergio Molina'
    }])

#tiempo promedio de las tareas
def prom(lista):
    dias_totales = 0
    for tiempos in lista:
        dias_totales = dias_totales + tiempos['tiempo de ejecución (en días)']
    promedio = dias_totales / (len(lista))
    print(f'el promedio de dias que tardó en hacerse cada actividad es de {promedio} dias')

#costo total del proyecto
def costo_total(lista):
    costo = 0
    for costos in lista:
        costo = costo + costos['costo']
    print(f'el costo total del proyecto fue de ${costo:,}')    

#Actividades realizadas por una determinada persona
def persona_buscada(lista):
    persona = input('Ingrese el nombre y apellido de la persona que busca: ')

    # Agregamos el criterio para buscar por persona
    def criterio_persona(item):
        return item['persona a cargo'].lower()

    lista.add_criterion('persona a cargo', criterio_persona)

    index = lista.search(persona.lower(), 'persona a cargo')
    if index is not None:
        actividad = lista.get_element_by_index(index)
        print(f"{persona} está a cargo de la actividad: {actividad['actividad']}")
    else:
        print(f"{persona} no está asignado/a a ninguna actividad")

#tareas a realizar entre dos fechas dadas
def tareas_entre_fechas(lista):
    print('Ingrese entre qué fechas desea ver las tareas realizadas (formato: AAAA-MM-DD):')
    fecha_1 = datetime.strptime(input('Desde: '), '%Y-%m-%d').date()
    fecha_2 = datetime.strptime(input('Hasta: '), '%Y-%m-%d').date()

    temp = List()

    for tarea in lista:
        fecha_fin = tarea['fecha de fin efectiva']
        if fecha_1 <= fecha_fin <= fecha_2:
            temp.append(f"Fecha: {fecha_fin}, actividad terminada: {tarea['actividad']}")

    if temp:
        temp.show()
    else:
        print('No hay actividades realizadas entre esas fechas')      
 
#tareas en tiempo y fuera de tiempo
def tareas_tiempo(lista):
    en_tiempo = List()
    fuera_de_tiempo = List()

    for tareas in lista:
        if tareas['fecha de fin estimada'] < tareas['fecha de fin efectiva']:
            fuera_de_tiempo.append(tareas['actividad'])
        else: en_tiempo.append(tareas['actividad'])

    print('tareas realizada en tiempo:')
    en_tiempo.show()
    print()
    print('tareas realizadas fuera de tiempo:')
    fuera_de_tiempo.show()    

#ejecucion
prom(lista_proyecto) 
print()
costo_total(lista_proyecto) 
print()
persona_buscada(lista_proyecto)  
print()
tareas_entre_fechas(lista_proyecto)
print()
tareas_tiempo(lista_proyecto)