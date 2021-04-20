
print( '#------------------- PUNTO 1 ------------------#' )
#Cree la clase Persona con id, nombre, edad y cree 
#la función hablar la cual dado mensaje 
#se muestra en pantalla y cree la clase caminar 
#que dado una cantidad de pasos muestra en 
#pantalla cuanto ha caminado

class Persona ():
    '''
    nombreEntrada: Hace referencia al nombre
    edadEntrada: Hace referencia a la edad
    idEntrada: Hace referencia al ID
    Acción:
    *Hablar(accion): 
        Comentario
    *Caminar(accion):
        Pasos dados
    '''

    def __init__(self, nombreEntrada, edadEntrada, idEntrada):
        self.nombre = nombreEntrada
        self.edad = edadEntrada
        self.id = idEntrada


    def mostrarAtributos (self):
        print(f''' Soy {self.nombre}, tengo {self.edad} de
        edad y me identifico con el número de cedula
        {self.id} 
        ''')

    def hablar(self,mensaje):
        print(f'Tengo un mensaje que decir...', mensaje)
    
    def caminar(self, pasos):
        for i in range (pasos):
            print(f''' Como caminar ayuda a despejar la mente, 
            el día de hoy he dado {i + 1} pasos
            ''')


persona1 = Persona('Camilo', 18, 1003293645)
persona2 = Persona('Angelica', 21, 1004283456)
persona3 = Persona('Marlon', 28, 1002384512)

print('--------------- persona 1 ---------------')
persona1.mostrarAtributos()
persona1.hablar('Hoy me siento muy feliz')
persona1.caminar(5)

print('--------------- persona 2 ---------------')
persona2.mostrarAtributos()
persona2.hablar('Hoy no estoy muy bien, pero sigo de pie')
persona2.caminar(3)

print('--------------- persona 3 ---------------')
persona3.mostrarAtributos()
persona3.hablar('Hoy es un día más, sere feliz')
persona3.caminar(9)

print('#------------------- PUNTO 2 ------------------#')
#Herede la clase persona y cree la clase Doctor el 
#cual tendrá el nuevo atributo de especialidad y 
#podrá ejecutar una nueva función, la cual es dado 
#una enfermedad muestre en pantalla: procedo a tratar
#dicha enfermedad

class Doctor (Persona):
    def __init__(self, nombreEntrada, idEntrada, edadEntrada, especialidadEntreda):
        Persona.__init__(self, nombreEntrada, idEntrada, edadEntrada)
        self.especialidad = especialidadEntreda

    def tratamiento (self, enfermedad):
        print(f'''Hola soy {self.nombre}, me especialice
        en {self.especialidad} y el día de hoy
        te ayudare con tu problema de {enfermedad}
        ''')

doctor = Doctor('Jose', 199238, 50, 'Dermatologia')

doctor.tratamiento('Acne')

print('#------------------- PUNTO 3 ------------------#')
# Herede la clase Persona y cree la clase Nutricionista y 
# cree un atributo que se refiera a la 
# universidad en la que fue egresado. 
# También una función que devuelva el IMC dado el 
# peso y altura de un paciente

class Nutricionista (Persona):
    def __init__(self, nombreEntrada, idEntrada, edadEntrada, universidadEntreda):
        Persona.__init__(self, nombreEntrada, idEntrada, edadEntrada)
        self.universidad = universidadEntreda


    def masaCorporal (self, pesoEntrada, alturaEntrada):
        self.peso = pesoEntrada
        self.altura = alturaEntrada
        imc = self.peso / (self.altura**2)
        print(f''' Como tu nutriologo, vericando los datos
        de {self.peso} kg  de peso y {self.altura} m de altura, 
        da como resultado que tu IMC es {imc}
        ''')

nutricionista = Nutricionista('Diego', 199273561, 50, 'CES')
nutricionista.masaCorporal(60, 1.80)