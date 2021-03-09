
nombres = ['Santy','Samu','Aleja','Dani']
print(nombres)
print(nombres[2])
nombres.append('Mauricio')
print(nombres)
print(nombres[2])

edades = [18, 19, 20, 17]
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

#mayor de la lista
mayor = max(edades)
print(mayor)
menor = min(edades)
print(menor)