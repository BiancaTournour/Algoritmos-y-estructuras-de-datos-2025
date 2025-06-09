lista = [1, 2, 3, 4, 5]

def listar_inversa(lista):
    if lista:  
        print(lista[-1])           
        listar_inversa(lista[:-1]) 

listar_inversa(lista)        