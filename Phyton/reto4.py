'''
Descripción: Usted trabaja en una tienda de libros que recibe diariamente las órdenes de sus pedidos en una lista, que contiene sublistas con la siguiente estructura: [número de pedido, pedidos en una lista, que contiene sublistas con la siguiente estructura: [número de pedido, unidad)], como se muestra a continuación: 

Requerimiento. Se necesita conocer el número de pedido y la cantidad total del mismo. 
Escriba una función que reciba la lista con la orden del día, y devuelva una lista con pares de lista o tuplas con los siguientes datos (número de pedido, cantidad total de pedido), bajo las siguientes condiciones: 
Si el pedido es menor a $1.000.000 de pesos se le debe adicionar a la cantidad total del pedido $30.000 adicionales por concepto de fletes y la pareja de datos debe ser una tupla en caso contrario la pareja de datos es una lista. Recuerde que la cantidad total de pedido debe ser extraída de la lista “orden” y resulta de sumar por cada tupla de un pedido la multiplicación de la cantidad por precio por unidad. 

Entradas: Lista de nombre: orden (Lista que contiene sublistas con la siguiente estructura: [número de pedido, (código del artículo, cantidad, precio por unidad), ... (código del artículo, cantidad, precio por unidad)].)
    * Número de pedido: int  
    * Código del artículo: str 
    * Cantidad: int 
    * Precio por unidad: int 

Salida: Lista (lista con pares de listas o tuplas, donde cada par en forma de lista contiene el número de pedido y el precio total del pedido y cada par en forma de tupla contiene el numero de pedido y el precio total del pedido mas $30.000 adicionales por concepto de fletes.)
    * Número del pedido: int 
    * Precio total; int 

orden = [
    [1,('5464',4,30000),('8274',18,42000),('9744',9,150000)],
    [2,('5464',9,30000),('9744',9,150000)],
    [3,('5464',9,30000),('88112',11,45000)],
    [4,('8732',7,35000),('7733',11,80000),('88112',5,45000)]
]
'''

def facturarTotal(orden):
 
    multiplicacion = [tuple(map(lambda x: x[1]*x[2], (orden[i][1:]))) for i in range(len(orden))]
    
    sumatoria = list(map(sum, multiplicacion))
 
    numpedido = [orden[i][0] for i in range(len(orden))]

    lpedido = list(zip(numpedido, sumatoria))

    Salida = [list(lpedido[i]) if lpedido[i][1] > 1000000 else (lpedido[i][0], lpedido[i][1]+30000) for i in range(len(lpedido))]

    return Salida

print(facturarTotal(orden = [[1,('5464',4,30000),('8274',18,42000),('9744',9,150000)],
    [2,('5464',9,30000),('9744',9,150000)],
    [3,('5464',9,30000),('88112',11,45000)],
    [4,('8732',7,35000),('7733',11,80000),('88112',5,45000)]]))

print(facturarTotal(orden = [[1,("5464",1,30000),("8274",2,42000),("9744",3,150000)],
    [2,("7733",3,80000),("88112",10,45000),("5464",2,30000),("9744",9,150000)],
    [3,("88112",25,45000)],
    [4,("5464",9,30000),("9744",20,150000)],
    [5,("8732",7,35000),("7733",11,80000),("88112",5,45000)]]))
