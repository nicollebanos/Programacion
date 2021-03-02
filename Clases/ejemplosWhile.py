
#---------- Entradas -----------#
MENSAJE_BIENEVENIDA = 'Muy buenos días, a despertar'
PREGUNTA_MENU = ''' Ingrese
        1- Para mostrar los números del 1-5
        2- Para preguntar tu nombre
        3- Para mostrar el año en el que estamos
        4- Salir

'''
PREGUNTA_NOMBRE = 'Ingrese su nombre por favor: '
MENSAJE_ANO = 'Estamos en el años 2021'
MENSAJE_SALIR = 'Muchas gracias por usar el programa, feliz día'
MENSAJE_ERROR = 'Por favor ingrese un número valido'


entrada = 1
while(entrada >=1 and entrada<=3):
    entrada = int(input(PREGUNTA_MENU))
    if ( entrada == 1):
        print(1,2,3,4,5)
    elif(entrada == 2):
        nombre = input(PREGUNTA_NOMBRE)
        print(f'Bienvenido {nombre} a este menú, emplea las otras opciones')
    elif(entrada == 3):
        print(MENSAJE_ANO)
    elif(entrada == 4):
        print(MENSAJE_SALIR)
    else:
        entrada = 1
        print(MENSAJE_ERROR)