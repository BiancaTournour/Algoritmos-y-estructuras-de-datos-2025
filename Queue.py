from typing import Any, Optional

class Queue:

    def __init__(self):
        self.__elements = []  

    # Agrega un elemento al final de la cola
    def arrive(self, value: Any) -> None:
        self.__elements.append(value)

    # Elimina el primer elemento porque ya le di "atención"
    def attention(self) -> Optional[Any]: 
        return (
            self.__elements.pop(0)
            if self.__elements
            else None
        )

    # Cantidad de elementos de la fila
    def size(self) -> int:
        return len(self.__elements)

    # Devuelve qué elemento está primero en la fila
    def on_front(self) -> Optional[Any]:
        return (
            self.__elements[0]
            if self.__elements
            else None
        )

    # Mueve el primer elemento al final de la cola
    def move_to_end(self) -> Optional[Any]:
        if self.__elements:
            value = self.attention()
            self.arrive(value)
            return value

    # Mostrar cola
    def show(self):
        for i in range(len(self.__elements)):
            print(self.move_to_end())

    # Método __len__ para permitir usar len(self)
    def __len__(self):
        return len(self.__elements)

    # Método __bool__ usando __len__()
    def __bool__(self):
        return len(self) > 0  # Esto ahora llama a __len__ para obtener la longitud
     