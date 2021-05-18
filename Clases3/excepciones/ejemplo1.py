
isCorrectInfo = False
while(isCorrectInfo == False):
    try: #intentar
        edad = int (input('ingrese su edad: '))
        isCorrectInfo = True
    except ValueError:
        print('Ingresaste un dato no valido')


NOMBRE_ARCHIVO = input('Ingrese el nombre del archivo que desea encotrar: ')
try:
    archivo = open(NOMBRE_ARCHIVO)
except FileNotFoundError:
    print(f'el archivo {NOMBRE_ARCHIVO} no ha sido encontrado')

base = 4
divisor = 0 
try:
    dividir = base/divisor 
except ZeroDivisionError: 
    print('El divisor ingresado es igual a cero, por lo cual es imposible dividir')

nombre = 'Nicolle'
print(nombre.isalpha()) #letras V y numeros F
assert(nombre.isalpha())
isCorrectInfo = False
while(isCorrectInfo == False):
    try: 
        nombre = input('ingrese su nombre: ')
        assert(nombre.isalpha())
        isCorrectInfo = True
    except AssertionError:
        print('Ingresaste un dato no valido')

isCorrectInfo = False
while(isCorrectInfo == False):
    try: 
        edad = int(input('ingrese su edad: '))
        assert(edad >= 18)
        isCorrectInfo = True
    except AssertionError:
        print('Los menores de edad no puede acceder')
    except ValueError:
        print('Las edades son números enteros')

lista = [2, 34, 23, 4]
try: 
    lista[5]
except IndexError:
    print('El indice es mayor al tamaño de la lista')

