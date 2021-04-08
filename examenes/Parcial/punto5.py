# se sabe que la sucesión de 
# Fibonacci sigue el siguiente patrón 
# 0,1,1,2,3,5,8,13,21,34,55,89,144, …. Se le pide como 
# ingeniero biomédico, que dado un número n de la 
# sucesión muestre en pantalla su valor. Por ejemplo, si el 
# usuario digita 3 se mostrará 1 y si el usuario digita 5 
# mostrará 3 si ingresa 100 debe mostrar el número que le 
# corresponda en la sucesión.

listaFibonacci = [0,1,1,2,3,5,8,13,21,34,55,89,144]

def mostrarListaFibo (valor):
    valor1 = 0
    valor2 = 1
    for elemento in range(valor-1):
        secuencia = valor1+valor2
        valor1 = valor2
        valor2 = secuencia
    return(valor1)
posicion = mostrarListaFibo(5)
print(posicion)

