
# Un taller de biomédica desea tener un archivo para el manejo de los 
# clientes, se pide que desarrolle un programa que en su primera ejecución 
# cree el archivo llamado mantenimientos.txt. Luego en cada ejecución se 
# preguntará por el nombre del equipo médico, una descripción y el precio 
# acordado para el mantenimiento (se deben almacenar estos datos nuevos en 
# el archivo mantenimientos.txt)

def validarArchivo(nombreArchivo, descripcion):
    try:
        archivo = open(nombreArchivo)
        return True
    except FileNotFoundError:
        archivo = open(nombreArchivo, 'w', encoding='UTF-8')
        print("2")
        archivo.writelines(descripcion)
        return False

def guardarLinea (nombreArchivo, lineaIn):
    archivo = open(nombreArchivo,'a')
    archivo.writelines(lineaIn)

nameFile = "mantenimientos.txt"
isValidate = validarArchivo(nameFile, 'Seguimiento de mantenimiento de equipos medicos')
if (isValidate):
    descEquipo = input('Ingrese la descripción del equipo : ')
    nombre = validateString('Ingrese su nombre: ')
    precio = validateFloat('Ingrese el precio:  ')
    linea ='\nDescripcion465'+ descEquipo+ ' nombre técnico: ' + nombre + ' precio acordado: '+ str(precio)
    guardarLinea(nameFile, linea)
else:
    print('se creó el archivo')