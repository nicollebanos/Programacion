
#---------------Preguntas --------------------#
preguntaNumero = '''Ingrese alguna de estas opciones
    1.Hacer conversión de dolares a pesos colombianos o Euros
    2.Mostrar si es bajo, medio alto o elevado ingreso
    3. Mostrar ingreso más alto, más bajo y promedio
    4.Salir
'''

listaDolares = [20000,30000,4000,2500,1000,7600]
preguntaMoneda = '''
    C- Mostrar en pesos colombiano
    D- Mostrar original en Dolares
    E- Mostrar en Euros
'''
mensajeDolares = 'Mostrando lista original'
mensajePesos = 'Mostrando lista pesos colombianos'
mensajeEuros = 'Mostrando lista en euros'
mensajeErrorEntrada ='valor ingresado no valido'
preguntarNumero = 'Ingrese un valor en dolares :'

mensajeOpcion = 'Usted escogio la opción {}'

mensajeIgredoBajo = 'El ingreso bajo es -->'
mensajeIngresoMedio = 'El ingreso medio es -->'
mensajeIngresoAlto = 'El ingreso altoes -->'
mensajePromedio = 'El promedio es -->'

masAlto = max (listaDolares)
masBajo = min (listaDolares)
acumulador = 0
for elemento in listaDolares :
    acumulador += elemento
promedio= acumulador/len(listaDolares)
promedioDolares = round (promedio,2)

mensajeDespedida ='Muchas gracias, vuelva pronto'

#---------------- punto 1 --------------------#
listaEuros = []
for elemento in listaDolares:
    conversor = round (elemento*0.84,2)
    listaEuros.append(conversor)
listaPesos = []
for elemento in listaDolares:
    conversor = round (elemento*3700,2)
    listaPesos.append(conversor)

#------------------- Punto 2 ------------------------#
listaClasificacion = []
for elemento in listaDolares:
    clasificacion = ''
    if (elemento < 1000 ):
        clasificacion = 'Ingresos bajos'
    elif (elemento >= 1000 and elemento < 7000):
        clasificacion = 'Ingresos medios'
    elif (elemento >= 7000 and elemento < 20000):
        clasificacion = 'Ingresos altos'
    else:
        clasificacion = 'Ingresos elevados'
    listaClasificacion.append(clasificacion)

#----------------------- Opciones -----------------------#
opcionEscogida = int(input(preguntaNumero))
while (opcionEscogida !=4):
    #--------------------------Opcion1----------------------------#
    if (opcionEscogida == 1):
        opcionMoneda = input(preguntaMoneda)
        if (opcionMoneda == 'C'):
            print(mensajePesos)
            print(listaPesos)
        elif (opcionMoneda == 'D'):
            print(mensajeDolares)
            print(listaDolares)
        elif (opcionMoneda == 'E'):
            print(mensajeEuros)
            print(listaEuros)
        else:
            print(mensajeErrorEntrada)
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

