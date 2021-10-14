"""
Crea un diccionario que contenga los precios por kilo de 4 frutas.
El programa debe preguntar al usuario que fruta desea y cuantos kilos necesita.
Cree una función que devuelva el precio que debe pagar el usuario.
Si la fruta no está en el diccionario debe mostrar el mensaje que no hay existencias de la fruta.
"""

fruta = input('Ingrese la fruta que desea: ')
kilos = input('Cuántos kilos necesita: ')


def precio_fruta(fruta: str, kilos: int):
    frutas = dict(manzana=5000, banana=2500, lulo=4000, pera=5800)

    if (fruta in frutas):
        print(frutas[fruta])
        precioTotal = int(frutas[fruta])*int(kilos)
        #return f"El precio total de {kilos} kilos de {fruta} es de {precioTotal}"
        return "El precio total de {} kilos de {} es de {}".format(kilos,fruta,precioTotal)
    else:
        return f"No contamos con {fruta} en el inventario"


print(precio_fruta(fruta, kilos))
