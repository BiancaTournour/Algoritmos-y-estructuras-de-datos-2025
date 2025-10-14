from heap import HeapMax

heap_empresa = HeapMax()

# Lista original de personas y prioridades
personas = [
    ("Díaz Juan", 1),
    ("Pérez Ana", 1),
    ("López Mario", 1),
    ("Gómez Pablo", 2),
    ("Fernández Lucía", 2),
    ("Martínez Carla", 3)
]


# a) Cargar tres empleados
empleados = [("Díaz Juan", 1), ("Pérez Ana", 1), ("López Mario", 1)]
for nombre, prioridad in empleados:
    heap_empresa.arrive(nombre, prioridad)


# b) Imprimir el primer documento

prioridad, nombre = heap_empresa.attention()
print(f"Primer documento impreso: {nombre}")


# c) Cargar dos staff TI

staff_ti = [("Gómez Pablo", 2), ("Fernández Lucía", 2)]
for nombre, prioridad in staff_ti:
    heap_empresa.arrive(nombre, prioridad)


# d) Cargar un gerente

gerente = [("Martínez Carla", 3)]
for nombre, prioridad in gerente:
    heap_empresa.arrive(nombre, prioridad)


# e) Imprimir los dos primeros documentos

for _ in range(2):
    if heap_empresa.size() > 0:
        prioridad, nombre = heap_empresa.attention()
        print(f"Documento impreso: {nombre}")


# f) Cargar dos empleados y un gerente más

empleados_extra = [("Díaz Juan", 1), ("Pérez Ana", 1)]
gerente_extra = [("Martínez Carla", 3)]

for nombre, prioridad in empleados_extra + gerente_extra:
    heap_empresa.arrive(nombre, prioridad)


# g) Imprimir todos los documentos restantes

print("\nImprimiendo todos los documentos restantes:")
while heap_empresa.size() > 0:
    prioridad, nombre = heap_empresa.attention()
    print(f"Documento impreso: {nombre}")

