
# Desarrollar un gráfico de torta que represente 
# las cinco ciudades de Colombia debes sobresalir 
# la ciudad más grande.

import matplotlib as plt 
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
plt.savefig('GraficoCortaCiudades.png')
plt.show()