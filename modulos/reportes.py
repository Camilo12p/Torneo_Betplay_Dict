def masGoles(equipos:dict):
    masgoles=equipos[1]['gf']
    
    for key,value in equipos.items():
        if value['gf']>=masgoles:
            masgoles=value['gf']
            maxgoles=value['nombre']  
            

    print('maximo goleador')
    print(f'{maxgoles} con {masgoles}')  
            
def masPuntos(equipos:dict):
    maspuntos=equipos[1]['tp']
    print(maspuntos)
    for key,value in equipos.items():
        if value['tp']>=maspuntos:
            maspuntos=value['tp']
            maxpuntos=value['nombre']  
            
    print('maximo de puntos')
    print(f'{maxpuntos} con {maspuntos}') 
    
    
def masGanados(equipos:dict):
    masganados=equipos[1]['pg']
    print(masganados)
    for key,value in equipos.items():
        if value['pg']>=masganados:
            masganados=value['pg']
            maxganados=value['nombre']  
    print('Mas partidos ganados')
    print(f'{maxganados} con {masganados}') 
    
def totalGoles(equipos:dict,op=1):
    totalgoles=0
    
    for key,value in equipos.items():
        totalgoles+=value['gf']
              
    if(op==1):      
        print('Total de goles ')
        print(f'{totalgoles} ') 
    return totalgoles

def promedioGoles(equipos:dict,fechas:dict):
    totalgoles=totalGoles(equipos,2)
    partidos=0
    for key,values in fechas.items():
        partidos+=len(values)
    
    promedio=totalgoles/partidos

    print('Promedio de gol por partido')
    print(f'{promedio} ') 
