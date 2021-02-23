# Dos números - mayor - iguales

#Constantes
MENSAJE_BIENVENIDA = "Buenas, espero que te encuentres muy bien"
MENSAJE_SALIDA = "Muchras gracias, vuelva pronto"
PREGUNTA_NOMBRE = "Cúal es tu nombre?: "
NUMERO1 = "Digite un número: "
NUMERO2 = "Para continuar, digite otro número: "

print("---------------Bienvenida---------------------")
nombre = input(PREGUNTA_NOMBRE) 
print(MENSAJE_BIENVENIDA, nombre)
print("----------------números----------------------")
# Datos
numeroA = input(NUMERO1)
numeroB = input(NUMERO2)
numA = float(numeroA)
numB = float(numeroB)

#Códigos
if (numA > numB):
    print("El número ", numA, " es mayor que ", numB)
elif (numA < numB):
    print("El número ", numA, " es menor que ",numB)
else:
    print("Ambos números son iguales:", numA)