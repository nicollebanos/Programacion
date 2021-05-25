
# Pida al usuario que ingrese un párrafo y luego muestre en pantalla 
# cual es la palabra más grande, la palabra más pequeña. Valide que el párrafo
# ingresado termine en punto sino es así se debe pedir al usuario que ingrese 
# nuevamente el párrafo


def validateEndWith(strValidate, pregunta):
    isCorrectData = False
    while (isCorrectData == False):
        try:
            valor = input(pregunta)
            assert(valor.endswith(strValidate))
            isCorrectData = True
        except AssertionError:
            print(f'datos incorrectos ingrese nuevamente y recuerde que debe terminar con "{strValidate}" ')
    return valor 

parrafo =validateEndWith('.','ingrese un parrafo: ')
parrafo = parrafo[:-1]
palabras = parrafo.split(' ')
print(palabras)
print(f'la palabra más grande es "{max(palabras, key=len)}" y el menor es "{min(palabras, key=len)}"')
