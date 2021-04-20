
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
        print(f''' Buenas tardes soy la nutricionista {self.nombre},
        tengo {self.edad} años y curse mis estudios en 
        la univdersidad {self.universidad}.
    ''')

    def indiceMasaCorporal (self, pesoEntrada, alturaEntrada):
        self.peso = pesoEntrada
        self.altura = alturaEntrada
        print(f'''
        ''')

nutricionista = Nutricionista(19, 'Juan', 'CES')


#----------------- Print ----------------------#
print('--------------- nutricionista ---------------')
nutricionista.mostrarAtributos()



