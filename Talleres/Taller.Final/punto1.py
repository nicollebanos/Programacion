
#  Calcular el IMC de un usuario, pero valide que los datos de entrada 
# sean los correctos en caso de que alguna entrada sea errónea vuelva a 
# solicitar el ingreso del dato hasta que sea correcto (adicionalmente pida el 
# nombre y valide que sea un nombre válido)

#--------------constantes-----------#
PREGUNTA_PESO = 'Digita tu peso: '
PREGUNTA_NOMBRE = 'Digite su nombre: '
PREGUNTA_ESTATURA = 'Digita tu estatura: '
MENSAJE_BIENVE = 'Hola, calculare tu IMC, llena los siguentes datos'
MENSAJE_DESPEDIDA = 'Tú IMC es... '

#--------------constantes-----------#
print(MENSAJE_BIENVE)            

isCorrectInfo = False
while(isCorrectInfo == False):
    try: 
        nombre = input(PREGUNTA_NOMBRE)
        assert(nombre.isalpha())
        isCorrectInfo = True
    except AssertionError:
        print('Ingresaste un dato no valido')

isCorrectInfo = False
while(isCorrectInfo == False):
    try: 
        peso = int(input(PREGUNTA_PESO))
        isCorrectInfo = True
    except ValueError:
        print('Ingrese un valor numerico')

isCorrectInfo = False
while(isCorrectInfo == False):
    try: 
        estatura = float(input(PREGUNTA_ESTATURA))
        isCorrectInfo = True
    except ValueError:
        print('Ingrese un valor numerico')


imc = peso/(estatura**2)
print(MENSAJE_DESPEDIDA, imc)
