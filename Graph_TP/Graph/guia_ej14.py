from graph import Graph

grafo = Graph(is_directed=False)

# a) habitaciones
grafo.insert_vertex("Cocina")
grafo.insert_vertex("Comedor")
grafo.insert_vertex("Cochera")
grafo.insert_vertex("Quincho")
grafo.insert_vertex("Baño 1")
grafo.insert_vertex("Baño 2")
grafo.insert_vertex("Habitacion 1")
grafo.insert_vertex("Habitacion 2")
grafo.insert_vertex("Sala de estar")
grafo.insert_vertex("Terraza")
grafo.insert_vertex("Patio")

# b) cargar conexiones (aristas)
grafo.insert_edge("Cocina", "Comedor", 3)
grafo.insert_edge("Cocina", "Patio", 5)
grafo.insert_edge("Cocina", "Quincho", 5)

grafo.insert_edge("Comedor", "Sala de estar", 4)
grafo.insert_edge("Comedor", "Terraza", 5)

grafo.insert_edge("Cochera", "Patio", 4)
grafo.insert_edge("Cochera", "Cocina", 3)
grafo.insert_edge("Cochera", "Quincho", 5)

grafo.insert_edge("Quincho", "Patio", 3)
grafo.insert_edge("Quincho", "Comedor", 4)

grafo.insert_edge("Baño 1", "Habitacion 1", 2)
grafo.insert_edge("Baño 1", "Habitacion 2", 3)
grafo.insert_edge("Baño 1", "Sala de estar", 5)

grafo.insert_edge("Baño 2", "Habitacion 2", 2)
grafo.insert_edge("Baño 2", "Sala de estar", 4)

grafo.insert_edge("Habitacion 1", "Habitacion 2", 3)
grafo.insert_edge("Habitacion 1", "Sala de estar", 5)

grafo.insert_edge("Habitacion 2", "Sala de estar", 4)

grafo.insert_edge("Terraza", "Patio", 3)

# c) arbol de expansion minima
# Obtenemos el árbol desde Kruskal
arbol = grafo.kruskal("Cocina")  

# Inicializamos contador
total_metros = 0

aristas = arbol.split(';')
for a in aristas:
    # Cada arista tiene formato "origen-destino-peso"
    partes = a.split('-')
    if len(partes) == 3:
        peso = int(partes[2])
        total_metros += peso

print("Metros totales para el árbol de expansión mínima:", total_metros)

# d) camino mas corto entre habitacion 1 y sala de estar
def camino_mas_corto(grafo, origen, destino):
    stack = grafo.dijkstra(origen)

    while stack:
        dato = stack.pop()
        if dato[0] == destino:
            print(f"El camino mas corto desde {origen} hasta {destino} es de {dato[1]} metros")
            break


camino_mas_corto(grafo, "Habitacion 1", "Sala de estar")