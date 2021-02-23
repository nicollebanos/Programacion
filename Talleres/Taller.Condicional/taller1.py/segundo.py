
# #Constantes
PREGUNTA_NOMBRE = "Cúal es tu nombre?: "
MENSAJE_BIENVENIDA = "Buenas, espero que te encuentres muy bien"
PREGUNTA_EDAD = "Cuantos años tienes?: "
MENSAJE_MENOR_EDAD = "Aún eres menor de edad, espera algunos años más"
MENSAJE_JOVEN = "La juventud esta en ti, gozala"
MENSAJE_ADULTO = "Es la etapa con más resposabilidades, la adultez"
MENSAJE_ADULTO_MAYOR = "Ojo con el covid, eres adulro mayos"
MENSAJE_SALIDA = "Muchas gracias, cuidate"

#Bienvenida
print("---------------Bienvenida---------------------")
nombre = input(PREGUNTA_NOMBRE) 
print(MENSAJE_BIENVENIDA, nombre)

#Código
print("---------------Dato---------------------")
edad = int(input(PREGUNTA_EDAD))
isMenorEdad = edad < 18
isJoven = edad >= 18 and edad < 25
isAdulto = edad >= 26 and edad < 60
isMayorAdulto = edad >= 60

print("---------------respuesta---------------------")
if (isMenorEdad):
    print(MENSAJE_MENOR_EDAD)
elif (isJoven):
    print(MENSAJE_JOVEN)
elif (isAdulto):
    print(MENSAJE_ADULTO)
else:
    print(MENSAJE_ADULTO_MAYOR)

print("---------------despedida---------------------")
print(MENSAJE_SALIDA, nombre)