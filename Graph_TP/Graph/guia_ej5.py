from graph import Graph

grafo = Graph(is_directed = False)

#a) cargar en los nodos del grafo los sistemas operativos y dispositivos de la red
grafo.append(Graph._Graph__nodeVertex("Red Hat", "notebook"))
grafo.append(Graph._Graph__nodeVertex("Debian", "notebook"))
grafo.append(Graph._Graph__nodeVertex("Arch", "notebook"))
grafo.append(Graph._Graph__nodeVertex("Manjaro", "pc"))
grafo.append(Graph._Graph__nodeVertex("Fedora", "pc"))
grafo.append(Graph._Graph__nodeVertex("Ubuntu", "pc"))
grafo.append(Graph._Graph__nodeVertex("Mint", "pc"))
grafo.append(Graph._Graph__nodeVertex("Guaraní", "servidor"))
grafo.append(Graph._Graph__nodeVertex("MongoDB", "servidor"))
grafo.append(Graph._Graph__nodeVertex("Router 1", "router"))
grafo.append(Graph._Graph__nodeVertex("Router 2", "router"))
grafo.append(Graph._Graph__nodeVertex("Router 3", "router"))
grafo.append(Graph._Graph__nodeVertex("Switch 1", "switch"))
grafo.append(Graph._Graph__nodeVertex("Switch 2", "switch"))
grafo.append(Graph._Graph__nodeVertex("Impresora", "impresora"))
grafo.append(Graph._Graph__nodeVertex("Parrot", "pc"))

#conexiones de Switch
grafo.insert_edge("Switch 1", "Mint", 80)
grafo.insert_edge("Switch 1", "Impresora", 22)
grafo.insert_edge("Switch 1", "Ubuntu", 18) 
grafo.insert_edge("Switch 1", "Debian", 17)
grafo.insert_edge("Switch 1", "Router 1", 29)

#conexiones Router 1
grafo.insert_edge("Router 1", "Router 2", 37)
grafo.insert_edge("Router 1", "Router 3", 43)

#conexiones Router 2
grafo.insert_edge("Router 2", "Red Hat", 25)
grafo.insert_edge("Router 2", "Guaraní", 9)
grafo.insert_edge("Router 2", "Router 3", 50)

#conexiones Router 3
grafo.insert_edge("Router 3", "Switch 2", 61)

#conexiones Switch 2
grafo.insert_edge("Switch 2", "Fedora", 3)
grafo.insert_edge("Switch 2", "Arch", 56)
grafo.insert_edge("Switch 2", "MongoDB", 5)
grafo.insert_edge("Switch 2", "Parrot", 12)
grafo.insert_edge("Switch 2", "Manjaro", 40)

#b) barrido en profundidad y amplitud desde: Red Hat, Debian, Arch (notebooks)

notebooks = ["Red Hat", "Debian", "Arch"]

#profundidad
for notebook in notebooks:
    print(f"barrido en profundidad desde {notebook}")
    grafo.deep_sweep(notebook)
    print()

#amplitud
for notebook in notebooks:
    print(f"barrido en amplitud desde {notebook}")
    grafo.amplitude_sweep(notebook)
    print()


#c) Encontrar el camino mas corto desde pc: manjaro, red hat y fedora hasta la impresora
def camino_mas_corto(grafo, origen, destino):
    stack = grafo.dijkstra(origen)

    while stack:
        dato = stack.pop()  # cada elemento es [vertice, costo_total, predecesor]
        if dato[0] == destino:
            print(f"El camino más corto a {destino} desde {origen} es de peso total {dato[1]}")
            break

camino_mas_corto(grafo, "Manjaro", "Impresora")
print()
camino_mas_corto(grafo, "Red Hat", "Impresora")
print()
camino_mas_corto(grafo, "Fedora", "Impresora")
print()

#d) encontrar el arbol de expansion minima
arbol = grafo.kruskal("Switch 1")
print("Arbol de expansion minima:", arbol)
print()

#e) determinar desde que pc (no notebook) es el camino más corto hasta el servidor "Guaraní"
def pc_mas_cercana(grafo, tipo_dispositivo, servidor):

    pc_mas_corta = None
    distancia_minima = float('inf')
    
    # Buscar todas las PCs (no notebooks)
    for vertice in grafo:
        if vertice.other_values == tipo_dispositivo:
            # Ejecutar Dijkstra desde esta PC
            stack = grafo.dijkstra(vertice.value)
            
            # Buscar la distancia al servidor
            while stack:
                dato = stack.pop()
                if dato[0] == servidor:
                    print(f"Desde {vertice.value} hasta {servidor}: distancia = {dato[1]}")
                    
                    # Actualizar si encontramos un camino más corto
                    if dato[1] < distancia_minima:
                        distancia_minima = dato[1]
                        pc_mas_corta = vertice.value
                    break
    
    print(f"La PC más cercana a {servidor} es: {pc_mas_corta} con distancia {distancia_minima}")
    return pc_mas_corta, distancia_minima

pc_mas_cercana(grafo, "pc", "Guaraní")
print()

#f)  indicar desde que computadora del switch 01 es el camino más corto al servidor “MongoDB”
def cercania_desde_nodo(grafo, nodo_origen, servidor):

    pc_mas_corta = None
    distancia_minima = float('inf')
    
    # Buscar el nodo origen
    pos_nodo = grafo.search(nodo_origen, 'value')
    
    if pos_nodo is not None:
        # Recorrer las aristas del nodo para encontrar computadoras conectadas
        for edge in grafo[pos_nodo].edges:
            # Buscar el vértice conectado
            pos_vertice = grafo.search(edge.value, 'value')
            
            if pos_vertice is not None:
                dispositivo = grafo[pos_vertice]
                tipo = dispositivo.other_values
                
                # Solo considerar PCs y notebooks (computadoras)
                if tipo in ["pc", "notebook"]:
                    # Calcular camino más corto desde esta computadora
                    stack = grafo.dijkstra(dispositivo.value)
                    
                    while stack:
                        dato = stack.pop()
                        if dato[0] == servidor:
                            if dato[1] < distancia_minima:
                                distancia_minima = dato[1]
                                pc_mas_corta = dispositivo.value
                            break
    
    print(f"La computadora de {nodo_origen} más cercana a {servidor} es: {pc_mas_corta} con distancia {distancia_minima}")
    return pc_mas_corta, distancia_minima

cercania_desde_nodo(grafo, "Switch 1", "MongoDB")
print()
    
# g) cambiar la conexión de la impresora al router 02 y vuelva a resolver el punto b
grafo.delete_edge("Switch 1", "Impresora", "value")
grafo.insert_edge("Router 2", "Impresora", 22)

# b) barridos en profundidad y amplitud
#profundidad
for notebook in notebooks:
    print(f"barrido en profundidad desde {notebook}")
    grafo.deep_sweep(notebook)
    print()

#amplitud
for notebook in notebooks:
    print(f"barrido en amplitud desde {notebook}")
    grafo.amplitude_sweep(notebook)
    print()
