#--------- Constantes -----------#
MENSAJE_BIENVENIDA = "Hola, espero que estes bien"
PREGUNTA_NUMEROA = "Ingrese un número A: "
PREGUNTA_NUMEROB = "Ingrese un número B: "
MENSAJE_MAYOR = "El número A es mayor que B"
MENSAJE_MENOR = "El número A es menor que B"
MENSAJE_IGUAL = "El número A es igual a B"

#--------- Entrada de código -----------#
print(MENSAJE_BIENVENIDA)
numeroA = int(input(PREGUNTA_NUMEROA))
numeroB = int(input(PREGUNTA_NUMEROB))
isMayor = numeroA > numeroB
isMenor = numeroA < numeroB

if (isMayor): 
    print(MENSAJE_MAYOR)
elif (isMenor):
    print(MENSAJE_MENOR)
else:
    print(MENSAJE_IGUAL)
