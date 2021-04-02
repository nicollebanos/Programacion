
#----------- Que devuelva únicamente los elementos mayores a 24 ---------------#

def listaMayores(lista):
  mayores = []
  for elemento in lista:
    if elemento > 24 :
      mayores.append (elemento)
  return mayores
money_dolares = [10, 50, 27, 48, 100, 5, 23, 15]
money_mayores = listaMayores(money_dolares)
print('------- Respuesta --------------')
print('Los números mayores de 24 son:', money_mayores)
