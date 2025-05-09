from stack import Stack

trajes = Stack()
trajes_aux = Stack()

#llenar pila
trajes.push({"modelo":"Mark III",
             "pelicula":"Iron Man",
             "estado":"dañado"})

trajes.push({"modelo":"Mark V",
             "pelicula":"Iron Man 2",
             "estado":"impecable"})

trajes.push({"modelo":"Mark XLIV",
             "pelicula":"Avengers: la era de Ultron",
             "estado":"dañado"})

trajes.push({"modelo":"Mark XLII",
             "pelicula":"Iron Man 3",
             "estado":"destruido"})

trajes.push({"modelo":"Traje Stark",
             "pelicula":"Civil War",
             "estado":"dañado"})

trajes.push({"modelo":"Mark I",
             "pelicula":"Spider Man: Homecoming",
             "estado":"impecable"})

trajes.push({"modelo":"traje casero",
             "pelicula":"Spider Man: Homecoming",
             "estado":"impecable"})

#funcion para restaurar la pila
def restaurar_pila(destino, origen):
    while origen:
        traje = origen.pop()
        if traje is None:
            break
        destino.push(traje)

#buscar si esta en la pila el traje Mark XLIV
def buscar_modelo(trajes, trajes_aux):
    encontrado = False

    while trajes:
        traje = trajes.pop()
        if traje is None:
            break
        if traje["modelo"].lower() == ("Mark XLIV").lower(): #utilizo lower para evitar errores por diferencias en la escritura
            print(f"Se encontró: {traje["modelo"]} / Película: {traje["pelicula"]} / Estado: {traje["estado"]}")
            encontrado = True
        trajes_aux.push(traje)

    restaurar_pila(trajes, trajes_aux)
    if not encontrado:
        print("El modelo Mark XLIV no fue encontrado")

#Trajes dañados
def mostrar_dañados(trajes, trajes_aux):
    print("Trajes dañados:")

    while trajes:
        traje = trajes.pop()
        if traje is None:
            break
        if traje["estado"] == "dañado":
            print(f"- {traje["modelo"]}")
        trajes_aux.push(traje)

    restaurar_pila(trajes, trajes_aux)

#Trajes destruidos
def eliminar_destruidos(trajes, trajes_aux):
    print("Eliminando trajes destruidos:")

    while trajes:
        traje = trajes.pop()
        if traje is None:
            break
        if traje["estado"] == "destruido":
            print(f"- {traje["modelo"]}")
        else:
            trajes_aux.push(traje)

    restaurar_pila(trajes, trajes_aux)

#Agregar Mark LXXXV
def agregar_traje(trajes):
    nuevo = ({"modelo":"Mark LXXXV",
              "pelicula":"Avengers: Endgame",
              "estado":"destruido"})
    trajes.push(nuevo)        

#Trajes de Civil War y Spiderman: homecoming
def trajes_peliculas(trajes, trajes_aux):
    while trajes:
        traje = trajes.pop()
        if traje is None:
            break
        if traje["pelicula"].lower() == ("Civil War").lower():
            print(f"traje/s usado/s en Civil WAr: ", traje["modelo"])
        elif traje["pelicula"].lower() == ("Spider Man: Homecoming").lower():
            print(f"traje/s usado/s en Spider Man: Homecoming: ", traje["modelo"])
    
    restaurar_pila(trajes, trajes_aux)    

#ejecucion
buscar_modelo(trajes, trajes_aux)
print()
mostrar_dañados(trajes, trajes_aux)
print()
eliminar_destruidos(trajes, trajes_aux)   
print()
agregar_traje(trajes)
trajes_peliculas(trajes, trajes_aux)     