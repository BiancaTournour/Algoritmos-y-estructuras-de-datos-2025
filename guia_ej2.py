from List_ import List
import random
import string

lista = List()
vocales = ['a', 'e', 'i', 'o', 'u']

for i in range (10):
    lista.append(random.choice(string.ascii_lowercase))

print('lista original:')
lista.show()    

for letra in lista[:]:  # recorremos una copia con lista[:] para evitar problemas
    if letra in vocales:
        lista.delete_value(letra)

print()
print('lista sin vocales:')
lista.show()
    