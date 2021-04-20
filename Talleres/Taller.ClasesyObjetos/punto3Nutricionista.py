
# Cree una clase Nutricionista donde tendrá los atributos de edad, 
# nombre, universidad en 
# la que se egresó. Tendrá una función que dado el peso y la altura 
# de un paciente calcule el
# IMC.

class Nutricionista ():
    '''
    edadEntrada: Hace referencia ala edad
    nombreEntrada: Hace referencia al nombre
    universidadEntrada: Hace referencia a la universidaden la que se egresó
    '''

    def __init__(self, edadEntrada, nombreEntrada, universidadEntrada):
        print("Datos por Nutricionista")
        self.edad = edadEntrada
        self.nombre = nombreEntrada
        self.universidad = universidadEntrada 


    def mostrarAtributos (self):
        print(f''' Buenas tardes soy el nutricionista {self.nombre},
        tengo {self.edad} años y curse mis estudios en 
        la univdersidad {self.universidad}.
    ''')

    def masaCorporal (self, pesoEntrada, alturaEntrada):
        self.peso = pesoEntrada
        self.altura = alturaEntrada
        IMC : self.peso / (self.altura**2)
        print(f''' Como tu nutriologo, vericando los datos
        de {self.peso} kg  de peso y {self.altura} m de altura 
        dando como resultado como IMC {IMC}
        ''')



nutricionista = Nutricionista(30, 'Juan', 'CES')



print('--------------- nutricionista ---------------')
nutricionista.mostrarAtributos()
nutricionista.masaCorporal(57, 1.58)




