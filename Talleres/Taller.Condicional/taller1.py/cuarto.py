

#Constantes
PREGUNTA_NOMBRE = "Cómo te llamas?: "
MENSAJE_BIENVENIDA = "Bienvenid@"
MENSAJE_SALIDA = "Muchas gracias, vuelve pronto"
PREGUNTA_PRIMERA = "Ingrese una distancia en cm: "
PREGUNTA_SEGUNDA = "¿A que unidad quieres pasarlo? ¿km, m o mm?:"
MENSAJE_DISTANCIA = "La distancia es: "

#Bienvenida
print("---------------Bienvenida---------------------")
nombre = input(PREGUNTA_NOMBRE) 
print(MENSAJE_BIENVENIDA, nombre)

#Datos
print("---------------dato---------------------")
distancia = float(input(PREGUNTA_PRIMERA))
respuesta_unidad = input(PREGUNTA_SEGUNDA)

print("---------------respuesta---------------------")
#Código
if(respuesta_unidad.lower() == "km"):
    distancia = distancia * 10**-5
    print(MENSAJE_DISTANCIA, distancia, "km")
elif(respuesta_unidad.lower() == "mm"):
    distancia = distancia * 10
    print(MENSAJE_DISTANCIA, distancia, "mm")
elif(respuesta_unidad.lower() == "m"):
    distancia = distancia * 10**-2
    print(MENSAJE_DISTANCIA, distancia, "m")

print("---------------despedida---------------------")
print(MENSAJE_SALIDA, nombre)