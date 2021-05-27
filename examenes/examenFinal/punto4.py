
# Un consultorio de neurología desea tener un archivo para el manejo de 
# los clientes, se pide que desarrolle un programa que en su primera ejecución cree el archivo 
# llamado pacientes.txt. Luego en cada ejecución se preguntará por el nombre del paciente, una 
# descripción de la enfermedad y el precio de la consulta (se deben almacenar estos datos 
# nuevos en el archivo pacientes.txt).

import sys

nombre = input('Digite su nombre: ')
enfermedad = input('Digite que enfermedad padece: ')
precio = input('Digite el precio de la consulta: ')

NOMBRE_ARCHIVO = "paciente.txt"
try:
    archivo = open(NOMBRE_ARCHIVO)
    print('I')
except FileNotFoundError: 
    archivo = open (NOMBRE_ARCHIVO, 'w', encoding='UTF-8')
    descripcion = 'Archivo del paciente de neurologia'
    print('II')
    archivo.writelines(descripcion)
    sys.exit(1)

archivo = open(NOMBRE_ARCHIVO,'a')
linea = "\nnombre:"+ nombre + " edad: "+ str(enfermedad) + " estatura: "+ str(precio)
archivo.writelines(linea)
archivo.close()

with open(NOMBRE_ARCHIVO, 'r') as reader:
    for line in reader:
        print(line)

