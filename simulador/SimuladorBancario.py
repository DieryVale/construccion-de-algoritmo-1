from cuentaCorriente import cuentaCorriente
from cuentAhorro import cuentaAhorro
from CDT import CDT

class simuladorBancario:
    
    #aqui va el codigo

    '''-----------------
    Atributos 
    --------------------'''
    cedula = 0
    nombre=''
    mesActual = 0
    VIP = 0
    Platino = 0
    Normal = 0

    '''---------------------
    # Asociaciones
    ------------------------'''
    ahorros = cuentaAhorro()
    corriente = cuentaCorriente()
    cdt = CDT()

    '''------------------------
    # Constructor
    ----------------------------'''
    def __init__(self,cedula, nombre, mesActual, VIP, Platino, Normal):

        self.cedula = cedula
        self.nombre = nombre
        self.mesActual = mesActual
        self.VIP = VIP
        self.Platino = Platino
        self.Normal = Normal


    '''-----------------
    #Metodos
    ------------------'''

    def CalcularSaldoTotal(self):
        # forma 1 
        return self.ahorros.consultarSaldo() + self.corriente.ConsultarSaldo()
        #forma 2 
        # total = self.ahorros.Consultarsaldo() + self.coerriente.ConsultarSaldo()
        # return total
        # forma 3 - forma no recomendada // por vulnerabilidad 
        # total = self.ahorros.saldo + self.corriente.saldo
        # return total

    def ConsignarCuentaCorriente(self, monto):
        self.corriente.ConsignarMonto(monto)
        
    
    def ConsignarCuentaAhorro(self, monto):
        self.ahorros.ConsignarMonto(monto)  

    def TrasferirAhorrosACorriente(self):
        self.ConsignarCuentaCorriente(self.ahorros.ConsultarSaldo())
        self.ahorros.RetirarMonto(self.ahorros.ConsultarSaldo())

    def DuplicarAhorros(self):
        self.ConsignarCuentaAhorro(self.ahorros.ConsultarSaldo())

    def RetirarCuentaCorriente(self, monto):
        self.corriente.RetirarMonto(monto)

    def RetirarCuentaAhorros(self, monto):
        self.ahorros.RetirarMonto(monto)

    def RetirarTodo(self):
        total = self.CalcularSaldoTotal()
        self.TrasferirAhorrosACorriente()
        self.RetirarCuentaCorriente(total)

        return total
    
    def cambiarTipoCliente(self, nuevoTipoClinete):
        self.cliente = nuevoTipoClinete 

    '''--------------------------'''      
    # revisar 
    # def ConsultarSaldoTotalCorriente(self):
    #     SaldoTotalC = self.cuentaCorriente()
    #     return SaldoTotalC
    
    # def PasarDeAhorroCorriente(self):
    #     pasra = self.cuentaAhorro()
    #     pasado = self.cuentaCorriente() 


    # hacer lo siguientes metodos agregar las asociaciones en el caso dos, cuenta bancaria,  cosignar cuenta corriente, calcular saldo total 
    # cuenta de ahorro. Cuenta corriente, pasar de ahorros a corriente 
