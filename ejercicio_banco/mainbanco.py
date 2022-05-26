from classes.Clientes import Clientes
from classes.Cuentas import Cuentas

cliente=Clientes()
cuenta=Cuentas()

opcion=-1
clientes=[]
cuentas=[]
while(opcion!=0):
    print("**********")
    print("Digitar 1 para registrar un Cliente")
    print("Digitar 2 para registrar una Cuenta")
    print("Digitar 3 para consultar saldo de una cuenta")
    print("Digitar 4 para ingresar dinero a una cuenta")
    print("Digitar 5 para retirar dinero de una cuenta")
    print("Digitar 0 para cerrar programa")
    print("**********")
    opcion = int(input("Digite una opción: "))
    if(opcion==1):
        cliente = {}        
        cliente['nombre'] = input("Digita el nombre del cliente: ")
        cliente['apellido'] = input("Digita el apellido del cliente: ")
        cliente['cedula'] = int(input("Digita la cedula del cliente: "))
        cliente['ciudad'] = input("Digita la ciudad del cliente: ")
        clientes.append(cliente)
    elif(opcion==2):
        cuenta={}
        cedula = int(input("Ingrese la cedula del cliente, para registar cuenta: "))
        for cliente in clientes:
            if cedula == cliente['cedula']:
                cuenta['numeroCuenta'] = int(input("Digite numero de cuenta a asignar: "))
                cuenta['saldo'] = int(input("ingrese saldo inicial: "))
                cuenta['cedula'] = cedula
                cuentas.append(cuenta)
            else:
                print("Cliente no registrado, no se puede asignar cuenta")
    elif(opcion==3):
        cuentaConsultada = int(input("Ingrese la cuenta a consultar: "))
        for cuenta in cuentas:
            if cuentaConsultada == cuenta['numeroCuenta']:
                saldoCuenta = cuenta['saldo']
                print("El saldo es: ")
                print(saldoCuenta)
            else:
                print("Cuenta no registrada")
    elif(opcion==4):
        cuentaIngresarDinero = int(input("Ingrese la cuenta a ingresar dinero: "))
        for cuenta in cuentas:
            if cuentaIngresarDinero == cuenta['numeroCuenta']:
                ingresarDinero = int(input("Digite dinero a ingresar: "))                
                cuenta['saldo'] = cuenta['saldo'] + ingresarDinero
                saldoCuenta = cuenta['saldo']
                print("El nuevo saldo es: ")
                print(saldoCuenta)
            else:
                print("Cuenta no registrada")
    elif(opcion==5):
        cuentaRetirarDinero = int(input("Ingrese la cuenta a retirar dinero: "))
        for cuenta in cuentas:
            if cuentaRetirarDinero == cuenta['numeroCuenta']:
                retirarDinero = int(input("Digite dinero a retirar: "))                
                cuenta['saldo'] = cuenta['saldo'] - retirarDinero
                saldoCuenta = cuenta['saldo']
                print("El nuevo saldo es: ")
                print(saldoCuenta)
            else:
                print("Cuenta no registrada")
    elif(opcion==0):
        print("Ha cerrado satisfactoriamente el programa")
        break