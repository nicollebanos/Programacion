#Constantes
PREGUNTA_NOMBRE = "Cúal es tu nombre?: "
MENSAJE_BIENVENIDA = "Bienvenid@ a nuestra base de datos sobre el perfil lípidico"
PREGUNTA_NIVEL_TRI = "Ingrese el valor de triglicéridos que tienes: "
VALOR_OPTIMO_TRI = "Tus niveles de triglicéridos estas en niveles optimos"
SOBRE_LIM_OPTIMO_TRI = "Tus niveles de triglicéridos estan en niveles sobre el límite optimo"
VALOR_ALTO_TRI = "Tus niveles de trigliceridos estan alto"
VALOR_MUY_ALTO_TRI = "Tus niveles de trigiceridos estan muy altos"


#Bienvenida
print("---------------Bienvenida---------------------")
nombre = input(PREGUNTA_NOMBRE) 
print(MENSAJE_BIENVENIDA, nombre)

#Código
print("---------------Dato---------------------")
valor = int(input(PREGUNTA_NIVEL_TRI))
isOptimo = valor < 150
isLimOptimo = valor > 150 and valor < 199
isAlto = valor > 200 and edad < 499
isMuyAlto = edad > 500

print("---------------respuesta---------------------")
if (isOptimo):
    print(VALOR_OPTIMO_TRI)
elif (isLimOptimo):
    print(SOBRE_LIM_OPTIMO_TRI)
elif (isAlto):
    print(VALOR_ALTO_TRI)
else:
    print(VALOR_MUY_ALTO_TRI)




print("---------------despedida---------------------")
print(MENSAJE_SALIDA, nombre)