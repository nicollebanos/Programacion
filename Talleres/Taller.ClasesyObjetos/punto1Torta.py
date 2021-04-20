
# Cree la clase Torta con atributos forma, sabor, altura, también tendrá una función donde 
# muestre todos sus atributos.

class Torta ():
    '''Reposteria de confianza y de las mejores que podras encontra
    en la ciudad, brindamos la mejor calidad para nuestros
    clientes. Cada torta es unica por lo que tendrian los 
    siguentes atributos:

    formaEntrada: Hace referencia a la forma de la torta
    saborEntrada: Hace referencia al sabor de la torta
    alturaEntrada: Hace referencia a la altura de la torta
    '''

    def __init__(self,formaEntrada, saborEntrada, alturaEntrada):
        print("Las mejores tortas de la ciudad")
        self.forma = formaEntrada
        self.sabor = saborEntrada
        self.altura = alturaEntrada

    def mostrarAtributos (self):
        print(f''' Hola, somos una reposteria unica que vende tortas 
        extraordinarias. Tu pedido de forma {self.forma}, sabor {self.sabor} 
        y de {self.altura} de altura ha sido recibido con exito. 
        El envio sera aproximadamente en una a dos semana. 
        Gracias por confiar en nosotros
    ''')

torta1 = Torta('circular', 'vainilla', 'dos pisos')
torta2 = Torta('cuadrada', 'chocolate','cuatro pisos')
torta3 = Torta('circular', 'red velvet', 'un piso')

#----------------- Print ----------------------#
print('--------------- Torta 1 ---------------')
torta1.mostrarAtributos()

print('--------------- Torta 2 ---------------')
torta2.mostrarAtributos()

print('--------------- Torta 3 ---------------')
torta3.mostrarAtributos()

