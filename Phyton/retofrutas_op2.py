"""
Crea un diccionario que contenga los precios por kilo de 4 frutas.
El programa debe preguntar al usuario que fruta desea y cuantos kilos necesita.
Cree una función que devuelva el precio que debe pagar el usuario.
Si la fruta no está en el diccionario debe mostrar el mensaje que no hay existencias de la fruta.
"""

frutas = {
    'chirimoya' : 5000,
    'mangostino' : 2000,
    'banano' : 200,
    'piña' : 1500
}
def fruteria(fruta: str, cantidad: int):
    if (fruta in frutas):
        precio = int(cantidad) * frutas[fruta]
        return f"Son {precio}"
    else:
        return f"No hay existencia de esa fruta"


print(fruteria(input('Qué fruta desea? '), input('Cuántas quiere?')))

