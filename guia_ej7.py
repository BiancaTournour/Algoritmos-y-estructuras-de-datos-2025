from List_ import List

lista = List([1, 2, 3, 4, 5, 10, 7])
lista2 = List([6, 7, 8, 9, 10])

# Guardar copias
lista_original = lista[:]
lista2_original = lista2[:]

#Restaurar
def restaurar_listas(lista1, copia1, lista2, copia2):#si no restauramos las listas luego de cada uso las siguientes funciones no van a funcionar
    lista1[:] = copia1
    lista2[:] = copia2

#unir listas
def unir_listas(lista1, lista2):
    for item in lista2:
        lista1.append(item)

unir_listas(lista, lista2)
print('listas unidas:')
lista.show() 
print()

restaurar_listas(lista, lista_original, lista2, lista2_original)

#unir sin repeticiones
def unir_sin_repetir(lista1, lista2):
    for item in lista2:
        if item not in lista1:
            lista1.append(item)

unir_sin_repetir(lista, lista2)

print('Listas unidas sin elementos repetidos:')
lista.show()

restaurar_listas(lista, lista_original, lista2, lista2_original)

#interseccion de las listas (elementos compartidos)
def interseccion(lista1, lista2):
    cont = 0
    for item in lista1:
        if item in lista2:
            cont += 1
    print(f'las listas comparten {cont} elementos')        

print()
interseccion(lista, lista2)          
restaurar_listas(lista, lista_original, lista2, lista2_original)

print()
#eliminar elementos de una lista, uno a la vez y mostrandolo
while lista:
    print('eliminar:')
    print(lista.pop())

restaurar_listas(lista, lista_original, lista2, lista2_original)    