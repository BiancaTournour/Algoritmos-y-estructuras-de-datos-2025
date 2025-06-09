from List_ import List

lista_ = List()

lista_.append('B')
lista_.append('I')
lista_.append('A')
lista_.append('N')
lista_.show()

print(f'hay {lista_.__len__()} nodos en la lista')       

lista_.append('C')
lista_.append('A')

print(f'hay {lista_.__len__()} nodos en la lista')

lista = List()
lista = List(['a', 'b', 'c']) #con el constructor
lista.show()