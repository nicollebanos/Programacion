# Pida a un usuario que ingrese sus 5 
# ciudades favoritos en el mundo y sus poblaciones luego 
# realice un gráfico de torta con la información ingresada y 
# resalte la ciudad con mayor población (recuerde poner titulo 
# al gráfico y a sus ejes también recuerde guardar el resultado 
# en un archivo png)

import matplotlib.pyplot as plt 
PREGUNTA_CIUDADES_FAV = 'Ingrese su ciudad fav del mundo: '
PREGUNTA_POBLACION = 'Ingrese el número de población: '
pieLabels = []
sizes = []
for i in range (5):
    ciudad = input(PREGUNTA_CIUDADES_FAV)
    pieLabels.append(ciudad)
    poblacioon = float(input(PREGUNTA_POBLACION))
    sizes.append(poblacioon)

print(sizes)
maximo = sizes.index(max(sizes))
pieExplode = [0, 0, 0, 0, 0] 

pieExplode[maximo] = 0.1

def etiquetarElementosPorcentuales(sizes, labels, indicador= ' ->'):
    acumulador = 0
    for elemento in sizes :
        acumulador += elemento
    for i in range (len(labels)):
        porcentaje = round(sizes[i]/acumulador*100, 2)
        pieLabels[i] += indicador+str(porcentaje) +' Millones de habitantes '

etiquetarElementosPorcentuales(sizes, pieLabels, '-')

plt.pie(sizes,labels=pieLabels, explode=pieExplode, shadow= True, counterclock = True, startangle= 45)
plt.title('Ciudades favoritas')
plt.savefig('GraficoTortaCiudades.png')
plt.show()