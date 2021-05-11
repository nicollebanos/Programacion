#  Pida a un usuario que ingrese sus 5 
# snacks favoritos y sus precios luego realice un gráfico de 
# barras con la información ingresada (recuerde poner titulo al 
# gráfico y a sus ejes también recuerde guardar el resultado en 
# un archivo png)

import matplotlib.pyplot as plt
PREGUNTA_SNACK_FAV = 'Ingrese un snack favorito: '
PREGUNTA_PRECIOS = 'Ingrese los precios: '
snacksFav = []
precios = []
for i in range (5):
    snacks = input(PREGUNTA_SNACK_FAV)
    snacksFav.append(snacks)
    precio = float(input(PREGUNTA_PRECIOS))
    precios.append(precio)

plt.bar(snacksFav, precios, width= 0.5, color = 'c')
plt.title('Snack favoritos')
plt.xlabel('Precios')
plt.ylabel('Snacks')
plt.savefig('graficoSnackFav.png')
plt.show()


