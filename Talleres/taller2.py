saludo = "Bienvenid@"
# Generenado saludo
PREGUNTA_NOMBRE = "Como te llamas?: "
PREGUNTA_APELLIDO = "Para saber un poco más de ti antes de empezar, como te apellidas?: "
print("-"*5, "saludo", "-"*5)
nombre = input(PREGUNTA_NOMBRE)
apellido = input(PREGUNTA_APELLIDO)
print(f"{saludo} {nombre} {apellido} a nuestra base de datos matematicos")

# constantes
NUMERO1 = "Por favor digita un número: "
NUMERO2 = "Para continuar, digita otro número: "
PREGUNTA_EDAD = "Cuantos años tienes?: "
MENOR = "Usa este programa como modo de ayuda, estan en tu étapa de aprendizaje"
MAYOR = "Wou eres algo mayor para esto pero continua sin problema, estamos para ayudar"

# Edad intro
print("-"*5, "edad", "-"*5)
edad = int(input(PREGUNTA_EDAD))
if edad < 13: 
    print(MENOR)
elif edad > 13:
    print(MAYOR)

# Entrega de datos
print("-"*5, "número", "-"*5)
numeroA = input(NUMERO1)
numeroB = input(NUMERO2)
numA = float (numeroA)
numB = float (numeroB)

# Suma de datos
print("-"*5, "suma", "-"*5)
sumar = numA + numB
print(f"{sumar} es la suma entre ambos números")

# Resta de datos
print("-"*5, "resta", "-"*5)
resta = numA - numB
print(f"{resta} es la resta entre ambos números")

# Mutiplicación de datos
print("-"*5, "multiplicación", "-"*5)
multiplicar = numA * numB
print(f"{multiplicar} es la multiplicación entre ambos números")

# División de datos
print("-"*5, "división", "-"*5)
dividir = numA / numB
print(f"{dividir} es la división entre ambos números")

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
print(f"{despedida} {nombre} {apellido}")
