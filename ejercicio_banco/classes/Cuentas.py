class Cuentas:
    def __init__(self):
        self.__numeroCuenta = None
        self.__saldo = None
        self.__cedula = None
        
    @property
    def numeroCuenta(self):
        return (self.__numeroCuenta)
    @property
    def saldo(self):
        return (self.__saldo)
    @property
    def cedula(self):
        return (self.__cedula)
            
    @numeroCuenta.setter
    def numeroCuenta(self,numeroCuenta):
        self.__numeroCuenta=numeroCuenta
    @saldo.setter
    def saldo(self,saldo):
        self.__saldo=saldo
    @cedula.setter
    def cedula(self,cedula):
        self.__cedula=cedula