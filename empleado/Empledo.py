from Fecha import fecha

class Empleado:
    #aqui va el codigo
    '''----------------------------
    # Atributos
    -------------------------------'''

    nombres = ''
    apellidos = ''
    salario = 0
    sexo = 0
    hijos = 0 

    '''--------------------------
     1 = Masculino y 2 = Femenino
     -----------------------------'''
   

    '''---------------------------
     # Asociaciones
    -------------------------------'''
    fechaNacimiento = fecha()
    fechaIngreso = fecha()

    '''--------------------------
     # Constructor
    -----------------------------'''

    def __init__(self, nombres, apellidos, salario, sexo, hijos):
        self.nombres = nombres
        self.apellidos = apellidos
        self.salario = salario
        self.sexo = sexo
        self.hijos = hijos


    '''----------------------------------------------
    #Metodos 
    ------------------------------------------------'''
    def cambirSalario(self, nSalario) :
        #aqui va el codigo
        self.salario = nSalario
        return "Su nuevo salario es: " + self.salario

    def CambiarEmpleado(self, nNombre, nApellido, nSexo, nSalario):
        # Aqui va el codigo del nuevo empleado
        return None       

    def ConsultarSalario(self):
        #Aqui va el codigo del metodo
        return self.salario

    def ConsultarNombre(self):
        return self.nombres    
    
    def ConsultarApellido(self):
        return self.apellidos
    
    def ConsultarNombreCompleto(self):
        return self.nombres + ' '+ self.apellidos
    
    def ConsultarCuantosHijos(self):
        return self.hijos
    
    def AumentoSalario(self):
        #aqui va el codigo
        aumentar = self.salario*0.05
        nSalario = self.salario+aumentar
        self.salario = nSalario
        return "Su nuevo salario es: " + self.salario
    
    def Cambiarnombre(self, nNombre):
        self.nombres = nNombre
        return "El nuevo nombre es: "+ self.nombres
    
    def CambiarApellido(self, nApellido):
        self.apellidos = nApellido
        return "El nuevo apellido es: "+ self.apellidos

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
    
    def AuxilioEmpleadoPorHijos(self, hijos):
        self.salario += hijos * 0.05

    def diferenciaSalarial(self, otroEmpleado):
        return abs(self.salario - otroEmpleado.salario) # abs devuelve el valor absoluto de un numero  eje abs(-5) devuelve 5

    
    # hacer lo siguientes metodos agregar las asociaciones en el caso dos, cuenta bancaria  cosignar cuenta corriente, calcular saldo total 
    # cuenta de ahorro. Cuenta corriente, pasar de ahorros a corriente 


    




