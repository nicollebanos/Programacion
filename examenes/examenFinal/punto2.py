
# Cree una clase humano con atributos nombre, sexo, edad y con la acción 
# hablar donde dado un mensaje se mostrará en pantalla. Luego cree una clase Doctor que 
# herede de humano y tenga la acción adicional de que dado una estatura y un peso calcule el 
# IMC y lo muestre en pantalla

class Humano ():
    '''
    nombreEntrada: Hace referencia al nombre del ususario
    sexoEntrada: hace referencia al sexo del usuario
    edadEntrada: hace referencia al sexo del usuario
    hablar (accion)
    '''

    def __init__(self, nombreEntrada, sexoEntrada, edadEntrada):
        print("Datos usuario")
        self.nombre = nombreEntrada
        self.sexo = sexoEntrada
        self.edad = edadEntrada


    def mostrarAtributos (self):
        print(f''' Buenas, mi nombre es {self.nombre},
        tengo {self.edad} años y soy una {self.sexo} teoricamente
        sana. Muchas gracias por la atención prestada. 
    ''')

    def hablar (self):
        print(f''' Yo {self.nombre} me considero un(a)
        {self.sexo} muy amable hasta que sobre pasan
        los limites conmigo. 
    ''')

humano = Humano('Andrea', 'mujer', '19')
humano.mostrarAtributos()

class Doctor(Humano):
    def calcularIMC(self,nombreDoctor):
        print(f'''Hola señora {self.nombre}, mi nombre es
        {nombreDoctor} y el día de hoy soy el encargado para
        calcular su IMC, por lo cual me digilenciara los
        siguentes datos.
    ''')

    def masaCorporal (self, pesoEntrada, alturaEntrada):
        self.peso = pesoEntrada
        self.altura = alturaEntrada
        imc = self.peso / (self.altura**2)
        print(f''' Como tu doctor encargado, teniendo presente que
        pesas {self.peso} kg y mides {self.altura} m...
        Tú IMC es de... {imc}
        ''')

doctor = Doctor('Andrés')
doctor.mostrarAtributos
doctor.calcularIMC(humano.nombre)
doctor.masaCorporal(58, 1.64)






