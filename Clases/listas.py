
nombres = ['Santy','Samu','Aleja','Dani']
print(nombres)
print(nombres[2])
nombres.append('Mauricio')
print(nombres)
print(nombres[2])

edades = [18, 19, 20, 17,32, 12, 15, 13]
estaturas = [1.62, 1.80, 1,67, 1.89]
# al último
print(edades[-2])
print(edades[0:2])
print(edades[:3])
print(edades[2:])
print(edades[:])

#Orden
edades.sort()
print(edades)
edades.sort(reverse=True)
print(edades)

#mayor y menor de la lista
mayor = max(edades)
print(mayor)
menor = min(edades)
print(menor)

#como contamos cuantos elementos hay?
largoListaEdades = len(edades)
print(largoListaEdades)

#como contamos cuantos elementos hay?
largoListaNombres = len(nombres)
print(largoListaNombres)

#Como sumamos elementos?
sumaEdades = sum(edades)
print(sumaEdades)

#Como calculo el promedio
promedioEdades = sumaEdades/largoListaEdades
print(promedioEdades)

#eliminar un elemento
edades.pop(2)
print(edades)

#nombres --> ciclo for y las listas
largoListaEdades = len(edades)
for indice in range (largoListaEdades):
    print(edades[indice])

#listado nombres largo
largoListaEdades = len(nombres)
for indice in range (largoListaNombres):
    print(nombres[indice])

#posiciones lista par
posicionesPares = []
largoListaEdades = len(edades)
for posicion in range (largoListaEdades):
    if(edades[posicion]%2 == 0):
        posicionesPares.append(posicion)

print(edades)
print(posicionesPares)

#solo cuando nos interese mostrar la lista
for edad in edades:
    print(edad)
for nombre in nombres:
    print(nombre)
    print(posicion)
    posicion+=1

posicion = 0
posicionesPares = []
for edad in edades:
    if(edad%2 == 0):
        posicionesPares.append(posicion)
    posicion+=1
print(posicionesPares)
