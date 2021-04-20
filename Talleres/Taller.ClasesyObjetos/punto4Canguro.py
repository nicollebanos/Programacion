# Cree una clase Canguro que tenga los atributos edad, id, nombre. 
# Cree una función que, dada una cantidad de saltos, 
# muestre en pantalla uno a uno los saltos del canguro. 
# Ejemplo : cangurp.saltos (5) →retorna lo siguiente :
# El canguro ha dado 1 salto
# El canguro ha dado 2 salto
# El canguro ha dado 3 salto
# El canguro ha dado 4 salto
# El canguro ha dado 5 salto

class Canguro ():
    '''
    edadEntrada: Hace referencia a la edad
    idEntrada: Hace referencia al ID
    nombreEntrada: Hace referencia al nombre
    '''

    def __init__(self, edadEntrada, idEntrada, nombreEntrada):
        self.edad = edadEntrada
        self.id = idEntrada
        self.nombre = nombreEntrada
