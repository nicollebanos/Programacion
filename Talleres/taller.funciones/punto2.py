
#Dada una lista de números enteros muestre en pantalla el número más grande, el más pequeño y el promedio de la lista


def listaNumEnte(lista):
  mayor = max (lista)
  menor = min (lista)
  acumulador = 0
  for elemento in lista :
    acumulador += elemento
  sizeList =   len (lista)
  promedio = acumulador / sizeList
  print('---------- Respuestas ------------')
  print (f'''
                El número mayor: {mayor}, 
                el menor: {menor} y 
                el promedio: {promedio}
''')
numeros_enteros = [22, 32, 43, 20, 38, 40, 60, 18, 84, 28]
listaNumEnte(numeros_enteros)
