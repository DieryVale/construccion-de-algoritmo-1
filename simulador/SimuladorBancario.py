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

    def consignarValor(self, cValor):
        #aqui va el codigo
        self.valor = cValor
        return "El valor consignado es: " + self.valor


    def consultarSaldo(self):
        #aqui va el codigo
        return "Su saldo es: " + self.saldo



    def retirarValor(self):
        #aqui va el codigo
        return "El valor retirado es: " + self.retirar


    def consultarInteresMensual(self):
        #aqui va el codigo
        return "Los interes mensuales son: " + self.conInteres