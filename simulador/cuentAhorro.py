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
        # aqui va el codigo
        return "Su salario es: "+ self.saldo
    
     def InteresMensual(self):
       #aqui va el codigo
       interes = self.saldo * 0.195
       nSaldo = self.saldo + interes
       self.saldo = nSaldo
       return self.saldo
    
     def DepositarValor(self, retiro):
       # aqui va el codigo
       nSaldo = self.saldo-retiro
       self.saldo < retiro
       return "fondos insuficientes"
