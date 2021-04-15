
class Perro ():
    '''Es un mamífero domestico carnívoro de la familia de 
    los cánidos. Lo caracterizan varios atributos que los diferencian 
    entre ellos:

    nombreEntrada: Hace referencia al tipo de Perro
    generoEntrada: Hace referencia a si es macho o hembra
    habitadEntrada: Hace referencia si es de casa o de calle
    razaEntrada: Hace referencia al la raza - pequeña, mediana, grande
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
        print(f"Holis soy {self.nombre}  y soy un canino muy dormilon")

    def jugar (self):
        print(f'''Soy un canino de nombre {self.nombre} y 
    vivo con tanta energía que juego todo el día
    sin cansarme
    ''')

    def mostrarAtributos (self):
        print(f'''Holis mi nombre es {self.nombre} y soy {self.genero}.
                Me encuentro viviendo en una/la {self.habitat} y soy de 
                raza {self.raza} lo que me hace cada vez más 
                atractivo para las personas
    ''')

perro1 = Perro('Bugdog Inglés', 'macho', 'casa', 'mediana')
perro2 = Perro('Chihuahua', 'hembra', 'casa', 'pequeña')
perro3 = Perro('Golden retriever', 'macho', 'calle', 'grande')

perro1.mostrarAtributos()
perro2.mostrarAtributos()
perro3.mostrarAtributos()
