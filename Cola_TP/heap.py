from typing import Any

class HeapMax:#el elemento padre siempre es mayor o igual que sus hijos

    def __init__(self):#Inicializa el heap creando una lista vacía
        self.elements = []
    
    def size(self) -> int:#Devuelve la cantidad de elementos en el heap
        return len(self.elements)
    
    #Agregue un valor al final de la lista y luego reorganice el montón llamando a float
    def add(self, value: Any) -> None:
        self.elements.append(value)
        self.float(self.size()-1)
    
    #Elimina y devuelve el elemento máximo (raíz del heap). Intercambia la raíz con el último elemento, elimina el último y reorganiza el montón con sink
    def remove(self) -> Any:
        last = self.size() -1
        self.interchange(0, last)
        value = self.elements.pop()
        self.sink(0)
        return value

    #Sube un elemento en el heap hacia la raíz si es mayor que su padre
    def float(self, index: int) -> None:
        father = (index - 1) // 2
        while index > 0 and self.elements[index] > self.elements[father]:
            # print(f'flotar desde {index} a {father}')
            self.interchange(index, father)
            index = father
            father = (index - 1) // 2

    #Baja un elemento en el heap hacia las hojas si es menor que sus hijos, intercambiando con el hijo mayor hasta que se cumpla la propiedad de heap
    def sink(self, index: int) -> None:
        left_son = (2 * index) + 1
        control = True
        while control and left_son < self.size():
            right_son = left_son + 1

            mayor = left_son
            if right_son < self.size():
                if self.elements[right_son] > self.elements[mayor]:
                    mayor = right_son

            if self.elements[index] < self.elements[mayor]:
                # print(f'hundir desde {index} a {mayor}')
                self.interchange(index, mayor)
                index = mayor
                left_son = (2 * index) + 1
            else:
                control = False


    #Intercambia los elementos en las posiciones index_1y index_2en la lista
    def interchange(self, index_1: int, index_2: int) -> None:
        self.elements[index_1], self.elements[index_2] = self.elements[index_2], self.elements[index_1]

    #Ordena los elementos del heap en orden descendente (de mayor a menor) eliminando repetidamente el máximo y almacenándolo en una lista
    def heapsort(self) -> list:
        result = []
        while self.size() > 0:
            result.append(self.remove())
        return result

    #Agrega un valor con una prioridad (1-baja, 2-media, 3-alta) como una lista [priority, value], utilizando addpara insertarlo en el montón
    def arrive(self, value: Any, priority: int) -> None:
        # priority 1-low, 2-medium, 3-high
        self.add([priority, value])
    
    #Elimina y devuelve el elemento de mayor prioridad del heap (similar a remove), útil para simulaciones de colas de prioridad
    def attention(self) -> Any:
        value = self.remove()
        return value


#el elemento padre siempre es menor o igual que sus hijos
class HeapMin:

    def __init__(self):
        self.elements = []
    
    def size(self) -> int:
        return len(self.elements)

    def add(self, value: Any) -> None:
        self.elements.append(value)
        self.float(self.size()-1)
    
    def remove(self) -> Any:
        last = self.size() -1
        self.interchange(0, last)
        value = self.elements.pop()
        self.sink(0)
        return value

    def float(self, index: int) -> None:
        father = (index - 1) // 2
        while index > 0 and self.elements[index] < self.elements[father]:
            self.interchange(index, father)
            index = father
            father = (index - 1) // 2

    def sink(self, index: int) -> None:
        left_son = (2 * index) + 1
        control = True
        while control and left_son < self.size():
            right_son = left_son + 1

            minor = left_son
            if right_son < self.size():
                if self.elements[right_son] < self.elements[minor]:
                    minor = right_son

            if self.elements[index] > self.elements[minor]:
                self.interchange(index, minor)
                index = minor
                left_son = (2 * index) + 1
            else:
                control = False


    def interchange(self, index_1: int, index_2: int) -> None:
        self.elements[index_1], self.elements[index_2] = self.elements[index_2], self.elements[index_1]

    # def monticulizar

    def heapsort(self) -> list:
        result = []
        while self.size() > 0:
            result.append(self.remove())
        return result

    def arrive(self, value: Any, priority: int) -> None:
        # priority 1-low, 2-medium, 3-high
        self.add([priority, value])
    
    def attention(self) -> Any:
        value = self.remove()
        return value
