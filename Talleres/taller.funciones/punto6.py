
#--------- Se sabe que el IMC se calcula dividiendo el peso por la altura al cuadrado, 
#--------- realice una función que lo calcule

SALUDO_BIENVENIDA = 'Bienvenido al sitio donde calcularas tu IMC'
PREGUNTA_NOMBRE = 'Como te llamas: '
PREGUNTA_PESO = 'Cuanto pesas? '
PREGUNTA_ESTATURA = 'Cuanto mides? '

#----------- BIENVENIDA ---------#
nombre = input(PREGUNTA_NOMBRE) 
print(SALUDO_BIENVENIDA, nombre)

#--------- PREGUNTAS -----------#
print("-"*10, "peso", "-"*10)
peso = int(input(PREGUNTA_PESO))

print("-"*10, "estatura", "-"*10)
estatura = float(input(PREGUNTA_ESTATURA))

#------- Procedimiento ---------#
print("-"*10, "IMC", "-"*10)
def calcularIMC (peso, altura):
  return peso /(altura**2)
imc = calcularIMC(peso, estatura)
print ('Tu IMC es', imc)