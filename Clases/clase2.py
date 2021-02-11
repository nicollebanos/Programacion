pruebav = True
pruebaf = False

print(pruebav)
print(pruebaf)

edad = 19
estatura =  1.57
peso = 45
NOMBRE = "Nicolle Baños Siolo"
# calculando si es mayor de edad
print("-"*5, "mayor de edad", "-"*5)
isMayorEdad = edad>= 18
print(isMayorEdad) 
# calculando sobre la estatura 
print("-"*5, "bajo la estatura promedio", "-"*5)
isMayorEstatura = estatura < 1.60
print(isMayorEstatura)
# calculando peso difetente al dado
print("-"*5, "peso diferente", "-"*5)
isPesoDiferente = peso!= 45
print(isPesoDiferente)
# ver si un apellido esta en el nobre compelto
apellido = "Baños"
isApellido = apellido in NOMBRE 
print("-"*5, "esta el apellido en el nombre completo", "-"*5)
print(isApellido)