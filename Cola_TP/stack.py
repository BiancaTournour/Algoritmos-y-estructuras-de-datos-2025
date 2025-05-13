from typing import Any
from typing import Optional


class Stack:#el objeto es una instancia de la clase, es decir, lo que defino dentro

    def __init__(self):#__init__ constructor, primer funcion de una clase, aquella clase con lo contenga sera la primera en la herencia de clases (superclase)
        self.__elements = [] #pila

    def push(self, value: Any) -> None:#apilar, agregar
        self.__elements.append(value)

    def pop(self) -> Optional[Any]:#eliminar el ultimo elemento
        return (self.__elements.pop()
                if self.__elements
                else None)

    def size(self) -> int:#tamaño de la pila
        return len(self.__elements)

    def on_top(self) -> Optional[Any]:
        return (self.__elements[-1]
                if self.__elements
                else None)

    def show(self):
        aux_stack = Stack()
        while self.size() > 0:
            value = self.pop()
            print(value)
            aux_stack.push(value)

        while aux_stack.size() > 0:
            self.push(aux_stack.pop())   

    def __bool__(self):
     return bool(self.__elements)

