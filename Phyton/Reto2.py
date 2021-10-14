datos_tanque = {
    'codigo': str,
    'sensor1': bool,
    'sensor2': bool, 
    'sensor3': bool
}

def estado_nivel(datos_tanque: dict)->dict:
    if (datos_tanque['sensor1'] == False and datos_tanque['sensor2'] == False and datos_tanque['sensor3'] == False):
        level = 'vacío'
    elif (datos_tanque['sensor1'] == True and datos_tanque['sensor2'] == False and datos_tanque['sensor3'] == False):
        level = 'nivel bajo'
    elif (datos_tanque['sensor1'] == True and datos_tanque['sensor2'] == True and datos_tanque['sensor3'] == False):
        level = 'nivel medio'
    elif (datos_tanque['sensor1'] == True and datos_tanque['sensor2'] == True and datos_tanque['sensor3'] == True):
        level = 'nivel alto'
    else:
        level = 'revisar sensores'
      
    dicSalida = {
        'codigoTanque': datos_tanque['codigo'],
        'nivel': level
    }
  
    return f"Estado del nivel del líquido del tanque {dicSalida['codigoTanque']}: {dicSalida['nivel']}"

print(estado_nivel(dict(codigo = "TA001", sensor1 = False, sensor2 = False, sensor3 = False)))
print(estado_nivel(dict(codigo = "TA001", sensor1 = True, sensor2 = False, sensor3 = False)))
print(estado_nivel(dict(codigo = "TA001", sensor1 = True, sensor2 = True, sensor3 = False)))
print(estado_nivel(dict(codigo = "TA001", sensor1 = True, sensor2 = True, sensor3 = True)))
print(estado_nivel(dict(codigo = "TA001", sensor1 = True, sensor2 = False, sensor3 = True)))
print(estado_nivel(dict(codigo = "TA001", sensor1 = False, sensor2 = False, sensor3 = True)))
print(estado_nivel(dict(codigo = "TA001", sensor1 = False, sensor2 = True, sensor3 = True)))
print(estado_nivel(dict(codigo = "TA001", sensor1 = False, sensor2 = True, sensor3 = False)))
