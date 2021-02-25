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
MENSAJE_DESPEDIDA = 'Felicidades, ganaste!!!'

#----------------- Entrada al código -----------------#
print('------------ Inicio juego ---------------------')
numeroOculto = 7
print(MENSAJE_SALUDO)
numeroIngresado = int(input(PREGUNTA_NUMERO))
while(numeroOculto != numeroIngresado) :
    numeroIngresado = int(input(PREGUNTA_FALLASTE))

print(MENSAJE_DESPEDIDA)