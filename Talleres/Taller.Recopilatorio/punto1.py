
listaDolares = [20000,30000,4000,2500,1000,7600]
preguntaMoneda = '''
    C- Mostrar en pesos colombiano
    D- Mostrar original en Dolares
    E- Mostrar en Euros
'''
mensajeDolares = 'Mostran Lista original'
mensajePesos = 'Mostrando lista pesos colombianos'
mensajeEuros = 'Mostran Lista en euros'
mensajeErrorEntrada ='valor ingresado no valido'

listaEuros = []
for elemento in listaDolares:
    conversor = round (elemento*0.84,2)
    listaEuros.append(conversor)
listaPesos = []
for elemento in listaDolares:
    conversor = round (elemento*3700,2)
    listaPesos.append(conversor)

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