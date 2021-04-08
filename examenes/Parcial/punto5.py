# se sabe que la sucesión de 
# Fibonacci sigue el siguiente patrón 
# 0,1,1,2,3,5,8,13,21,34,55,89,144, …. Se le pide como 
# ingeniero biomédico, que dado un número n de la 
# sucesión muestre en pantalla su valor. Por ejemplo, si el 
# usuario digita 3 se mostrará 1 y si el usuario digita 5 
# mostrará 3 si ingresa 100 debe mostrar el número que le 
# corresponda en la sucesión.

listaFibonacci = [0,1,1,2,3,5,8,13,21,34,55,89,144]

#------Bienvenida --------#
print('Digite un número y se le dara el número que se encuentre en esa posición de la lista')

#------ Pregunta número ------#
PREGUNTA_NUMERO = 'Digite un número: '
pregunta = input(PREGUNTA_NUMERO)
print(pregunta)

def mostrarListaFibo (lista):
    a = 0
    b = 1
    for lista in range(lista-1):
        secuencia = a+b
        a = b
        b = secuencia
    return(a)

posicion = mostrarListaFibo(3)

print(posicion)

