from cuentaCorriente import cuentaCorriente
from cuentAhorro import cuentAhorro

class simuladorBancario:
    
    #aqui va el codigo

    '''-----------------
    Atributos 
    --------------------'''
    cedula = 0
    nombre=''
    ingresAct = 0
    valor = 0

    '''-----------------
    #Metodos
    ------------------'''

     def ConsignarCuentaCorriente(self):
        cosignar = self.cuentaCorriente()
        return cosignar
    
    def ConsultarSaldoTotalAhorro(self):
        SaldoTotalA = self.cuentaAhorro()
        return SaldoTotalA
    
    def ConsultarSaldoTotalCorriente(self):
        SaldoTotalC = self.cuentaCorriente()
        return SaldoTotalC
    
    def PasarDeAhorroCorriente(self):
        pasra = self.cuentaAhorro()
        pasado = self.cuentaCorriente() 
    # hacer lo siguientes metodos agregar las asociaciones en el caso dos, cuenta bancaria,  cosignar cuenta corriente, calcular saldo total 
    # cuenta de ahorro. Cuenta corriente, pasar de ahorros a corriente 
