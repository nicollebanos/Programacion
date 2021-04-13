
class Humano(): 
    def __init__(self):
        print('Hola, soy un humano nuevo')
    
    def hablar(self, mensaje):
        print('Hola, tengo un mensaja que decir...', mensaje)

humano1 = Humano()
humano2 = Humano()

humano1.hablar('Espero que esten muy bien')
humano2.hablar('Chao')