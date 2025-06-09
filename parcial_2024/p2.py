from stack import Stack

pila_dinos = Stack()

dinosaurios = [
    {
      "nombre": "Tyrannosaurus Rex",
      "especie": "Theropoda",
      "peso en kg": 7000,
      "descubridor": "Barnum Brown",
      "ano_descubrimiento": 1902
    },
    {
      "nombre": "Triceratops",
      "especie": "Ceratopsidae",
      "peso en kg": 6000,
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1889
    },
    {
      "nombre": "Velociraptor",
      "especie": "Dromaeosauridae",
      "peso en kg": 15,
      "descubridor": "Henry Fairfield Osborn",
      "ano_descubrimiento": 1924
    },
    {
      "nombre": "Brachiosaurus",
      "especie": "Sauropoda",
      "peso en kg": 56000,
      "descubridor": "Elmer S. Riggs",
      "ano_descubrimiento": 1903
    },
    {
      "nombre": "Stegosaurus",
      "especie": "Stegosauridae",
      "peso en kg": 5000,
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1877
    },
    {
      "nombre": "Spinosaurus",
      "especie": "Spinosauridae",
      "peso en kg": 10000,
      "descubridor": "Ernst Stromer",
      "ano_descubrimiento": 1912
    },
    {
      "nombre": "Allosaurus",
      "especie": "Theropoda",
      "peso en kg": 2000,
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1877
    },
    {
      "nombre": "Apatosaurus",
      "especie": "Sauropoda",
      "peso en kg": 23000,
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1877
    },
    {
      "nombre": "Diplodocus",
      "especie": "Sauropoda",
      "peso en kg": 15000,
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1878
    },
    {
      "nombre": "Ankylosaurus",
      "especie": "Ankylosauridae",
      "peso en kg": 6000,
      "descubridor": "Barnum Brown",
      "ano_descubrimiento": 1908
    },
    {
      "nombre": "Parasaurolophus",
      "especie": "Hadrosauridae",
      "peso en kg": 2500,
      "descubridor": "William Parks",
      "ano_descubrimiento": 1922
    },
    {
      "nombre": "Carnotaurus",
      "especie": "Theropoda",
      "peso en kg": 1500,
      "descubridor": "José Bonaparte",
      "ano_descubrimiento": 1985
    },
    {
      "nombre": "Styracosaurus",
      "especie": "Ceratopsidae",
      "peso en kg": 2700,
      "descubridor": "Lawrence Lambe",
      "ano_descubrimiento": 1913
    },
    {
      "nombre": "Therizinosaurus",
      "especie": "Therizinosauridae",
      "peso en kg": 5000,
      "descubridor": "Evgeny Maleev",
      "ano_descubrimiento": 1954
    },
    {
      "nombre": "Pteranodon",
      "especie": "Pterosauria",
      "peso en kg": 25,
      "descubridor": "Othniel Charles Marsh",
      "ano_descubrimiento": 1876
    },
    {
      "nombre": "Quetzalcoatlus",
      "especie": "Pterosauria",
      "peso en kg": 200,
      "descubridor": "Douglas A. Lawson",
      "ano_descubrimiento": 1971
    },
    {
      "nombre": "Plesiosaurus",
      "especie": "Plesiosauria",
      "peso en kg": 450,
      "descubridor": "Mary Anning",
      "ano_descubrimiento": 1824
    },
    {
      "nombre": "Mosasaurus",
      "especie": "Mosasauridae",
      "peso en kg": 15000,
      "descubridor": "William Conybeare",
      "ano_descubrimiento": 1829
    },

  ]

for dino in dinosaurios:
    pila_dinos.push(dino)

#restaurar la pila luego de recorrerla
def restaurar_pila(pila, aux):
    while aux:
        pila.push(aux.pop())

#contar especies
def contar_especies(pila):
    aux = Stack()
    especies = set()

    while pila:
        dino = pila.pop()
        aux.push(dino)
        especies.add(dino['especie'])

    print(f"Hay {len(especies)} especies distintas en la pila.")
    restaurar_pila(pila, aux)

#contar descubridores
def contar_descubridores(pila):
    aux = Stack()
    descubridores = set()

    while pila:
        dino = pila.pop()
        aux.push(dino)
        descubridores.add(dino['descubridor'])

    print(f"Hay {len(descubridores)} descubridores distintos en la pila.")
    restaurar_pila(pila, aux)

#dinosaurios con inicial T
def dinosaurios_con_T(pila):
    aux = Stack()
    pila_temp = Stack()

    while pila:
        dino = pila.pop()
        if dino['nombre'].startswith('T'):
            pila_temp.push(dino['nombre'])
        aux.push(dino)

    restaurar_pila(pila, aux)

    if pila_temp:
        print('Dinosaurios que comienzan con T:')
        pila_temp.show()
    else:
        print('No hay dinosaurios con la inicial T en la pila.')

#dinosaurios de menos de 275 kg
def dinosaurios_por_peso(pila):
    aux = Stack()
    pila_temp = Stack()

    while pila:
        dino = pila.pop()
        aux.push(dino)
        if dino['peso en kg'] < 275:
            pila_temp.push(dino['nombre'])

    if pila_temp:
        print('dinosaurios que pesan menos de 275kg: ')
        pila_temp.show()
    else: print('no hay dinosuarios que pesen menos de 275kg en la pila')

    restaurar_pila(pila, aux)

#crear nueva pila
dinos_AQS = Stack()

#separar dinos
def separar_dinos(pila):
    aux = Stack()

    while pila:
        dino = pila.pop()
        if dino['nombre'].startswith(('A', 'Q', 'S')):
            dinos_AQS.push(dino)
        else: aux.push(dino)

    if dinos_AQS:
        print('pila nueva:')
        dinos_AQS.show()
    else: print('no hay dinosaurios con las iniciales A, Q o S') 

    restaurar_pila(pila, aux)   
    
#ejecucion
contar_especies(pila_dinos)
print()
contar_descubridores(pila_dinos)
print()
dinosaurios_con_T(pila_dinos)
print()
dinosaurios_por_peso(pila_dinos)
print()
separar_dinos(pila_dinos)