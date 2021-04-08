# Crear una función que dada una lista de 
# números enteros muestre el promedio, el máximo, el 
# mínimo.

lista_nume_ente = [12, 18, 40, 20, 100, 35, 60, 102, 39, 26]

def listaNumEnte(lista):
  mayor = max (lista)
  menor = min (lista)
  acumulador = 0
  for elemento in lista :
    acumulador += elemento
  sizeList =   len (lista)
  promedio = acumulador / sizeList
  print('---------- Resutados ------------')
  print (f'''
    El número mayor es {mayor}, 
    el número menor es {menor} y 
    el promedio es {promedio}
''')

listaNumEnte(lista_nume_ente)
