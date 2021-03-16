

#---------------Pregunta inicial --------------------#
preguntaNumero = '''Ingrese alguna de estas opciones
    1. Hacer conversión de grados Centigrados a Kelvin o a fahrenheit.
    2. Mostrar si es hipotermia, fiebre o temperatura normal, clasificación.
    3. Mostrar la temperatura máxima y la minima.
    4.Salir.
'''

#------------------ Temperatura original en C° --------------------#
listaTemperaturaCorporal = [36,37,38,35,36,38,37.5,38.2,41,37.4,38.6,39.1,40.3,33]
preguntaTemperatura = '''
    C- Mostrar lista original en centigrados
    D- Mostrar en grados Kelvin
    E- Mostrar en grados fahrenheit
'''
#-------------------- MENSAJES -----------------#
MENSAJE_GRADO_KELVIN = 'Mostrando lista en grados kelvin'
MENSAJE_GRADO_CENTIGRADO = 'La conversión no es valida, ya la lista se encuentra en grados centigrados'
MENSAJE_GRADO_FAHRENHEIT = 'Mostrando lista en grados fahrenheit'
MENSAJE_ERROR_ENTRADA ='valor ingresado no valido'

MENSAJE_OPCION = 'Usted escogio la opción {}'

MENSAJE_TEMP_MAX = 'La temperatura máxima es -->'
MENSAJE_TEMP_MIN = 'La temperatura minima es -->'


masAlto = max (listaTemperaturaCorporal)
masBajo = min (listaTemperaturaCorporal)

MESNSAJE_DESPEDIDA ='Muchas gracias... espero que haya sido de mucha ayuda para usted, vuelva pronto '

#---------------- punto 1 --------------------#
listaGradosKelvin = []
for elemento in listaTemperaturaCorporal:
    conversor = round (273.15+elemento)
    listaGradosKelvin.append(conversor)
listaGradosFahrenheit = []
for elemento in listaTemperaturaCorporal:
    conversor = round ((elemento*1.8)+32)
    listaGradosFahrenheit.append(conversor)

#------------------- Punto 2 ------------------------#
listaClasificacion = []
for elemento in listaTemperaturaCorporal:
    clasificacion = ''
    if (elemento < 36 ):
        clasificacion = 'Hipotermia'
    elif (elemento >= 37.6):
        clasificacion = 'Fiebre'
    elif (elemento >= 36 and elemento < 37.5):
        clasificacion = 'Temperatura normal'
    listaClasificacion.append(clasificacion)

#----------------------- Opciones INICIO -----------------------#
opcionEscogida = int(input(preguntaNumero))
while (opcionEscogida !=4):
    #--------------------------Opcion1----------------------------#
    if (opcionEscogida == 1):
        opcionTemperatura = input(preguntaTemperatura)
        if (opcionTemperatura == 'C'):
            print(MENSAJE_GRADO_CENTIGRADO)
            print(listaTemperaturaCorporal)
        elif (opcionTemperatura == 'D'):
            print(MENSAJE_GRADO_KELVIN)
            print(listaGradosKelvin)
        elif (opcionTemperatura == 'E'):
            print(MENSAJE_GRADO_FAHRENHEIT)
            print(listaGradosFahrenheit)
        else:
            print(MENSAJE_ERROR_ENTRADA)
    #-------------------------------Opcion2-------------------------#
    elif (opcionEscogida == 2):
        print(MENSAJE_OPCION.format(2))
        print (listaClasificacion)
    #--------------------------- Opcion 3 -------------------------#
    elif (opcionEscogida == 3):
        print(MENSAJE_OPCION.format(3))
        print (MENSAJE_TEMP_MAX, masAlto)
        print (MENSAJE_TEMP_MIN, masBajo)
    #---------Opcion no valida---------#
    else:
        print(MENSAJE_ERROR_ENTRADA)
    opcionEscogida = int(input(preguntaNumero))

#--------------- vuelve -------------#
print (MESNSAJE_DESPEDIDA)

