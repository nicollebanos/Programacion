# Dos números - mayor - iguales

#Constantes
MENSAJE_BIENVENIDA = "Buenas, espero que se enceuntre muy bien"
MENSAJE_SALIDA = "Mucgras gracias, vuelva pronto"
NUMERO1 = "Digite un número: "
NUMERO2 = "Para continuar, digite otro número: "

print("-----------------------------------------")
print(MENSAJE_BIENVENIDA)
print("-----------------------------------------")
# Datos
numeroA = input(NUMERO1)
numeroB = input(NUMERO2)
numA = float(numeroA)
numB = float(numeroB)

#Código
print("Comparación mayor, menor o igual")
if (numA > numB):
    print("El número ", numA, " es mayor que ", numB)
elif (numA < numB):
    print("El número ", numA, " es menor que ",numB)
else:
    print("Los números ", numA, " son iguales")
input()