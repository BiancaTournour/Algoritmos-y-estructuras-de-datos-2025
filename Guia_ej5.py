from Tree import BinaryTree

from superheroes_data import superheroes

tree = BinaryTree()
H_tree = BinaryTree()
V_tree = BinaryTree()

for super_hero in superheroes:
     tree.insert(super_hero['name'], super_hero)


#b) listar villanos en odern alfabetico
def villanos_en_orden(tree):
    def _inorder(node):
        if node is not None:
            _inorder(node.left) #va al subarbol izquierdo
            if node.other_values["is_villain"] is True: #procesa el nodo / other values guadra los demas datos
                print(node.value)  # si es villano muestra el nombre
            _inorder(node.right) # va al subarbol derecho

    if tree.root is not None:
        _inorder(tree.root)

#c) mostrar los superheroes con C
def heroes_por_inicial(tree):
    def __heroes_por_inicial(node):
        if node is not None:
            __heroes_por_inicial(node.left)
            if node.value.startswith('C'):
                print(node.value)
            __heroes_por_inicial(node.right)

    if tree.root is not None:
        __heroes_por_inicial(tree.root)            

#d) determinar cuantos superheroes hay en el arbol
def contar_heroes(tree):
    contador = [0]
    def __contar_heroes(node):  
        if node is not None:
            __contar_heroes(node.left)
            if node.other_values["is_villain"] is False:
                contador [0] += 1
            __contar_heroes(node.right)  

    if tree.root is not None:
        __contar_heroes(tree.root)    
    print(f"hay {contador} heroes en el arbol")              

#e) busqueda por proximidad
def buscar_dr(tree):
 tree.proximity_search('Dr')
 print()
 name = input('ingrese nombre para modificar: ')
 value, other_value = tree.delete(name)
 if value is not None:
    fix_name = input('ingrese el nuevo nombre: ')
    other_value['name'] = fix_name
    tree.insert(fix_name, other_value) 

#g) crear bosque
def divide_tree(tree, arbol_h, arbol_v):
        def __divide_tree(node, arbol_h, arbol_v):
            if node is not None:
                if node.other_values["is_villain"] is False:
                    arbol_h.insert(node.value, node.other_values)
                else:
                    arbol_v.insert(node.value, node.other_values)
                __divide_tree(node.left, arbol_h, arbol_v)
                __divide_tree(node.right, arbol_h, arbol_v)
         
        __divide_tree(tree.root, arbol_h, arbol_v)      

#contar nodos
def count_nodes(tree):
    contador = [0]

    def __count_nodes(node):
        if node is not None:
            __count_nodes(node.left)
            contador[0] += 1
            __count_nodes(node.right)

    if tree.root is not None:
        __count_nodes(tree.root)    
    print(f"hay {contador} nodos en el arbol indicado")  

#generar bosque
bosque = [H_tree, V_tree]

#ejecucion
print()
villanos_en_orden(tree) #b)
print()
heroes_por_inicial(tree) #c)
print()
contar_heroes(tree) #d)
print()
buscar_dr(tree) #e)
print()
tree.post_order() #f) lista descendente
print()
divide_tree(tree, H_tree, V_tree) #g) dividir arbol
print()
#g) I)
print("nodos del arbol de heroes:")
count_nodes(H_tree)
print()
print("nodos del arbol de villanos:")
count_nodes(V_tree)
#g) II)
print()
print("barridos de: arbol de heroes y arbol de villanos:")
for tree in bosque:
    tree.in_order()
    print()