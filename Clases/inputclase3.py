#----------------- constatnte -----------------#
PREGUNTA_NOMBRE = "Como te llamas?: "
PREGUNTA_EDAD = "Cuantos años tienes?: "
PREGUNTA_ESTATURA = "Cuanto mides?: "
#----------------- entrada de códigos -----------------#
nombre = input(PREGUNTA_NOMBRE)
print(f"Un gusto en conocerte {nombre}")
edad = int(input(PREGUNTA_EDAD))
print(f"{nombre} en 5 años tendras: {edad+5}")
input("Te sientes vieja?: ")
if True : 
    print("Me encanta tu sinceridad")
else False: 
    print("Pues si lo eres, ACEPTALO")

print("Otra pregunta")
estatura = float(input(PREGUNTA_ESTATURA))
print("Muy amable, vuelva pronto")
