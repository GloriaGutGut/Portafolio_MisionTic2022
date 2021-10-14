"""
Un asesor de seguros debe calcular el valor total de los seguros que vende
teniendo en cuenta los siguientes parámetros:
nombre  y apellido del tomador del seguro
valor_asegurado, valor a pagar (15% del valor asegurado)
descuento del mes (5%)
"""

def calcular_seguro(nombre: str, apellido: str, valor_asegurado: int, descuento: int):
    nombre = nombre
    apellido = apellido
    valor_seguro = int(valor_asegurado * 0.15)
    valor_descuento = int(valor_seguro * descuento)/100
    valor_total = valor_seguro - valor_descuento
    return f"El valor del seguro de {nombre} {apellido} es: {valor_total}, el descuento realizado fue: {valor_descuento}"

print(calcular_seguro("Pedro","Díaz",10000000,5))