from classes.Ciclista import Ciclista

ciclista=Ciclista()

opcion=-1
ciclistas=[]
while(opcion!=0):
    print("**********")
    print("Digitar 1 para registrar un ciclista")
    print("Digitar 2 para mostrar ciclista con mejor tiempo")
    print("Digitar 0 para cerrar programa")
    print("**********")
    opcion = int(input("Digite una opción: "))
    if(opcion==1):
        ciclista = {}        
        ciclista['nombre'] = input("Digita el nombre del ciclista: ")
        ciclista['edad'] = int(input("Digita la edad del ciclista: "))
        ciclista['pais'] = input("Digita el pais del ciclista: ")
        ciclista['equipo'] = input("Digita el equipo del ciclista: ")
        ciclista['tiempo'] = int(input("Digita el tiempo en minutos del ciclista: "))
        ciclistas.append(ciclista)
    elif(opcion==2):
        mejorTiempo = 999999999999
        mejorCiclista={}
        for ciclista in ciclistas:
            if mejorTiempo > ciclista['tiempo']:
                mejorTiempo = ciclista['tiempo']                
                mejorCiclista = ciclista
        print("Los datos del ciclista con el mejor tiempo son:")
        print(mejorCiclista)
    elif(opcion==0):
        print("Ha cerrado satisfactoriamente el programa")
        break