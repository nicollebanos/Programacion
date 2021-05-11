# Pida a un usuario que ingrese sus 5 
# ciudades favoritos en el mundo y sus poblaciones luego 
# realice un gráfico de torta con la información ingresada y 
# resalte la ciudad con mayor población (recuerde poner titulo 
# al gráfico y a sus ejes también recuerde guardar el resultado 
# en un archivo png)

import matplotlib.pyplot as plt 
pieLabels = ['Medellín', 'Bogota', 'Cali', 'Barranquilla', 'Cartagena']
sizes = [2.5 ,10.4, 2.4, 1.2, 1] #tamaño de las porciones
pieExplode = [0, 0.1, 0, 0, 0] #alejamineto del origen

def etiquetarElementosPorcentuales(sizes, labels, indicador= ' ->'):
    acumulador = 0
    for elemento in sizes :
        acumulador += elemento
    for i in range (len(labels)):
        porcentaje = round(sizes[i]/acumulador*100, 2)
        pieLabels[i] += indicador+str(porcentaje) +'Millones de habitantes'

etiquetarElementosPorcentuales(sizes, pieLabels, '-')

plt.pie(sizes,labels=pieLabels, explode=pieExplode, shadow= True, counterclock = True, startangle= 45)
plt.title('Las 5 ciudades más grandes de Colombia')
plt.savefig('GraficoTortaCiudades.png')
plt.show()