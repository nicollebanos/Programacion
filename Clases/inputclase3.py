#----------------- constatnte -----------------#
PREGUNTA_NOMBRE = "Como te llamas?: "
PREGUNTA_EDAD = "Cuantos años tienes?: "
PREGUNTA_ESTATURA = "Cuanto mides?: "
#----------------- entrada de códigos -----------------#
nombre = input(PREGUNTA_NOMBRE)
print(f"Un gusto en conocerte {nombre}")
edad = int(input(PREGUNTA_EDAD))
print(f"{nombre} en 5 años tendras: {edad+5}")

print("Otra pregunta")
estatura = float(input(PREGUNTA_ESTATURA))
print("Muy amable, vuelva pronto")
