"""
Descripción.\n
 Una empresa de seguridad maneja una lista con los datos de los sistemas de seguridad\n
  que tiene instalados en locaciones de la ciudad.\n
 Además, tiene otra lista con los datos personales de los clientes con se muestra a continuación:
"""
datos = [
{'codigo': '010010','nom': 'Juan Pérez','dir': 'cr 30 25 80','zona': 1, 'sensores': 7},
{'codigo': '020008','nom': 'Carolina Charris','dir': 'cr 84 70 27 Bod 4','zona': 2,'sensores': 5},
{'codigo': '030011','nom': 'Jorge Rios','dir': 'cr 30 25 80','zona': 3,'sensores': 5},
{'codigo': '020114','nom': 'Omar Acosta','dir': 'cr 30 25 80','zona': 2,'sensores': 5},
{'codigo': '020115','nom': 'Camilo Fernández','dir': 'cr 30 25 80','zona': 2,'sensores': 5},
{'codigo': '010020','nom': 'Juan Pérez','dir': 'cr 30 25 80','zona': 1,'sensores': 8}]

nuevalista = []
nuevodict = {}
def monitoreo(codigo:str,sensores:tuple)->list:
    #averiguar la cantidad de sensores prendidos (1) en el parámetro.
    cant_sens_activ = sensores.count(1)
    if cant_sens_activ == 0:
        nuevodict = {}     
    else:
        for i in range(0, len(datos)):
            if codigo==datos[i]['codigo']:  #si codigo del parametro está en diccionario
                direcc = datos[i]['dir']
                cantsensor = datos[i]['sensores']  #captura cantidad de sensores
                if cantsensor==len(sensores):          #si cantidad de sensores del parametro=    
                    estsensor="correcto"               #cant sensores en diccionario 
                else:
                    estsensor="revisar"
                # averiguar la zona a la que pertenece el cliente\n
                # para definir la cantidad de guardias.   
                zona = datos[i]['zona']
                if zona == 1:
                    guardias = 3
                else:
                    guardias = 2
            
            
                nuevodict = {'codigo_cliente': codigo, 'direccion': direcc, 'cantidad_guardias': f"{guardias} guardias" , 'sensores_activos': cant_sens_activ, 'estado_sensores': estsensor}
    nuevalista.append(nuevodict)
    return nuevalista            
print(monitoreo('020115',(0,0,0,0,0)))           
print(monitoreo('020008',(1,0,1,0,0,0,0)))
