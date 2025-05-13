from stack import Stack
from Queue import Queue

cola_personajes = Queue()
cola_masculinos = Queue()
cola_femeninos = Queue()

cola_personajes.arrive({"personaje":"Tony Stark",
                        "superheroe":"Iron Man",
                        "genero":"M"})

cola_personajes.arrive({"personaje":"Steve Rogers",
                        "superheroe":"Capitan America",
                        "genero":"M"})

cola_personajes.arrive({"personaje":"Peter Paker",
                        "superheroe":"Spider Man",
                        "genero":"M"})

cola_personajes.arrive({"personaje":"Stephen Strange",
                        "superheroe":"Doctor Strange",
                        "genero":"M"})

cola_personajes.arrive({"personaje":"Wanda Maximoff",
                        "superheroe":"Bruja Escarlata",
                        "genero":"F"})

cola_personajes.arrive({"personaje":"Natasha Romanoff",
                        "superheroe":"Black Widow",
                        "genero":"F"})

cola_personajes.arrive({"personaje":"Scott Lang",
                        "superheroe":"Ant Man",
                        "genero":"M"})  

cola_personajes.arrive({"personaje":"Carol Danvers",
                        "superheroe":"Capitana Marvel",
                        "genero":"F"})

cola_personajes.arrive({"personaje":"Bruce Banner",
                        "superheroe":"Hulk",
                        "genero":"M"})  

#funcion para restaurar la cola
def restaurar_cola(cola, pila):
    temp = Stack()
    while pila:
        temp.push(pila.pop()) 
    while temp:
        cola.arrive(temp.pop())  

#funcion para saber si Carol Danvers existe en la cola
def carol_danvers(cola_personajes):
    pila_aux = Stack()
    carol = False
    while cola_personajes:
        personaje = cola_personajes.attention()
        pila_aux.push(personaje)
        if personaje["personaje"] == "Carol Danvers":
            carol = True  
            print("Carol Danvers se ecnuentra en la cola")
            break 
    restaurar_cola(cola_personajes, pila_aux) 
    if carol:
        capitana_marvel(cola_personajes) 
    else: print("Carol Danvers no se encuentra en la cola")  
         
#funcion para encontrar el nombre de capitana marvel
def capitana_marvel(cola_personajes):
    pila_aux = Stack()
    while cola_personajes:
        personaje = cola_personajes.attention()
        pila_aux.push(personaje)
        if personaje["superheroe"].lower() == "capitana marvel":
            print(f"nombre: {personaje['personaje']}, nombre de superheroe: {personaje['superheroe']}")
    restaurar_cola(cola_personajes, pila_aux)

#funcion para encontrar el nombre de superheroe de scott lang
def scott_lang(cola_personajes):
    pila_aux = Stack()
    while cola_personajes:
        personaje = cola_personajes.attention()
        pila_aux.push(personaje)
        if personaje["personaje"].lower() == "scott lang":
            print(f"nombre de superheroe de {personaje['personaje']}: {personaje['superheroe']}")
    restaurar_cola(cola_personajes, pila_aux)   

#funcion para crear una cola alternativa con los nombres de los personajes femeninos
def superheroes_femeninos(cola_personajes):
    pila_aux = Stack()
    while cola_personajes:
        personaje = cola_personajes.attention()
        pila_aux.push(personaje)
        if personaje["genero"] == "F":
            cola_femeninos.arrive(personaje["personaje"])
    restaurar_cola(cola_personajes, pila_aux)    

#funcion para crear una cola alternativa con los nombres de los personajes masculinos
def superheroes_masculinos(cola_personajes):
    pila_aux = Stack()
    while cola_personajes:
        personaje = cola_personajes.attention()
        pila_aux.push(personaje)
        if personaje["genero"] == "M":
            cola_masculinos.arrive(personaje["personaje"])
    restaurar_cola(cola_personajes, pila_aux) 

#funcion para mostrar los personajes cuyo nombre real o de superheroe empieza con S
def personajes_s(cola_personajes):
    pila_aux = Stack()
    while cola_personajes:
        personaje = cola_personajes.attention()
        pila_aux.push(personaje)       
        if personaje["personaje"][0].upper() == "S" or personaje["superheroe"][0].upper() == "S":
            print(personaje)      
    restaurar_cola(cola_personajes, pila_aux)             

#ejecucion
carol_danvers(cola_personajes) 
print()
scott_lang(cola_personajes)
print()
superheroes_femeninos(cola_personajes) 
print("personajes femeninos:")
cola_femeninos.show()  
print()
superheroes_masculinos(cola_personajes)
print("personajes masculinos:")
cola_masculinos.show()  
print()
print("personajes con inicial S (nombre real o de superheroe):")
personajes_s(cola_personajes)