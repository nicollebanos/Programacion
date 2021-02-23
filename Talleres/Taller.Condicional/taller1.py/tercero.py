
from datetime import date

#Constantes
PREGUNTA_NOMBRE = "Cúal es tu nombre?: "
MENSAJE_BIENVENIDA = "Bienvenid@"
PREGUNTA_ANOS = "Ingresa un año: "
MENSAJE_ANOS_FALTANTES = "Aún faltan {} años para llegar a esa fecha en particular"
MENSAJE_ANOS_PASADOS = "Han pasado {} años desde que fue esa fecha"
MENSAJE_ANOS_IGUALES = "Es el mismo año en el que nos encontramos"
MENSAJE_SALIDA = "Espero que haya sido útil, adios"

#Bienvenida
print("---------------Bienvenida---------------------")
nombre = input(PREGUNTA_NOMBRE) 
print(MENSAJE_BIENVENIDA, nombre)

#Datos
print("---------------dato---------------------")
anoUsuario = int(input(PREGUNTA_ANOS))
anoActual = date.today().year

print("---------------respuesta---------------------")
#Código
if (anoActual > anoUsuario):
    resta = anoActual - anoUsuario
    print(MENSAJE_ANOS_PASADOS.format(resta))
elif (anoActual < anoUsuario):
    restapasados = anoUsuario - anoActual
    print(MENSAJE_ANOS_FALTANTES.format(restapasados))
else:
    print(MENSAJE_ANOS_IGUALES)

print("---------------despedida---------------------")
print(MENSAJE_SALIDA, nombre)