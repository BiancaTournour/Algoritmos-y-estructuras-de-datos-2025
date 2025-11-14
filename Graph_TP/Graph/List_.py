#python ya cuenta con funciones para listas, agregaremos las que no estan definidas
from typing import Any
from typing import Optional

class List(list):#heredar los metodos de la clase lista de python (List)

    CRITERION_FUNCTIONS = {}

    def __init__(self, iterable=None):
        super().__init__(iterable or [])

    def add_criterion(self, key_criterion: str, function,):
        self.CRITERION_FUNCTIONS[key_criterion] = function

    def show(self) -> None:
        for element in self:
            print(element)

    def delete_value(self, value, key_value: str = None,) -> Optional[Any]:
        index = self.search(value, key_value)
        return self.pop(index) if index is not None else index

    def sort_by_criterion(self, criterion_key: str = None,) -> None:
        criterion = self.CRITERION_FUNCTIONS.get(criterion_key)

        if criterion is not None:
            self.sort(key=criterion)
        elif self and  isinstance(self[0], (int, str, bool)):
            self.sort()
        else:
            print('criterio de orden no encontrado')

    def search(self, search_value, search_key: str = None,) -> int:
        self.sort_by_criterion(search_key)
        start = 0
        end = len(self) -1
        middle = (start + end) // 2

        while start <= end:
            criterion = self.CRITERION_FUNCTIONS.get(search_key)
            if criterion is None and self and not isinstance(self[0], (int, str, bool)):
                return None

            value = criterion(self[middle]) if criterion else self[middle]
            if value == search_value:
                return middle
            elif value  < search_value:
                start = middle +1
            else:
                end = middle -1
            middle = (start + end) // 2

    def get_element_by_index(self, index: int) -> Optional[Any]:
     if 0 <= index < len(self):
        return self[index]
     return None


#.append agregar al final
#.insert agregar en una posicion deseada
#.sort ordena
#.pop elimina un elemento y lo devuelve (el ultimo o el parametro que le pasemos)
#.remove elimina un elemento indicado (se le indica el value, no posicion)

