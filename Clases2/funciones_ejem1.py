
guardar = print('Hola')
print(guardar)

guardar = round(14.2534897,2)
print(guardar)

def linedesing(cantidad=10, simbolo='$'):
    print(simbolo*cantidad)
    return None

linedesing(30,'#')
linedesing(10,'*')
linedesing(40,'!')
linedesing() #--- Por defecto ---#

#------------- Muestre la lista -------------#
def mostrarLista(inLista):
    for elemento in inLista:
        print(elemento)
    return None
lista = [22, 23, 24, 25, 27]
lista2 = [1, 2, 3, 4,5]
linedesing(30,':v')
mostrarLista(lista)
linedesing(30,'.-.')
mostrarLista(lista2)


#------------- sumar dos númerod -------------#
def sumar (a = 0,b = 0):
    suma = a + b
    return suma
linedesing(10,':v')
resultado = sumar()
print(sumar(12,14))
round(12.23456,2)
