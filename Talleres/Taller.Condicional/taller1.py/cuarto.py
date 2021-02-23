

# #Constantes
PREGUNTA_NOMBRE = "Cómo te llamas?: "
MENSAJE_BIENVENIDA = "Bienvenid@"
MENSAJE_SALIDA = "Muchas gracias, vuelva pronto"
PREGUNTA_UNO = "Ingrese la distancia en cm: "
PREGUNTA_DOS = "¿A qué unidad la desea convertir? ¿km, m o mm?:"
MENSAJE_DISTANCIA = "La distancia es: "
MENSAJE_OPCION_INVALIDO = "Opción no valida"

#Bienvenida
print("---------------Bienvenida---------------------")
nombre = input(PREGUNTA_NOMBRE) 
print(MENSAJE_BIENVENIDA, nombre)

#Datos
distancia = float(input(PREGUNTA_UNO))
respuesta_unidad = input(PREGUNTA_DOS)

#Código
if(respuesta_unidad.lower() == "km"):
    distancia = distancia * 10**-5
    print(MENSAJE_DISTANCIA, distancia, "km")
elif(respuesta_unidad.lower() == "m"):
    distancia = distancia * 10**-2
    print(MENSAJE_DISTANCIA, distancia, "m")
elif(respuesta_unidad.lower() == "mm"):
    distancia = distancia * 10
    print(MENSAJE_DISTANCIA, distancia, "mm")
else:
    print( )

print("---------------despedida---------------------")
print(MENSAJE_SALIDA, nombre)