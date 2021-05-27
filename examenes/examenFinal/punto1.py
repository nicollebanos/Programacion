
# Solicite a un usuario que ingrese sus 8 alimentos favoritos y sus precios 
# luego realice un gráfico de barras con la información ingresada (recuerde poner título al 
# gráfico y a sus ejes también recuerde guardar el resultado en un archivo png)

import matplotlib.pyplot as plt
PREGUNTA_ALIMEN_FAV = 'Ingrese su alimento favorito: '
PREGUNTA_PRECIOS = 'Ingrese el precio: '
alimenFav = []
precios = []
for i in range (8):
    alimen = input(PREGUNTA_ALIMEN_FAV)
    alimenFav.append(alimen)
    precio = float(input(PREGUNTA_PRECIOS))
    precios.append(precio)

plt.bar(alimenFav, precios, width= 0.5, color = 'c')
plt.title('Alimentos favoritos')
plt.xlabel('Alimentos')
plt.ylabel('Precios')
plt.savefig('graficoAlimenFav.png')
plt.show()
