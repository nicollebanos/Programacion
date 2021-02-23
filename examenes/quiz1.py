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
isAlto = edad >= 26 and edad < 60
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