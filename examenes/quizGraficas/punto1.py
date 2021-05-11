#  Pida a un usuario que ingrese sus 5 
# snacks favoritos y sus precios luego realice un gráfico de 
# barras con la información ingresada (recuerde poner titulo al 
# gráfico y a sus ejes también recuerde guardar el resultado en 
# un archivo png)

PREGUNTA_SNACKS = 'Ingrese sus 5 snacks favoritos'
PREGUNTA_PRECIOS = 'Ingrese los precios'


import matplotlib.pyplot as plt

snacksFav = input(PREGUNTA_SNACKS)
precios = float(input(PREGUNTA_PRECIOS))

