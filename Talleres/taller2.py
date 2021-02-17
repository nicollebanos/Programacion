saludo = "Bienvenid@"
# Generenado saludo
PREGUNTA_NOMBRE = "Como te llamas?: "
print("-"*5, "saludo", "-"*5)
nombre = input(PREGUNTA_NOMBRE)
print(f"{saludo} {nombre} a nuestra base de datos matematicos")

# constantes
NUMERO1 = "Por favor digita un número: "
NUMERO2 = "Para continuar, digita otro número: "

# Entrega de datos
print("-"*5, "número", "-"*5)
numeroA = input(NUMERO1)
numeroB = input(NUMERO2)
numA = float (numeroA)
numB = float (numeroB)

# Suma de datos
print("-"*5, "suma", "-"*5)
sumar = numA + numB
print(f"la suma dio {sumar} exitosamente")

# Resta de datos
print("-"*5, "resta", "-"*5)
resta = numA - numB
print(f"la resta dio {resta} exitosamente")

# Mutiplicación de datos
print("-"*5, "multiplicación", "-"*5)
multiplicar = numA * numB
print(f"la multiplicación dio {multiplicar} exitosamente")

# División de datos
print("-"*5, "división", "-"*5)
dividir = numA / numB
print(f"la división dio {dividir} exitosamente")

#Calculando que número es mayor
print("-"*5, "orden números", "-"*5)
if numA < numB: 
    print("El número mayor es:", numB)
elif numA > numB:
    print("El número mayor es:", numA)
elif numA == numB:
    print("Los números son iguales")

# Generenado despedida
despedida = "Muchas gracias, vuelva pronto"
print("-"*5, "despedida", "-"*5)
print(f"{despedida} {nombre}")
