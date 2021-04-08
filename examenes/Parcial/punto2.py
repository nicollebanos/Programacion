
# Crear una función que dada tres listas del mismo 
# tamaño las muestre en pantalla


def mostrarLista (lista):
  for elemento in lista :
    print (elemento)

nombres = ['Gabito', 'Nacho', 'Lobito', 'Hugo', 'Nicky']
edades = [17, 20, 19, 21, 18]
estatura = [1.57, 1.60, 1.64, 1.70, 1.71]

print('#----- Lista nombres -----#')
mostrarLista(nombres)

print('#----- Lista edades -----#')
mostrarLista(edades)

print('#----- Lista estaturas -----#')
mostrarLista(estatura)