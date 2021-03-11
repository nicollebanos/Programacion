
PREGUNTA_NUMERO = ''' Ingrese alguna de estas opciones:
                    1. Hacer conversioón de pesos a dolares o Euros
                    2. Agerege un valor a la lista de pesos
                    3. Mostrar vaor más alto, más bajo y promedio
                    4. Eliminar elemento de la lista
                    5. Salir
'''


listaPesos = [20000,30000,4000,2500,1000,7600]
opcionEscogida = int(input(PREGUNTA_NUMERO))
while(opcionEscogida !=5):
    is1 = opcionEscogida == 1
    is2 = opcionEscogida == 2
    is3 = opcionEscogida == 3
    is4 = opcionEscogida == 4
    isnotvalid = opcionEscogida != 5
    if(is1):
        print('Escogiste 1')
    elif(is2):
        print('Escogistes 2')
    elif(is3):
        print('Escogiste 3')
    elif(is4):
        print('Escogiste 4')
    else:
        print('Respuesta no valida')
    opcionEscogida = int(input(PREGUNTA_NUMERO))

print('Felix día')