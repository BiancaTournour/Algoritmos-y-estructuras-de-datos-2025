def usar_la_fuerza(mochila, objetos_sacados=0):

    if not mochila: #ya se sacaron todos los objetos y la mochila quedo "vacia"
        return False, objetos_sacados

    if mochila[0] == "sable de luz":
        return True, objetos_sacados + 1
    else:
        return usar_la_fuerza(mochila[1:], objetos_sacados + 1)

mochila = ["comunicador", "linterna", "provisiones", "capa", "sable de luz"]

encontrado, cantidad = usar_la_fuerza(mochila)

if encontrado:
    print(f"¡Sable de luz encontrado! Se sacaron {cantidad} objetos para hallarlo")
else:
    print("No se encontró el sable de luz en la mochila")