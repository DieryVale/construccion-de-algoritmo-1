class cuentaCorriente:
     #aqui va el codigo

    '''-----------------
    #Atributos 
    --------------------'''
    
    saldo=0

    '''-----------------
    #Metodos 
    ---------------------'''

    def ConsultarSaldo(self):
        # aqui va el codigo 
        return "Su salario actual es: " + self.saldo
    
    def ConsignarMonto(self, monto):
        #forma 1 
        self.saldo += monto
        #forma 2
        #self.saldo = self.saldo + monto

    def RetirarMonto(self, monto):
        #forma 1 
        self.saldo -= monto
        # forma 2
        #self.saldo = self.saldo - monto

        

    '''------------------------------------''' 
    
    # def DepositarValor(self,deposito):
    #     #aqui va el codigo
    #     nSaldo = self.saldo + deposito
    #     self.saldo = nSaldo
    #     return "Usted ha despositado " + deposito
    
    # def RetirarValor(self, retiro):
    #     # aqui va el codigo
    #     nSaldo = self.saldo - retiro
    #     self.saldo = nSaldo
    #     return "Usted ha retirado "+ retiro
    
    # def DuplicarSaldo(self):
    #     # aqui va el codigo
    #     self.nSaldo *= 2 
