#Constantes
PREGUNTA_NOMBRE = "Cúal es tu nombre?: "
MENSAJE_BIENVENIDA = "Bienvenid@ a nuestra base de datos sobre el perfil lípidico"
PREGUNTA_NIVEL_TRI = "Ingrese el valor de triglicéridos que tienes: "
VALOR_OPTIMO_TRI = "Tus niveles de triglicéridos estas en niveles optimos"
SOBRE_LIM_OPTIMO_TRI = "Tus niveles de triglicéridos estan en niveles sobre el límite optimo"
VALOR_ALTO_TRI = "Tus niveles de trigliceridos estan alto"
VALOR_MUY_ALTO_TRI = "Tus niveles de trigiceridos estan muy altos"
PREGUNTA_NIVEL_HOMO = "Ingrese el valor de homocisteína que tienes: "
VALOR_OPTIMO_HOMO = "Tus niveles de homocisteína estas en niveles optimos"
SOBRE_LIM_OPTIMO_HOMO = "Tus niveles de homocisteína estan en niveles sobre el límite optimo"
VALOR_ALTO_HOMO = "Tus niveles de homocisteína estan alto"
VALOR_MUY_ALTO_HOMO = "Tus niveles de homocisteína estan muy altos"
MENSAJE_SALIDA = "Espero que las respuestas hayan sido de tu agrado, cuidate"


#Bienvenida
print("---------------Bienvenida---------------------")
nombre = input(PREGUNTA_NOMBRE) 
print(MENSAJE_BIENVENIDA, nombre)

#Código
print("---------------Dato---------------------")
valor = float(input(PREGUNTA_NIVEL_TRI))
isOptimo = valor < 150
isLimOptimo = valor >= 150 and valor <= 199
isAlto = valor >= 200 and valor <= 499
isMuyAlto = valor > 500

#Código
valorhomo = float(input(PREGUNTA_NIVEL_HOMO))
isOptimoHomo = valorhomo >= 12 and valorhomo <= 15
isLimOptimoHomo = valorhomo > 15 and valorhomo <= 30
isAltoHomo = valorhomo > 30 and valorhomo <= 100
isMuyAltoHomo = valorhomo > 100

print("---------------respuesta---------------------")
if (isOptimo):
    print(VALOR_OPTIMO_TRI)
elif (isLimOptimo):
    print(SOBRE_LIM_OPTIMO_TRI)
elif (isAlto):
    print(VALOR_ALTO_TRI)
else:
    print(VALOR_MUY_ALTO_TRI)


if (isOptimoHomo):
    print(VALOR_OPTIMO_HOMO)
elif (isLimOptimoHomo):
    print(SOBRE_LIM_OPTIMO_HOMO)
elif (isAltoHomo):
    print(VALOR_ALTO_HOMO)
else:
    print(VALOR_MUY_ALTO_HOMO)

print("---------------despedida---------------------")
print(MENSAJE_SALIDA, nombre)


