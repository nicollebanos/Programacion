#  Pida a un usuario que ingrese sus 5 
# snacks favoritos y sus precios luego realice un gráfico de 
# barras con la información ingresada (recuerde poner titulo al 
# gráfico y a sus ejes también recuerde guardar el resultado en 
# un archivo png)

import matplotlib.pyplot as plt
snacksFav = ['Doritos', 'DeTodito', 'Trululu', 'jugo Hit', 'Choclitos']
precio = [3000, 1300, 2500, 3500, 2300]
plt.bar(snacksFav, precio, width= 0.5, color = 'c')

plt.title('Snack favoritos')
plt.xlabel('Precios')
plt.ylabel('Snacks')
plt.savefig('graficoSnackFav.png')
plt.show()


