
# Cree una clase Estudiante donde tenga de atributos edad, nombre, id, carrera, semestre. 
# También este estudiante tendrá una función donde dada una materia y una cantidad de 
# tiempo muestra en pantalla que estudiará dicha materia en esa cantidad de tiempo

class Estudiante ():
    '''En un aula de encuentro se reuniron varias personas
    de diferentes atributos academicos, los cuales serian:

    nombreEntrada: Hace referencia al nombre del estudiante
    edadEntrada: Hace referencia a la edad del estudiante
    idEntrada: Hace referencia al ID del estudiante
    carreraEntrada: Hace referencia a la carrera del estudiante
    semestreEntrada: Hace referencia el semestre en el que cursa el estudiante
    El estudiante presenta las siguentes aciones:
    *Estudio(accion):
        Descibre el tiempo de estudio del estudiante
    '''

    def __init__(self,nombreEntrada, idEntrada, carreraEntrada, semestreEntrada):
        print("Datos por estudiante")
        self.nombre = nombreEntrada
        self.id = idEntrada
        self.carrera = carreraEntrada
        self.semestre = semestreEntrada 


    def mostrarAtributos (self):
        print(f''' 
    ''')

estudiante1 = 
estudiante2 = 
estudiante3 = 

#----------------- Print ----------------------#
print('--------------- Estudiante 1 ---------------')
estudiante1.mostrarAtributos()

print('--------------- Estudiante 2 ---------------')
estudiante2.mostrarAtributos()

print('--------------- Estudiante 3 ---------------')
estudiante3.mostrarAtributos()
