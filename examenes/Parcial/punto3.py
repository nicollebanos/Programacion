# Crear una función que calcule y devuelva el área 
# de un triangulo recuerde que la formula del mismo es 
# (base*altura) /2. Pida las entradas que considere 
# necesarias

PREGUNTA_BIENVENIDA = 'Digite por favor los valores pedido para poder hallar el área del triangulo'
PREGUNTA_BASE = 'Digite la base del triangulo '
PREGUNTA_ALTURA = 'Digite la altura del triangulo '

#----------- BIENVENIDA ---------#
print(PREGUNTA_BIENVENIDA)

#--------- PREGUNTAS -----------#
print("-"*10, "Base", "-"*10)
base = int(input(PREGUNTA_BASE))

print("-"*10, "Altura", "-"*10)
altura = float(input(PREGUNTA_ALTURA))

#------- Procedimiento ---------#
print("-"*10, "Área", "-"*10)
def calcularArea (base, altura):
  return (base * altura)/2
area = calcularArea(base, altura)
print ('El área del triangulo es ', area)