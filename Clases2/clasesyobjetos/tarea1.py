
class Perro ():
    '''Es un mamífero domestico carnívoro de la familia de 
    los cánidos. Lo caracterizan varios atributos que los diferencian 
    entre ellos:

    nombreEntrada: Hace referencia al nombre del perro
    generoEntrada: Hace referencia a si es macho o hembra
    habitadEntrada: Hace referencia si es de casa o de calle
    razaEntrada: Hace referencia al la raza
    El canino presenta las siguentes aciones:
    *dormir(accion):
        Describe cada cuanto duerme
    *jugar(accion):
        Describe su felicidad a la hora de jugar
    *mostrarAtributos():
        Muestra los atributos del canino
    '''

    def __init__(self,nombreEntrada,razaEntrada,habitatEntrada,generoEntrada):
        print("Holis, soy una perro muy amoroso")
        self.nombre = nombreEntrada
        self.genero = generoEntrada
        self.habitat = habitatEntrada
        self.raza = razaEntrada

    def dormir (self):
        print(f'''Podria decir que me considero un {self.raza} muy dormilon.
    Duermo toda la noche y hago siestas al medio día.
    ''')

    def jugar (self):
        print(f''' Ademas de eso, vivo en una/la {self.habitat} difrutando y 
    jugando al máximo día y noche hasta caer cansado, 
    se pasa un rato agradable.
    ''')

    def mostrarAtributos (self):
        print(f'''Holis mi nombre es {self.nombre} y soy {self.genero}.
    Me encuentro viviendo en una/la {self.habitat} y soy de 
    raza {self.raza} lo que me hace atractivo 
    para las personas cuando me ven.
    ''')

perro1 = Perro('Pancho', 'Bugdog Inglés', 'casa', 'macho')
perro2 = Perro('Milu', 'Chihuahua', 'casa', 'hembra')
perro3 = Perro('Rocky', 'Golden retriever', 'calle', 'macho')

print('--------------- Perro 1 ---------------')
perro1.mostrarAtributos()
perro1.dormir()
perro1.jugar()

print('--------------- Perro 2 ---------------')
perro2.mostrarAtributos()
perro2.dormir()
perro2.jugar()

print('--------------- Perro 3 ---------------')
perro3.mostrarAtributos()
perro3.dormir()
perro3.jugar()
