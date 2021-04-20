
# Piense en su instrumento musical favorito y cree una clase 
# asociada al mismo, defina los 
# atributos y cree una función que permita dada una canción 
# interpretarla en el mismo

class Violin ():
    ''' 
    colorEntrada: hace referencia al color del violin
    marcaEntrada: hace referencia a la marca del violin
    tamañoEntrada: hace referencia al tamaño del violin 
    Acción:
    *tocar(accion):
        Interpretación musical 
    '''

    def __init__(self,colorEntrada, marcaEntrada, tamañoEntrada):
        print("Datos sobre violines")
        self.color = colorEntrada
        self.marca = marcaEntrada
        self.tamaño = tamañoEntrada

    def mostrarAtributos (self):
        print(f''' Hacemos entrega del violin de color {self.color}, 
        marca {self.marca} y de tamaño {self.tamaño} a nuestro más fiel
        cliente. Disfrutelo
    ''')


    def tocar (self, cancion):
        print(f''' El compositor esta tocando con el violin
        la canción {cancion}
    ''')




violin1 = Violin('marrón', 'Gewa', '1/2')
violin2 = Violin('blanco', 'Stentor', '3/4')
violin3 = Violin('negro', 'Gliga', '4/4')




print('--------------- Violin 1 ---------------')
violin1.mostrarAtributos()
violin1.tocar('Perfect')

print('--------------- Violin 2 ---------------')
violin2.mostrarAtributos()
violin2.tocar('Crystallize')

print('--------------- Violin 3 ---------------')
violin3.mostrarAtributos()
violin3.tocar('A thousand years')
