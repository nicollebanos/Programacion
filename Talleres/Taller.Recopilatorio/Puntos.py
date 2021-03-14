
#---------------Preguntas --------------------#
preguntaNumero = '''Ingrese alguna de estas opciones
    1.Hacer conversión de dolares a pesos colombianos o Euros
    2.Agregar un valor a la lista de dolares
    3.Mostrar si es bajo, medio alto o elevado ingreso
    4. Mostrar ingreso más alto, más bajo y promedio
    5.Salir
'''

#-----------------------Punto 1----------------------#
listaDolares = [20000,30000,4000,2500,1000,7600]
preguntaMoneda = '''
    C- Mostrar en pesos colombiano
    D- Mostrar original en Dolares
    E- Mostrar en Euros
'''
mensajeDolares = 'Mostran lista original'
mensajePesos = 'Mostrando lista pesos colombianos'
mensajeEuros = 'Mostran lista en euros'
mensajeErrorEntrada ='valor ingresado no valido'
preguntarNumero = 'Ingrese un valor en dolares :'

mensajeIgredoBajo = 'El ingreso bajo es -->'
mensajeIngresoMedio = 'El ingreso medio es -->'
mensajeIngresoAlto = 'El ingreso altoes -->'
mensajePromedio = 'El promedio es -->'

mensajeDespedida ='Muchas gracias, vuelva pronto'

listaEuros = []
for elemento in listaDolares:
    conversor = round (elemento*0.84,2)
    listaEuros.append(conversor)
listaPesos = []
for elemento in listaDolares:
    conversor = round (elemento*3700,2)
    listaPesos.append(conversor)

#----------------------- Opciones -----------------------#
opcionEscogida = int(input(preguntaNumero))
while (opcionEscogida !=5):
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
    #----------------------Opcion2---------------------------#
    elif (opcionEscogida == 2):
        valorIngresado = float (input(preguntarNumero))
        listaDolares.append(valorIngresado)
        print(listaDolares)
    #-------------------------------Opcion3-------------------------#
    elif(opcionEscogida == 3):
        print(mensajeIgredoBajo, max(listaDolares))
        print(mensajeIngresoMedio, min(listaDolares))
        print(mensajeIngresoAlto, )
        print(mensajePromedio,sum(listaDolares)/len(listaDolares))
    #-------------------------------Opcion4-----------------------------#
    #---------Opcion no valida---------#
    else:
        print(mensajeErrorEntrada)
    opcionEscogida = int(input(preguntaNumero))

print (mensajeDespedida)