
#--- Que devuelva todos los números pares de una lista de números enteros ---#

def paresLista(lista):
  pares = []
  for elemento in lista:
    if elemento % 2 == 0 :
      pares.append (elemento)
  return pares

edades = [22, 31, 43, 20, 38, 40, 60, 17, 84, 9]
edadesPares = paresLista(edades)
print (edadesPares)