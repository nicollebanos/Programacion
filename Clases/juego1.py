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
print('------------ Inicio juego ---------------------')
numeroOculto = 7
vidas = 3
print(MENSAJE_SALUDO)
numeroIngresado = int(input(PREGUNTA_NUMERO))
if(numeroIngresado != numeroOculto):
    vidas -=1
while(numeroOculto != numeroIngresado and vidas > 0) :
    vidas -=1
    numeroIngresado = int(input(PREGUNTA_FALLASTE))

if(vidas > 0):
    print(MENSAJE_GANASTE)
    print(vidas)
else:
    print(MENSAJE_PERDISTE, 'El número era el', numeroOculto)