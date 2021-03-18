
guardar = print('Hola')
print(guardar)

guardar = round(14.2534897,2)
print(guardar)

def linedesing(cantidad, simbolo):
    print(simbolo*cantidad)
    return None

linedesing(30,'#')
linedesing(10,'*')
linedesing(40,'!')

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