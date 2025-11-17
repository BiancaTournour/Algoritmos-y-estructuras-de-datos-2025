from graph import Graph

# Crear grafo no dirigido
grafo = Graph(is_directed=False)

# Insertar vértices (personajes)
grafo.insert_vertex("Luke Skywalker", {"episodios": [4,5,6,7,8,9]})
grafo.insert_vertex("Darth Vader", {"episodios": [1,2,3,4,5,6,9]})
grafo.insert_vertex("Yoda", {"episodios": [1,2,3,5,6,8]})
grafo.insert_vertex("Boba Fett", {"episodios": [2,5,6]})
grafo.insert_vertex("C-3PO", {"episodios": [1,2,3,4,5,6,7,8,9]})
grafo.insert_vertex("Leia", {"episodios": [3,4,5,6,7,8,9]})
grafo.insert_vertex("Rey", {"episodios": [7,8,9]})
grafo.insert_vertex("Kylo Ren", {"episodios": [7,8,9]})
grafo.insert_vertex("Chewbacca", {"episodios": [3,4,5,6,7,8,9]})
grafo.insert_vertex("Han Solo", {"episodios": [4,5,6,7,9]})
grafo.insert_vertex("R2-D2", {"episodios": [1,2,3,4,5,6,7,8,9]})
grafo.insert_vertex("BB-8", {"episodios": [7,8,9]})


# Insertar aristas (origen, destino, peso = episodios compartidos)
# Luke Skywalker con otros
grafo.insert_edge("Luke Skywalker", "Darth Vader", 3)
grafo.insert_edge("Luke Skywalker", "Yoda", 5)
grafo.insert_edge("Luke Skywalker", "Boba Fett", 2)
grafo.insert_edge("Luke Skywalker", "C-3PO", 6)
grafo.insert_edge("Luke Skywalker", "Leia", 6)
grafo.insert_edge("Luke Skywalker", "Rey", 3)
grafo.insert_edge("Luke Skywalker", "Kylo Ren", 3)
grafo.insert_edge("Luke Skywalker", "Chewbacca", 6)
grafo.insert_edge("Luke Skywalker", "Han Solo", 4)
grafo.insert_edge("Luke Skywalker", "R2-D2", 6)
grafo.insert_edge("Luke Skywalker", "BB-8", 3)

# Darth Vader con otros
grafo.insert_edge("Darth Vader", "Yoda", 2)
grafo.insert_edge("Darth Vader", "Boba Fett", 2)
grafo.insert_edge("Darth Vader", "C-3PO", 4)
grafo.insert_edge("Darth Vader", "Leia", 3)
grafo.insert_edge("Darth Vader", "Chewbacca", 4)
grafo.insert_edge("Darth Vader", "Han Solo", 3)
grafo.insert_edge("Darth Vader", "R2-D2", 4)

# Yoda con otros
grafo.insert_edge("Yoda", "Boba Fett", 2)
grafo.insert_edge("Yoda", "C-3PO", 8)
grafo.insert_edge("Yoda", "Leia", 5)
grafo.insert_edge("Yoda", "Rey", 3)
grafo.insert_edge("Yoda", "Kylo Ren", 3)
grafo.insert_edge("Yoda", "Chewbacca", 6)
grafo.insert_edge("Yoda", "Han Solo", 3)
grafo.insert_edge("Yoda", "R2-D2", 8)
grafo.insert_edge("Yoda", "BB-8", 3)

# Boba Fett con otros
grafo.insert_edge("Boba Fett", "C-3PO", 2)
grafo.insert_edge("Boba Fett", "Leia", 2)
grafo.insert_edge("Boba Fett", "Chewbacca", 2)
grafo.insert_edge("Boba Fett", "Han Solo", 2)
grafo.insert_edge("Boba Fett", "R2-D2", 2)

# C-3PO con otros
grafo.insert_edge("C-3PO", "Leia", 6)
grafo.insert_edge("C-3PO", "Rey", 3)
grafo.insert_edge("C-3PO", "Kylo Ren", 3)
grafo.insert_edge("C-3PO", "Chewbacca", 7)
grafo.insert_edge("C-3PO", "Han Solo", 4)
grafo.insert_edge("C-3PO", "R2-D2", 9)
grafo.insert_edge("C-3PO", "BB-8", 3)

# Leia con otros
grafo.insert_edge("Leia", "Rey", 3)
grafo.insert_edge("Leia", "Kylo Ren", 3)
grafo.insert_edge("Leia", "Chewbacca", 6)
grafo.insert_edge("Leia", "Han Solo", 4)
grafo.insert_edge("Leia", "R2-D2", 6)
grafo.insert_edge("Leia", "BB-8", 3)

# Rey con otros
grafo.insert_edge("Rey", "Kylo Ren", 3)
grafo.insert_edge("Rey", "Chewbacca", 3)
grafo.insert_edge("Rey", "R2-D2", 3)
grafo.insert_edge("Rey", "BB-8", 3)

# Kylo Ren con otros
grafo.insert_edge("Kylo Ren", "Chewbacca", 3)
grafo.insert_edge("Kylo Ren", "R2-D2", 3)
grafo.insert_edge("Kylo Ren", "BB-8", 3)

# Chewbacca con otros
grafo.insert_edge("Chewbacca", "Han Solo", 4)
grafo.insert_edge("Chewbacca", "R2-D2", 7)
grafo.insert_edge("Chewbacca", "BB-8", 3)

# Han Solo con otros
grafo.insert_edge("Han Solo", "R2-D2", 4)

# R2-D2 con otros
grafo.insert_edge("R2-D2", "BB-8", 3)

# hallar el arbol de expansion minima desde C_3PO, Yoda y Leia
personajes = ["C-3PO", "Yoda", "Leia"]

for personaje in personajes:
    print(f"arbol de expansion minima desde {personaje}")
    arbol = grafo.kruskal(personaje)
    print(arbol)
    print()

# hallar el numero maximo de episodios que comparten dos personajes e indicar todos los pares de personajes que coinciden con dicho número
def max_episodios(grafo):
    max_peso = -1
    parejas = []

    for vertex in grafo:
        nodo = vertex
        for edge in nodo.edges:
            destino = edge.value
            peso = edge.weight

            # Evitar duplicados (A-B y B-A)
            if nodo.value < destino:
                if peso > max_peso:
                    max_peso = peso
                    parejas = [(nodo.value, destino)]
                elif peso == max_peso:
                    parejas.append((nodo.value, destino))

    print(f"El máximo número de episodios compartidos es: {max_peso}")
    print("Pares que coinciden con ese número:")
    for p in parejas:
        print(f"{p[0]} y {p[1]}")

max_episodios(grafo)
print()

# calcule el camino mas corto desde un personaje a otro
def camino_mas_corto(grafo, origen, destino):
    stack = grafo.dijkstra(origen)

    while stack:
        dato = stack.pop()  
        if dato[0] == destino:
            print(f"El camino más corto a {destino} desde {origen} es de peso total {dato[1]}")
            break

camino_mas_corto(grafo, "C-3PO", "R2-D2")
print()
camino_mas_corto(grafo, "Yoda", "Darth Vader")
print()

# indicar personajes que aparecieron en los 9 episodios de la saga
def personajes_todos_episodios(grafo):
    personajes = []
    for personaje in grafo:
        if personaje.other_values and "episodios" in personaje.other_values:
            if len(personaje.other_values["episodios"]) == 9:
                personajes.append(personaje.value)
    print("Personajes que aparecen en todos los episodios de la saga:")
    print(personajes)

personajes_todos_episodios(grafo)