from Tree import BinaryTree

from pokemons_data import pokemons

tree_nombres = BinaryTree()
tree_numeros = BinaryTree()
tree_tipos = BinaryTree()

for pokemon in pokemons:
    tree_nombres.insert(pokemon["nombre"], pokemon)

for pokemon in pokemons:
    tree_numeros.insert(pokemon["numero"], pokemon)
    
for pokemon in pokemons:
    for tipo in pokemon["tipos"]:
        nodo = tree_tipos.search(tipo)
        if nodo is None:
            tree_tipos.insert(tipo, [pokemon])
        else:
            nodo.other_values.append(pokemon)

# mostrar datos de un pokemon a partir de su numero
def buscar_por_numero(tree, numero):
     node = tree.search(numero)
     if node is not None:
          print(f"numero: {numero}, nombre: {node.other_values.get("nombre")}, tipo/s: {node.other_values.get("tipos")}, debilidades: {node.other_values.get("debilidades")}, mega evolucion: {node.other_values.get("mega_evolucion")}, gigamax: {node.other_values.get("gigamax")}")
     else: print(f"no se encontro un pokemon con el numero {numero} en el arbol")

buscar_por_numero(tree_numeros, 9) #en este caso es mas util usar el arbol con valor principal numero
print()

#buscar por nombre con proximity search
def buscar_por_nombre(tree, texto):
    resultados = []
    
    def __proximity_search(node, texto):
        if node is not None:
            if node.value.startswith(texto):
                resultados.append(node.value)
            __proximity_search(node.left, texto)
            __proximity_search(node.right, texto)
    
    if tree.root is not None:
        __proximity_search(tree.root, texto)
    
    for nombre in resultados:
        node = tree.search(nombre)
        if node is not None:
            print(f"numero: {node.other_values.get('numero')}, nombre: {node.value}, tipo/s: {node.other_values.get('tipos')}, debilidades: {node.other_values.get('debilidades')}, mega evolucion: {node.other_values.get('mega_evolucion')}, gigamax: {node.other_values.get('gigamax')}")

print("ejemplo: busqueda por proximidad con Ga...")
buscar_por_nombre(tree_nombres, "Ga")
print()

# mostrar todos los pokemons de un tipo
def mostrar_por_tipo(tree_tipos, tipo):
    nodo = tree_tipos.search(tipo)
    if nodo:
        for pokemon in nodo.other_values:
            print(pokemon["nombre"])
    else:
        print(f"No se encontraron pokémons de tipo {tipo}")

tipos = ["Fantasma", "Fuego", "Acero", "Eléctrico"]
for tipo in tipos:
    print(f"tipo: {tipo}")
    mostrar_por_tipo(tree_tipos, tipo)
    print()

print()

# listados Ascendentes 
print("listado ascendente por numeros:")
tree_numeros.in_order()
print()

print("listado ascendente por nombres:")
tree_nombres.in_order()
print()

# listados por nivel
print("listado por nivel (por nombre):")
tree_nombres.by_level()
print()

# pokemons debiles frente a otros
def mostrar_debiles_contra(tree, nombres_atacantes):
    tipos_atacantes = []
    
    # Obtener los tipos de los atacantes
    for nombre in nombres_atacantes:
        node = tree.search(nombre)
        if node is not None:
            for tipo in node.other_values.get("tipos"):
                tipos_atacantes.append(tipo)
    
    print(f"tipos de ataque: {tipos_atacantes}")
    
    # Buscar pokémons débiles a esos tipos
    def __buscar_debiles(node):
        if node is not None:
            __buscar_debiles(node.left)
            debilidades = node.other_values.get("debilidades")
            for tipo in tipos_atacantes:
                if tipo in debilidades:
                    print(node.other_values.get("nombre"))
                    break
            __buscar_debiles(node.right)
    
    if tree_nombres.root is not None:
        __buscar_debiles(tree_nombres.root)

mostrar_debiles_contra(tree_nombres, ["Jolteon", "Lycanroc", "Tyrantrum"])
print()

# tipos de pokemon y cantidad de cada tipo
def contar_por_tipo(tree):
    tipos_count = {}
    
    def __contar(node):
        if node is not None:
            __contar(node.left)
            tipo = node.value
            cantidad = len(node.other_values)
            tipos_count[tipo] = cantidad
            __contar(node.right)
    
    if tree_tipos.root is not None:
        __contar(tree.root)
    
    for tipo in tipos_count:
        print(f"{tipo}: {tipos_count[tipo]}")
    
    print(f"total de tipos: {len(tipos_count)}")

print("pokemons de cada tipo:")
contar_por_tipo(tree_tipos)
print()

# cuantos pokemons tienen mega evolucion y gigamax
def caracteristica_bool_(tree, caracteristica):
    contador = 0
    def __caracteristica_bool_(node, caracteristica):
        nonlocal contador

        if node is not None:
            __caracteristica_bool_(node.left, caracteristica)
            if node.other_values.get(caracteristica) is True:
                contador += 1
            __caracteristica_bool_(node.right, caracteristica)

    __caracteristica_bool_(tree.root, caracteristica)
    print(f"hay {contador} pokemons con {caracteristica} en el arbol")

caracteristica_bool_(tree_nombres, "mega_evolucion")
print()
caracteristica_bool_(tree_nombres, "gigamax")      