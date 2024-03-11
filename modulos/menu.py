import modulos.equipos as e
import modulos.reportes as r
import os

def Principal()->int:
    titulo='''
        ++++++++++++++++++++++++++++++
        +     Liga betplay 2024      +
        ++++++++++++++++++++++++++++++
    '''

    os.system('cls')

    opciones=['1.Agregar/Borar equipo\n2.Agregar Fecha\n3.Reportes\n4.Salir\n']
    print(titulo)
    for i in opciones:
        print(i)
    op=int(input('Elige una opcion: ')) 

    return op   

def opcion1(torneo:dict):
    titulo='''
        ++++++++++++++++++++++++++++++++++++
        +  Modificador de equipos betplay  +
        ++++++++++++++++++++++++++++++++++++
    '''
    
   
    
    validar1=True
    while validar1:
       
        os.system('cls')
        print(titulo)
        print('1.Agregar Equipo\n2.Borrar Equipo\n3.Salir\n')
        op= int(input('Elige una opcion: '))
        if op==1:
            e.agregarEquipos(torneo)
        elif op==2:
            e.eliminarEquipo(torneo)
        elif op==3:
            validar1=False
        else:
            print('ingresa un valor valido')
      

def registrarFecha():
    titulo='''
            +++++++++++++++++++++
            +  Registrar fecha  +
            +++++++++++++++++++++
    '''
    os.system('cls')
    print(titulo)


def reportes(equipos:dict,fechas:dict):
    titulo= """
            +++++++++++++++++++++++++++++++++++++++
            +         REPORTES DEL TORNEO         +
            +++++++++++++++++++++++++++++++++++++++
            
    A. Nombre del equipo que más goles anotó
    B. Nombre del equipo que más puntos tiene
    C. Nombre del equipo que más partidos ganó
    D. Total de goles anotados por todos los equipos
    E. Promedio de goles anotados en el torneo
    F. Regresar al menú principal
    """
    os.system('cls')
    
    validar=True
    while validar:
        

        print(titulo)

        op=input('selecciona una opcion: ').upper()
               
        if op=='A':
            r.masGoles(equipos)
            os.system('pause')
        elif op=='B':
            r.masPuntos(equipos)
            os.system('pause')
        elif op=='C':
            r.masGanados(equipos)
            os.system('pause')
        elif op=='D':
            r.totalGoles(equipos)
            os.system('pause')
        elif op=='E':
            r.promedioGoles(equipos,fechas)
            os.system('pause')
        elif op=='F':
            validar=False
            os.system('pause')
        else:
            print('Selecciona la respuesta correcta')
            os.system('pause')
