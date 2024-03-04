from Fecha import fecha

class Empleado:
    #aqui va el codigo
    '''----------------------------
    #Atributos
    -------------------------------'''

    nombres = ''
    apellidos = ''
    '''--------------------------
     1 = Masculino y 2 = Femenino
     -----------------------------'''
    sexo = 0
    salario = 0

    '''---------------------------
     # Asociaciones
    -------------------------------'''
    fechaNacimiento = fecha()
    fechaIngreso = fecha()

    '''--------------------------
     # Constructor
    -----------------------------'''

    def __init__(self, nombres, apellidos, salario, sexo):
        self.nombres = nombres
        self.apellidos = apellidos
        self.salario = salario
        self.sexo = sexo


    '''----------------------------------------------
    #Metodos 
    ------------------------------------------------'''
    def cambirSalario(self, nSalario) :
        #aqui va el codigo
        self.salario = nSalario
        return "Su nuevo salario es: " + self.salario       

    def ConsultarSalario(self):
        #Aqui va el codigo
        return self.salario    
    
    def AumentoSalario(self):
        #aqui va el codigo
        aumentar = self.salario*0.05
        nSalario = self.salario+aumentar
        self.salario = nSalario
        return "Su nuevo salario es: " + self.salario

    def DuplicarSalario(self):
        #forma 1
        nuevoSalario = self.salario * 2
        self.salario = nuevoSalario

        # forma 2
        # self.salario *= 2


    def CalcularSalarioAnual(self): #calcular el impuesto anual del 19.5 iba 
        # forma 1
        salarioAnual = self.salrio * 12        
        return salarioAnual 

        #forma 2
        # return "Su salario anual es: " + self.salario*12 // comentar lineas cont k + c, contr k + u
    
    def ConsultarDiaCumpleaños(self):
        return self.fechaNacimiento.ConsultarDia() 
    
    def CalcularImpuestos(self):
        # forma 1
        total = self.CalcularSalarioAnual()
        total = total * (19.5/100)
        return total

        #forma 2        
        # return self.CalcularSalarioAnual() * 0.195
    
    # hacer lo siguientes metodos agregar las asociaciones en el caso dos, cuenta bancaria  cosignar cuenta corriente, calcular saldo total 
    # cuenta de ahorro. Cuenta corriente, pasar de ahorros a corriente 


    




