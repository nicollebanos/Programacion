
# Se sabe que un Dólar son 0.82 euros, indique a un usuario que ingrese su 
# dinero en dolares y su nombre, luego muestre en pantalla el nombre del usuario y cuanto 
# dinero tiene en euros (recuerde validar que todos los datos ingresados por el usuario sean 
# del formato correcto).

isCorrectInfo = False
while(isCorrectInfo == False):
    try: 
        nombre = input('Ingrese su nombre: ')
        assert(nombre.isalpha())
        isCorrectInfo = True
    except AssertionError:
        print('Ingresaste un dato no valido')

isCorrectInfo = False
while(isCorrectInfo == False):
    try: 
        dolares = float(input('Ingrese tu dinero en dolares: '))
        isCorrectInfo = True
    except ValueError:
        print('Verifica bien, has ingresado un valor no valido')

euro = []
for elemento in dolares:
    conversor = round (elemento*0.82,2)
    dolares.append(conversor)

