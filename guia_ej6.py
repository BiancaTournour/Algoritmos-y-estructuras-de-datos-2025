from super_heroes_data import superheroes
from List_ import List
class Superhero:
    
    def __init__(self, name, alias, real_name, short_bio, first_appearance, is_villain):
        self.name = name
        self.alias = alias
        self.real_name = real_name
        self.short_bio = short_bio
        self.first_appearance = first_appearance
        self.is_villain = is_villain

    def __str__(self):
        return f"{self.name}, {self.real_name} - {self.is_villain}"

def order_by_name(item):
    return item.name

list_superhero = List()
list_superhero.add_criterion('name', order_by_name)


for superhero in superheroes:
    hero = Superhero(
        name=superhero["name"],
        alias=superhero["alias"],
        real_name=superhero["real_name"],
        short_bio=superhero["short_bio"],
        first_appearance=superhero["first_appearance"],
        is_villain=superhero["is_villain"],
    )
    list_superhero.append(hero)

#eliminar a linterna verde
if list_superhero.search('green lantern', 'name'):
 print(list_superhero.delete_value('green lantern', 'name'))
else:
    print('el personaje linterna verde no se encuentra en la lista')

#año de aparicion de wolverine
index = list_superhero.search('Wolverine', 'name')
if index is not None:
    wolverine = list_superhero.get_element_by_index(index)
    print(f"Wolverine apareció por primera vez en {wolverine.first_appearance}")
else:
    print('Wolverine no se encuentra en la lista')


