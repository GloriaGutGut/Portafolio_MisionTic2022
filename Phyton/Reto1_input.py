"""
Un asesor de seguros debe calcular el valor total de los seguros que vende
teniendo en cuenta los siguientes parámetros:
nombre  y apellido del tomador del seguro
valor_asegurado, valor a pagar (15% del valor asegurado)
descuento del mes (5%)
"""

nombre = input("ingrese el nombre del tomador del seguro ")
apellido = input("ingrese el apellido del tomador del seguro ")
nom_apell = nombre + " " + apellido
valor_1 = int(input("ingrese el valor asegurado sin puntos o comas "))
valor_2 = valor_1 * 0.15
descuento = valor_2 * 0.05
total = valor_2 - descuento

print("Reto 1 realizado por: Gloria Beatriz Gutiérrez G. cc43615404")
print ("EMPRESA DE SEGUROS TRANQUILIDAD")
print ("Sólo por éste mes descuento del 5% en el valor de su seguro")
print ("EL TOMADOR DEL SEGURO ES: " + str(nom_apell))
print ("Monto asegurado es: $" + str(valor_1)) 
print ("Valor del seguro antes de aplicar descuento es:  $" +str(valor_2))
print ("Descuento realizado es:  $" +str(descuento))
print ("Valor total a pagar por el seguro es: $" + str(total))
