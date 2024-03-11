import os


def agregarEquipos(torneo:dict):
    
    nombre=input('ingrese el nombre del equipo a agregar: ').capitalize()
    equipo={
        'nombre':nombre,
        'pj':0,
        'pg':0,
        'pp':0,
        'pe':0,
        'gf':0,
        'gc':0,
        'tp':0
     }
    torneo.update({len(torneo)+1:equipo})

    op=bool(input("Desea añadir otro equipor:\nPresiona S para si\nPresiona ENTER para no\n"))
    if(op==True):
        agregarEquipos(torneo)


def eliminarEquipo(torneo:dict):
    nombre=input('Ingrese el nombre del equipo a eliminar: ').capitalize()
    for key, value in torneo.items():
        if nombre in value['nombre']:
            torneo.pop(key)
            break