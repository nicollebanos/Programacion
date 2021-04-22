
class Usuario():
    def __init__(self, nombreEntrada, edadEntrada, sexoEntrada, nacionalidadEntrada):
        self.nombre = nombreEntrada
        self.edad = edadEntrada
        self.sexo = sexoEntrada
        self.nacionalidad = nacionalidadEntrada

    def mostrarAtributos (self):
        print(f''' Hola mi nombre es {self.nombre}, tengo
            {self.edad} y soy de {self.nacionalidad}. Me considero
            una persona del sexo {self.sexo} y amante de la música.
    ''')

    def tocar (self, cancion):
        print(f''' El día de hoy estoy escuchando
        {cancion}
    ''')

usuario = Usuario('Ándres', 23, 'masculino', 'colombiana')

usuario.mostrarAtributos()
usuario.tocar('El condor herido')

