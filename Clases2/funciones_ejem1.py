
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


#------------- sumar dos números -------------#
def sumar (a = 0,b = 0): #---- Valores por defector ----#
    '''
        devulve la suma de dos números a y b
        por defecto a vale cero al igual que b
    '''
    suma = a + b
    return suma
linedesing(10,':v')
resultado = sumar()
print(sumar(12,14))
round(12.23456,2)

#------------- restar dos números -------------#
def restar (a = 0,b = 0): #---- Valores por defector ----#
    resta = a - b
    return resta

#------------- multiplicar dos números -------------#
def multiplicar (a = 0,b = 0): #---- Valores por defector ----#
    multiplica = a * b
    return multiplica

#------------- dividir dos números -------------#
def dividir (a = 0,b = 1): #---- Valores por defector ----#
    dividi = a / b
    return dividi

#------------- potenciar dos números -------------#
def potenciar (base = 0,exponente = 1): #---- Valores por defector ----#
    potencia = base ** exponente
    return potencia

#------------- funciones dependientes de otras -------------#
def calcular (operacion, numeroA, numeroB):
    print(operacion(numeroA,numeroB))


print(restar(83,87))
print(multiplicar(83,87))
print(dividir(83,87))

calcular(multiplicar,63,67)