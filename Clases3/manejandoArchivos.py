
import sys

nombre = input('Ingrese su nombre: ')
edad = int(input('Ingrese su edad: '))
estatura = float(input('Ingrese su estatura: '))

nombreArchivo = 'estudiantes.txt'
try: 
    archivo = open(nombreArchivo, 'a')
    print('1')
except FileNotFoundError:
    archivo = open(nombreArchivo, 'w', encoding='UTF-8') 
    descripcion = 'Archivo de datos de estudiantes'
    print(2)
    archivo.writelines(descripcion)
    sys.exit(1)

archivo = open(nombreArchivo, 'a')
linea = '\nnombre: '+ nombre + 'edad: '+ str(edad) + 'estatura: '+ str(estatura)
archivo.writelines(linea)
archivo.close()

#leer
with open(nombreArchivo, 'r') as reader:
    for line in reader:
        print(line)



