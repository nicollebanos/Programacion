
import random
#----------- Entradas ----------#
MENSAJE_SALUDO =  '''Bienvenido 
                    a este programa,
                    juguemos!!'''
PREGUNTA_NUMERO = '''
                    En este juego debes asertar un número entero
                    que va desde el 1-10, la idea es que
                    lo puedes intentar antes de que se te 
                    acaben las vidas... 
                    muchos exitos, ingresa tu número 
'''
PREGUNTA_FALLASTE = 'Ahhhhhhhh! fallaste :3, ingresa otro número  '
MENSAJE_GANASTE = 'Felicidades, ganaste!!!'
MENSAJE_PERDISTE = 'Perdiste, vuelve a intentarlo!!!'
MENSAJE_SEGUNDO_NIVEL = 'Felicidades, pasaste el primer nivel... continuemos'
MENSAJE_CALIENTE = 'Estas caliente'
MENSAJE_FRIO = 'Estas frío'
PREGUNTA_DIFICULTAD = '''
            1- Fácil
            2- Moderado
            3- Difícil
'''

#----------------- Entrada al código -----------------#
numeroOculto = random.randint(1,10)
numeroOcultoDos = random.randint(1,10)
vidas = ''


dificultad = int(input(PREGUNTA_DIFICULTAD))
while(dificultad != 1 and dificultad != 2 and dificultad != 3):
    print('Ingrese una opción valida')
    dificultad = int(input(PREGUNTA_DIFICULTAD))

if(dificultad == 1):
    print('Modo fácil activado')
    vidas = 10
elif(dificultad == 2):
    print('Modo moderado activado')
    vidas = 5
else:
    print('Modo dicícil activado')
    vidas = 2

numeroIngresado = int (input(PREGUNTA_NUMERO))
while(numeroIngresado != numeroOculto and vidas>1):
    if(numeroIngresado > numeroOculto):
        print(MENSAJE_CALIENTE)
    else:
        print(MENSAJE_FRIO)
    vidas -=1
    print(F'te quedan {vidas} vidas')
    numeroIngresado =int(input(PREGUNTA_FALLASTE))
if(vidas >= 0 and numeroIngresado == numeroOculto):
    print(MENSAJE_SEGUNDO_NIVEL)
    numeroIngresado = int(input(PREGUNTA_NUMERO))
    while(numeroIngresado != numeroOcultoDos and vidas>1):
        if(numeroIngresado > numeroOcultoDos):
            print(MENSAJE_CALIENTE)
        else:
            print(MENSAJE_FRIO)
        vidas -=1
        print(F'te quedan {vidas} vidas')
        numeroIngresado =int(input(PREGUNTA_FALLASTE))


if(vidas >= 0 and numeroIngresado == numeroOculto):
    print(MENSAJE_GANASTE)

else:
    print(MENSAJE_PERDISTE, 
                    'El número uno era el ',
                    numeroOculto,
                    'El número dos era el',
                    numeroOcultoDos)