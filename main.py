import modulos.menu as m
import modulos.fechas as f

import os

validar=True
torneo={
    # 1:{
    # 'nombre':'A',
    # 'pj':2,
    # 'pg':1,
    # 'pp':0,
    # 'pe':1,
    # 'gf':3,
    # 'gc':0,
    # 'tp':4
    # },
    # 2:{
    # 'nombre':'B',
    # 'pj':2,
    # 'pg':0,
    # 'pp':1,
    # 'pe':1,
    # 'gf':0,
    # 'gc':3,
    # 'tp':1
    # }
}
fechas={
    1:{},
    2:{},
    3:{},
    4:{},
    5:{},
    6:{},
    7:{},
    8:{},
    9:{},
    10:{},
    11:{},
    12:{}
}

while validar:
    try:
        op= m.Principal()
       
        if op==1:
            m.opcion1(torneo)
            os.system('pause')  
        elif op==2:
            m.registrarFecha()
            f.definirFechas(fechas,torneo)
            os.system('pause')
            pass
        elif op==3:
            m.reportes(torneo,fechas)
            os.system('pause')
            pass
        elif op==4: 
            validar=False
            os.system('pause')
        else:
            print('ingresa un valor valido')
            os.system('pause')
    except ValueError:
        print('ingresa un valor valido')
        os.system('pause')
