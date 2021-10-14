'''
Escriba una función que reciba una lista con el código del cliente y una tupla, la cual esta formada por un sistema electrónico de control, el cual envía un código binario indicando que sensores están activos y los que no. Un ejemplo es: [020008,(1,0,0,1,0)], esta estructura indica que el cliente con código 020008, tiene activos sensores 1 y 4. La función debe retornar una lista que contenga los clientes que tienen sensores activos, lo cual indica
un estado de alarma y se necesita que los guardias de seguridad se dirijan al lugar. Por lo
tanto, la lista de salida debe contener diccionarios con los siguientes datos: código del cliente, dirección del cliente, cuantos agentes deben dirigirse al lugar. Este último dato depende de la zona donde se encuentre la locación: zona 1 = 3 guardias de seguridad y zonas 2 y 3 = 2 guardias de seguridad.

[{'codigo':'010010','nom':'Juan Pérez','dir':'cr 30 25 80','zona':1,'sensores':7},
{'codigo':'020008','nom':'Carolina Charris','dir':'cr 84 70 27 Bod 4','zona':2,'sensores':5},
{'codigo':'030011','nom':'Juan Pérez','dir':'cr 30 10 80','zona':3,'sensores':5},
{'codigo':'020114','nom':'Omar Acosta','dir':'cr 30 25 80','zona':2,'sensores':5},
{'codigo':'020115','nom':'Camilo Fernández','dir':'cr 30 25 80','zona':2,'sensores':5},
{'codigo':'010020','nom':'Juan Pérez','dir':'cr 30 15 80','zona':1,'sensores':8}]
'''

entrada = [{'codigo_cliente':'010010','dirección':'cr 30 25 80','cantidad_guardias':'3 guardias','sensores':7,'sensores_activos':int},
{'codigo_cliente':'020008','dirección':'cr 84 70 27 Bod 4','cantidad_guardias':'2 guardias','sensores':5,'sensores_activos':int},
{'codigo_cliente':'030011','dirección':'cr 30 10 80','cantidad_guardias':'2 guardias','sensores':5,'sensores_activos':int},
{'codigo_cliente':'020114','dirección':'cr 30 25 80','cantidad_guardias':'2 guardias','sensores':5,'sensores_activos':int},
{'codigo_cliente':'020115','dirección':'cr 30 25 80','cantidad_guardias':'2 guardias','sensores':5,'sensores_activos':int},
{'codigo_cliente':'010020','dirección':'cr 30 15 80','cantidad_guardias':'3 guardias','sensores':8,'sensores_activos':int}]

exit = {}
Salida = [{}]

def monitoreo(codigo:str,sensores:tuple)->list:
    for C in entrada:
        if C['codigo_cliente'] == codigo:
            exit = C['codigo_cliente'],['dirección'],['cantidad_guardias'],['sensores_activos']
            if 1 not in sensores:
                Salida = [{}]
            else:
                if sensores.count(1) >= 1:
                    exit['sensores_activos'] = sensores.count(1)
                    if len(sensores) == C['sensores']:
                        exit.append["'estado_sensores': 'correcto'"]
                    else:
                        exit.append["'estado_sensores': 'revisar'"]
                Salida = list{exit.items()}         #ERROR syntax
    return Salida

print(monitoreo('020114',(0,0,1,0,0)))
print(monitoreo('010010',(0,0,0,0,0)))
