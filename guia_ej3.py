from List_ import List
from random import randint

lista_enteros = List()
lista_pares = List()
lista_impares = List()

for num in range (30):
    lista_enteros.append(randint(1, 100))

lista_enteros.sort()
print('lista de enteros:')
lista_enteros.show()    

def separar_lista(enteros ,pares, impares):
    while enteros:
        num = enteros.pop() #la lista original se destruye
        if num % 2 == 0:
            pares.append(num)
        else: impares.append(num)   

print()
separar_lista(lista_enteros, lista_pares, lista_impares)  
#ordeno las nuevas listas antes de mostrarlas
lista_pares.sort()
lista_impares.sort()

print('lista pares:') 
lista_pares.show()

print()
print('lista impares:')
lista_impares.show()  