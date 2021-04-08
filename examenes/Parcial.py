# Crear una función que dado tres números 
# muestre en pantalla la suma, la resta, la multiplicación, la 
# división y la potencia entre ellos (ejem n1-n2-n3, n1/n2/n3, 
# etc.)

#------------- sumar dos números -------------#
def sumar (a = 0,b = 0, c = 0): 
    suma = a + b + c
    return suma

#------------- restar dos números -------------#
def restar (a = 0,b = 0, c = 0): 
    resta = a - b - c
    return resta

#------------- multiplicar dos números -------------#
def multiplicar (a = 0,b = 0, c = 0): 
    multiplica = a * b * c
    return multiplica

#------------- dividir dos números -------------#
def dividir (a = 0,b = 1, c = 1): 
    dividi = a / b / c
    return dividi

#------------- potencia dos números -------------#
def potenciar (base = 0,exponente = 1, exponente2 = 1): 
    potencia = base ** exponente ** exponente2
    return potencia


print(restar(40,28, 36))
print(multiplicar(40,28, 36))
print(dividir(40,28, 36))
print(multiplicar(40,28, 36))
print(potenciar(40,28, 36))