from Tree import BinaryTree
from criaturasdata import criaturas
from collections import Counter

tree = BinaryTree()

for criatura in criaturas:
    tree.insert(criatura['criatura'], criatura)

#a) imprimir las criaturas y quien las derrotó
def _in_order(tree): 
    def __in_order(node):
        if node is not None:
            __in_order(node.left)
            print(f"Criatura: {node.other_values.get('criatura')}, Derrotado por: {node.other_values.get('derrotado_por')}")
            __in_order(node.right)

    if tree.root is not None:
        __in_order(tree.root)

#c) mostrar toda la informacion de una criatura
def mostrar(tree, name):
    nodo = tree.search(name)
    if nodo is not None:
        print(f"criatura: {nodo.value}, breve descripcion: {nodo.other_values.get('descripcion')}, derrotado por: {nodo.other_values.get('derrotado_por')}, capturado por: {nodo.other_values.get('capturada')}")

#d) heroes con mas victorias
def top_victorias(tree):
    derrotas = []

    def _top_victorias(node):
        if node is not None:
            _top_victorias(node.left)
            derrotado = node.other_values.get('derrotado_por')
            if derrotado:
                derrotas.append(derrotado)
            _top_victorias(node.right)

    _top_victorias(tree.root)

    contador = Counter(derrotas)
    print('top 3 heroes con mas victorias y cantidad de victorias:')
    print(contador.most_common(3))

#e) criaturas derrotadas por un mismo heroe
def derrotas(tree, name):
    lista = []
    def _derrotas(node):
        if node is not None:
            _derrotas(node.left)
            if node.other_values.get('derrotado_por') == name:
                lista.append(node.value)
            _derrotas(node.right)  
    
    _derrotas(tree.root)

    print(f"criaturas derrotadas por {name}:")
    print(lista)

#f) criaturas sin derrotas
def sin_derrotas(tree):
    lista = []
    def _sin_derrotas(node):
        if node is not None:
            _sin_derrotas(node.left)
            if node.other_values.get('derrotado_por') == None:
                lista.append(node.value)
            _sin_derrotas(node.right)

    _sin_derrotas(tree.root)

    print(f"criaturas sin derrotas:")
    print(lista)                


#modificador para campos generales (descripcion, derrotado_por, capturada, etc.) puntos b, h y k
def modificador(tree, name, campo, nuevo_valor):
    encontrado = False

    def _modificador(node):
        nonlocal encontrado
        if node is not None:
            _modificador(node.left)
            if node.value == name:
                node.other_values[campo] = nuevo_valor
                print(f"Se modificó el campo: {campo}, de la criatura: {name}, su valor actual es: {nuevo_valor}")
                encontrado = True
            _modificador(node.right)

    _modificador(tree.root)

    if not encontrado:
        print("No se ha encontrado el valor buscado en el árbol")


# l) modificar el nombre de Ladón
def modificar_nombre(tree, nombre_viejo, nombre_nuevo):
    nodo = tree.search(nombre_viejo)
    if nodo is not None:
        datos = nodo.other_values.copy()
        # eliminar el nodo viejo
        tree.delete(nombre_viejo)
        # actualizar el nombre dentro de los datos
        datos['criatura'] = nombre_nuevo
        # insertar con el nuevo nombre
        tree.insert(nombre_nuevo, datos)
        print(f"Se modificó el nombre de la criatura {nombre_viejo} por {nombre_nuevo}")
    else:
        print(f"No se encontró la criatura {nombre_viejo} en el árbol")


#n) criaturas capturadas por un héroe
def capturas(tree, name):
    print(f"criaturas capturadas por {name}:")
    def _capturas(node):
        if node is not None:
            _capturas(node.left)
            if node.other_values['capturada'] == name:
                print(node.value) 
            _capturas(node.right)

    _capturas(tree.root)                   


#ejecucion
#a)
_in_order(tree)
print()

#b) ejemplo
modificador(tree, 'Sirenas', 'descripcion', 'Seres que atraían marineros con su canto hasta naufragar y respiraban bajo el agua.')
print()

#c)
mostrar(tree, 'Talos')
print()

#d)
top_victorias(tree)
print()

#e)
derrotas(tree, 'Heracles')
print()

#f)
sin_derrotas(tree)
print()

#h)  modifique los nodos de las criaturas Cerbero, Toro de Creta, Cierva Cerinea y Jabalí de Erimanto indicando que Heracles las atrapó
capturadas = ['Cerbero', 'Toro de Creta', 'Cierva de Cerinea', 'Jabali de Erimanto']
for criatura in capturadas:
    modificador(tree, criatura, 'capturada', 'Heracles')
print()

#i)
print("busqueda por coincidencia con ejemplo 'Ha...':")
tree.proximity_search("Ha")
print()

#j)
tree.delete("Basilisco")
tree.delete("Sirenas")

#k)  modificar el nodo que contiene a las Aves del Estínfalo, agregando que Heracles derroto a varias
modificador(tree, 'Aves del Estínfalo', 'derrotado_por', 'Heracles')
print()

#l) usar la nueva funcion para cambiar el nombre de Ladón
modificar_nombre(tree, 'Ladón', 'Dragón Ladón')
print()

#m) listado por nivel
print("listado por nivel:")
print(tree.by_level())
print()

#n)
capturas(tree, "Heracles")
