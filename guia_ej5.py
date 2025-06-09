from List_ import List
from random import randint

lista = List()

for numeros in range (20):
    lista.append(randint(1, 100))

lista.sort()

print('lista original:')
lista.show()
print()    

def es_primo(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    for i in range(3, int(n**0.5) + 1, 2):  # solo impares hasta raíz de n
        if n % i == 0:
            return False
    return True

for numero in lista[:]:
    if es_primo(numero):
     lista.delete_value(numero)

lista.sort()
print('lista sin numeros primos:')
lista.show()