
import random
#----------- Entradas ----------#
MENSAJE_SALUDO =  '''Bienvenido 
                    a este programa,
                    juguemos!!'''
PREGUNTA_NUMERO = '''
                    En este juego debes asertar un número entero
                    que va desde el 1-10, la idea es que
                    lo puedes intentar las veces que 
                    quieras...
                    muchos exitos, ingresa tu número 
'''
PREGUNTA_FALLASTE = 'Ahhhhhhhh! fallaste :3, ingresa otro número  '
MENSAJE_GANASTE = 'Felicidades, ganaste!!!'
MENSAJE_PERDISTE = 'Perdiste, vuelve a intentarlo!!!'

#----------------- Entrada al código -----------------#
numeroOculto = random.randint(1,10)
vidas = 3
numeroIngresado = int(input(MENSAJE_NUMERO))
while(numeroIngresado != numeroOculto and vidas>1):
    vidas-=1
    print(vidas)
    print(numeroOculto)
    numeroIngresado =int(input(PREGUNTA_FALLASTE))
    