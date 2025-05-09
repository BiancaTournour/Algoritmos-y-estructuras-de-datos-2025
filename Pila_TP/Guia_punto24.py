from stack import Stack

pila_personajes = Stack()
pila_temporal = Stack()
temp = Stack()

#llenar pila
pila_personajes.push({"personaje":"Hulk",
                      "participaciones/peliculas":11})  

pila_personajes.push({"personaje":"Wanda Maximoff",
                      "participaciones/peliculas":4})  

pila_personajes.push({"personaje":"Black Widow",
                      "participaciones/peliculas":9})  

pila_personajes.push({"personaje":"Capitan America",
                      "participaciones/peliculas":11})

pila_personajes.push({"personaje":"Rocket Raccoon",
                      "participaciones/peliculas":7})

pila_personajes.push({"personaje":"Clint Barton",
                      "participaciones/peliculas":6})

pila_personajes.push({"personaje":"Groot",
                      "participaciones/peliculas":7})

pila_personajes.push({"personaje":"Doctor Strange",
                      "participaciones/peliculas":4})  

#funcion para restaurar la pila
def restaurar_pila(destino, origen):
    temp = Stack()
    while origen:
        temp.push(origen.pop())
    while temp:
        destino.push(temp.pop())

#poscion de los personajes (tomando como 1 la cima de la pila)
def posiciones(pila_personajes):
    i = 0
    while pila_personajes:
        personaje = pila_personajes.pop()
        temp.push(personaje)
        i += 1
        if personaje is None:
            break
        if personaje["personaje"].lower() == "Rocket Raccoon".lower():
            print (f"el personaje {personaje["personaje"]} se encuentra en la posicion {i}")
        elif personaje["personaje"].lower() == "Groot".lower():
            print (f"el personaje {personaje["personaje"]} se encuentra en la posicion {i}")

    restaurar_pila(pila_personajes, temp)    


#participaciones en peliculas
def participaciones(pila_personajes, pila_temporal):
    while pila_personajes:
        personaje = pila_personajes.pop()
        if personaje is None:
            break
        temp.push(personaje)
        if int(personaje["participaciones/peliculas"]) > 5:
            pila_temporal.push(personaje)
    restaurar_pila(pila_personajes, temp)        

#participaciones de black widow
def Black_Widow(pila_personajes, temp):
    while pila_personajes:
        personaje = pila_personajes.pop()
        if personaje is None:
            break
        temp.push(personaje)
        if personaje["personaje"].lower() == "black widow":
            print(f"Black Widow participo en {personaje['participaciones/peliculas']} peliculas")
    restaurar_pila(pila_personajes, temp)        

#personajes con C, D o G
def iniciales(pila_personajes, temp):
    while pila_personajes:
        personaje = pila_personajes.pop()
        if personaje is None:
            break
        temp.push(personaje)
        inicial = personaje["personaje"][0].upper()
        if inicial in ("C", "D", "G"):
            print(personaje['personaje'])
    restaurar_pila(pila_personajes, temp)

#ejecucion
posiciones(pila_personajes)
print()
participaciones(pila_personajes,pila_temporal)
print("personajes con mas de 5 apariciones:")
pila_temporal.show()
print()
Black_Widow(pila_personajes, temp)
print()
print("personajes con inicial C, G o D")
iniciales(pila_personajes, temp)