from List_ import List

lista = List()

palabra = 'hola'

for letra in palabra:
    lista.append(letra)

if lista == lista[::-1]:#[::-1] es una reversa de la lista
    print(f'{palabra} es palindromo')
else:
    print(f'{palabra} no es palindromo')
