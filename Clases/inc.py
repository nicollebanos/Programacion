#--------------constantes-----------#
PREGUNTA_PESO = "Cuanto pesas en kg?: "
PREGUNTA_ESTATURA = "Cuanto mides en metros?: "
MENSAJE_BIENVE = "Hola, como estas? Voy a calcular tu IMC"
MENSAJE_DESPEDIDA = "Tú IMC es... {}%"

#--------------constantes-----------#
print(MENSAJE_BIENVE)
peso = float(input(PREGUNTA_PESO))
estatura = float (input(PREGUNTA_ESTATURA))
imc = peso/(estatura**2)
print(MENSAJE_DESPEDIDA.format(imc))
isObeso = imc >= 30
print("El resultado de la prueba de obecidad es ...", isObeso)
