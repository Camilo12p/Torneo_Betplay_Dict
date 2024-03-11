def definirFechas(fechas:dict,equipos:dict,contador=1):
    idx=1
    partido={
        
    }
    for key,value in equipos.items():
        print(f'{idx}.',value['nombre'])
        idx+=1
    
    for i in range(1,3):
        if i==1:
            local=int(input('ingrese el equipo local: '))
            golesL=int(input('Cuantos goles marco?: '))
        else:
            visitante=int(input('ingrese el equipo visitante: '))
            golesv=int(input('Cuantos goles marco?: '))

    partido.update({'local':equipos[local]['nombre'],'golesL':golesL,'visitante':equipos[visitante]['nombre'],'golesv':golesv})
            
    fechaday=int(input('Que fecha se esta jugando: '))
    fechas[fechaday].update({contador:partido})
#    equipo={
#         'nombre':nombre,
#         'pj':0,
#         'pg':0,
#         'pp':0,
#         'pe':0,
#         'gf':0,
#         'gc':0,
#         'tp':0
#      }
    if golesL>golesv:
        equipos[local]['pg']+=1
        equipos[local]['tp']+=3
        equipos[visitante]['pp']+=1
        
        
    elif golesL<golesv:
        equipos[local]['pp']+=1
        equipos[visitante]['pg']+=1
        equipos[visitante]['tp']+=3
        
    elif golesL==golesv:
        equipos[local]['pe']+=1
        equipos[visitante]['pe']+=1
        equipos[local]['tp']+=1
        equipos[visitante]['tp']+=1
        
    equipos[local]['gf']+=golesL
    equipos[local]['gc']+=golesv
    equipos[local]['pj']+=1

    equipos[visitante]['gf']+=golesv
    equipos[visitante]['gc']+=golesL
    equipos[visitante]['pj']+=1
    
    contador+=1
    if contador<=len(equipos)/2:
        definirFechas(fechas,equipos,contador)
    
    
    
        
