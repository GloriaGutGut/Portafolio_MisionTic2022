def funcion1(ruta_archivo:str, opcion:int)->dict:
    import pandas as pd
    
    df = pd.read_csv(ruta_archivo,names=["id_voluntario","nombre","codigo_playa","peso_recolectado"])
    if opcion == 1:
        rta = df.groupby(["codigo_playa"])["id_voluntario"].size()
        resultado = rta.to_dict()
    elif opcion == 2:
        rta = df.groupby(["codigo_playa"])["peso_recolectado"].sum()
        resultado = rta.to_dict()    
    elif opcion == 3:
        rta = df["peso_recolectado"].max()
        resultado = {"Máximo recolectado en una playa": rta}
    elif opcion == 4:
        rta = df["peso_recolectado"].sum()
        resultado = {"Total recolectado": rta}
    elif opcion == 5:
        rta = df["id_voluntario"].count()
        resultado = {"Total voluntarios": rta}
        
    return(resultado)
print(funcion1('https://raw.githubusercontent.com/marinacharris/retos/main/Voluntarios.csv',1))
print(funcion1('https://raw.githubusercontent.com/marinacharris/retos/main/Voluntarios.csv',2))
print(funcion1('https://raw.githubusercontent.com/marinacharris/retos/main/Voluntarios.csv',3))
print(funcion1('https://raw.githubusercontent.com/marinacharris/retos/main/Voluntarios.csv',4))
print(funcion1('https://raw.githubusercontent.com/marinacharris/retos/main/Voluntarios.csv',5))
