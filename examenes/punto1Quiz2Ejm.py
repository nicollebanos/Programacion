
listaPesos = [20000,30000,4000,2500,1000,7600]
PREGUNTA_MONEDA = '''
    C- Mostrar original en pesos colombianos
    D- mostrar en Dolares
    E- Mostrar en Euros
'''

listaEuros = []
for elemento in listaPesos:
    listaEuros.append(elemento*0.00023)
print(listaEuros)
