
from datetime import date
#PUNT03. Escriba un programa que pida el año actual y un año cualquiera
# y que escriba cuántos años han pasado desde ese año o cuántos años faltan para llegar a ese año.

#Constantes
PREGUNTA_NOMBRE = "Cúal es tu nombre?: "
MENSAJE_BIENVENIDA = "Bienvenid@"
PREGUNTA_ANOS = "Ingresa un año: "
MENSAJE_ANOS_FALTANTES = "Faltan {} años para el año que ingresaste"
MENSAJE_ANOS_PASADOS = "Desde el año actual, han pasado {} años"
MENSAJE_ANOS_IGUALES = "El año ingresado es igual al año actual"

#Bienvenida
print("---------------Bienvenida---------------------")
nombre = input(PREGUNTA_NOMBRE) 
print(MENSAJE_BIENVENIDA, nombre)

#Datos
print("---------------dato---------------------")
anhoUsuario = int(input(PREGUNTA_ANO))
anhoActual = date.today().year

print("---------------respuesta---------------------")
#Código
if (anhoActual > anhoUsuario):
    resta = anhoActual - anhoUsuario
    print(MENSAJE_ANOS_PASADOS.format(resta))
elif (anhoActual < anhoUsuario):
    restapasados = anhoUsuario - anhoActual
    print(MENSAJE_ANOS_FALTANTES.format(restapasados))
else:
    print(MENSAJE_ANOS_IGUALES)
