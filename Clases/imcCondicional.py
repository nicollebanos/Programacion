#--------------constantes-----------#
PREGUNTA_PESO = "Cuanto pesas en kg?: "
PREGUNTA_ESTATURA = "Cuanto mides en metros?: "
MENSAJE_BIENVE = "Hola, como estas? Voy a calcular tu IMC"
MENSAJE_DESPEDIDA = "Tú IMC es... {}%"
MENSAJE_BAJO_PESO = "Come ombe, estas delgado"
MENSAJE_NORMAL = "Estas en forma"
MENSAJE_SOBRE_PESO = "Abre el ojo, estas en sobre peso"
MENSAJE_OBESO = "Tú salud corre peligro, tate quieto estas obeso"

#--------------constantes-----------#
print(MENSAJE_BIENVE)
peso = float(input(PREGUNTA_PESO))
estatura = float (input(PREGUNTA_ESTATURA))
imc = peso/(estatura**2)
isBajoPeso = imc < 18.5 
isNormal = imc >= 18.5 and imc < 25

