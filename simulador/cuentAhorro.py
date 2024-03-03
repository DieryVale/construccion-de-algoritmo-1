class cuentaAhorro:
     #aqui va el codigo

     '''-----------------
    Atributos 
     --------------------'''
     saldo = 0
     interesMensual = 0

     '''-----------------
     # metodos 
     --------------------'''
     def ConsultarSaldo(self):
        return self.saldo
     
     def ConsultarInteresMensual(self):
        return self.interesMensual
     
     def ConsignarMonto(self, monto):
        #forma 1
        self.saldo += monto
        #forma 2
        # self.saldo = self.saldo + monto

     def RetirarMonto(self, monto):
        #forma 1
        self.saldo -= monto
        #forma 2 
        # self.saldo = self.saldo - monto


     

