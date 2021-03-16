

#---------------Pregunta inicial --------------------#
preguntaNumero = '''Ingrese alguna de estas opciones
    1. Hacer conversión de grados Centigrados a Kelvin o a fahrenheit.
    2. Mostrar es hipotermia, fiebre o temperatura normal, clasificación.
    3. Mostrar la temperatura maxima y la minima.
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
MENSAJE_GRADO_CENTIGRADO = 'La conversión no es valida'
MENSAJE_GRADO_FAHRENHEIT = 'Mostrando lista en grados fahrenheit'
MENSAJE_ERROR_ENTRADA ='valor ingresado no valido'

mensajeOpcion = 'Usted escogio la opción {}'

mensajeIgredoBajo = 'El ingreso bajo es -->'
mensajeIngresoMedio = 'El ingreso medio es -->'
mensajeIngresoAlto = 'El ingreso altoes -->'
mensajePromedio = 'El promedio es -->'

masAlto = max (listaTemperaturaCorporal)
masBajo = min (listaTemperaturaCorporal)
acumulador = 0
for elemento in listaTemperaturaCorporal :
    acumulador += elemento

mensajeDespedida ='Muchas gracias, vuelva pronto'

#---------------- punto 1 --------------------#
listaGradosKelvin = []
for elemento in listaTemperaturaCorporal:
    conversor = round (273.15*elemento)
    listaGradosKelvin.append(conversor)
listaGradosFahrenheit = []
for elemento in listaTemperaturaCorporal:
    conversor = round ((elemento-32)/1.8)
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
        print(mensajeOpcion.format(2))
        print (listaClasificacion)
    #--------------------------- Opcion 3 -------------------------#
    elif (opcionEscogida == 3):
        print(mensajeOpcion.format(3))
        print ('El ingreso más alto fue', masAlto)
        print ('El ingreso más bajo fue', masBajo)
        print ('El ingreso en promedio fue', promedioDolares)
    #---------Opcion no valida---------#
    else:
        print(mensajeErrorEntrada)
    opcionEscogida = int(input(preguntaNumero))

#--------------- vuelve -------------#
print (mensajeDespedida)

