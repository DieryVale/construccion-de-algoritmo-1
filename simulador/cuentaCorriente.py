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
    
    def DepositarValor(self,deposito):
        #aqui va el codigo
        nSaldo = self.saldo + deposito
        self.saldo = nSaldo
        return "Usted ha despositado " + deposito
    
    def RetirarValor(self, retiro):
        # aqui va el codigo
        nSaldo = self.saldo - retiro
        self.saldo = nSaldo
        return "Usted ha retirado "+ retiro
