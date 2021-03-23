
#------------- sumar dos números -------------#
def sumar (a = 0,b = 0): #---- Valores por defector ----#
    suma = a + b
    return suma

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
