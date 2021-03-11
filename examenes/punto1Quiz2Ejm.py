
listaPesos = [20000,30000,4000,2500,1000,7600]
PREGUNTA_MONEDA = '''
    C- Mostrar original en pesos colombianos
    D- mostrar en Dolares
    E- Mostrar en Euros
'''

listaEuros = []
for elemento in listaPesos:
    conversor = round(elemento*0.00023,2)
    listaEuros.append(conversor)

listaDolares = []
for elemento in listaPesos:
    conversor = round(elemento*0.00028,2)
    listaDolares.append(conversor)

opcionMoneda = input(PREGUNTA_MONEDA)
if(opcionMoneda == 'C'):
    print('Mostrando lista original')
    print(listaPesos)
elif(opcionMoneda == 'D')
    print('Mostrar lista en dolares')
    print(listaDolares)
elif(opcionMoneda == 'E')
    print('Mostrar lista en Euros')
    print(listaEuros)
else:
    print('Valor ingresado no valido')

print(listaEuros)
print(listaDolares)
