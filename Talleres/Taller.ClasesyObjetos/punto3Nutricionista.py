
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
    

    def __init__(self,nombreEntrada, idEntrada, carreraEntrada, semestreEntrada, edadEntrada):
        print("Datos por estudiante")
        self.nombre = nombreEntrada
        self.edad = edadEntrada 
        self.id = idEntrada
        self.carrera = carreraEntrada
        self.semestre = semestreEntrada  


    def mostrarAtributos (self):
        print(f''' Buenas tardes, mi nombre es {self.nombre} y tengo {self.edad}, 
        identificado con el ID {self.id}. Actualmente curso {self.semestre} 
        semetre de {self.carrera} y me siento dichos@ al poder decir
        que elegi bien mi carrera de vida
    ''')

    def tiempoEstudio (self, materiaEntrada, horasEntrada):
        self.materia = materiaEntrada
        self.horas = horasEntrada
        print(f'El día de hoy me dedicare a estudiar {self.materia} durante {self.horas} horas')

estudiante1 = Estudiante('Gabriela', '1002394756', 'diseño de modas', 'primer', '17')
estudiante2 = Estudiante('Ignacio', '1003945862', 'arquitectura', 'quinto', '20')
estudiante3 = Estudiante('Ándres', '1004293452', 'negocios internacionales', 'tercer', '19')

#----------------- Print ----------------------#
print('--------------- Estudiante 1 ---------------')
estudiante1.mostrarAtributos()
estudiante1.tiempoEstudio('geometría descriptiva', 2)

print('--------------- Estudiante 2 ---------------')
estudiante2.mostrarAtributos()
estudiante2.tiempoEstudio('análisis y diseño de estructuras', 3)

print('--------------- Estudiante 3 ---------------')
estudiante3.mostrarAtributos()
estudiante3.tiempoEstudio('Microeconomía', 2)

