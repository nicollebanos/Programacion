
import matplotlib.pyplot as plt

#se crean los labels sizes y explode
# Labels : Python, java, dart, js, Nombres porciones de torta
pieLabels = ['python', 'java', 'dart', 'js',]

#Sizes los tamaños de cada porción de la torta
sizes = [40,25,25,10]

#Explode: Que tan alejado del origen esta la torta
pieExplode = [0,0,0.1,0]

#Diferentes formas
#------- forma 1 -----------#
plt.pie(sizes)
#####################
plt.title('Uso de lenguajes de programación en el 2021')
plt.savefig('tortasLenguajes.png')
#####################
plt.show()

#------- forma 2 -----------#
plt.pie(sizes,labels=pieLabels)
#####################
plt.title('Uso de lenguajes de programación en el 2021')
plt.savefig('tortasLenguajes.png')
#####################
plt.show()

#------- forma 3 -----------#
pieExplode = [0,0,0.2,0]
plt.pie(sizes,labels=pieLabels, explode=pieExplode)
#####################
plt.title('Uso de lenguajes de programación en el 2021')
plt.savefig('tortasLenguajes.png')
#####################
plt.show()

#------- forma 4 -----------#
pieExplode = [0,0,0.2,0]
plt.pie(sizes,labels=pieLabels, explode=pieExplode, shadow= True)
#####################
plt.title('Uso de lenguajes de programación en el 2021')
plt.savefig('tortasLenguajes.png')
#####################
plt.show()

#------- forma 5 -----------#
pieExplode = [0,0,0.2,0]
plt.pie(sizes,labels=pieLabels, explode=pieExplode, shadow= True, startangle= 45)
#####################
plt.title('Uso de lenguajes de programación en el 2021')
plt.savefig('tortasLenguajes.png')
#####################
plt.show()

#------- forma 6 -----------#
def etiquetarElementosPorcentuales(sizes, labels, indicador= ' ->'):
    acumulador = 0
    for elemento in sizes :
        acumulador += elemento

    for i in range (len(labels)):
        pieLabels[i] += indicador+str(sizes[i]/acumulador*100) +'%'
pieExplode = [0,0,0.2,0]
acumulador = 0
sizes = [50,25,15,10]
pieLabels = ['python', 'java', 'dart', 'js',]
etiquetarElementosPorcentuales(sizes,pieLabels,'☺')

plt.pie(sizes,labels=pieLabels, 
        explode=pieExplode, 
        shadow= True, 
        counterclock = True, 
        startangle= 45)
#####################
plt.title('Uso de lenguajes de programación en el 2021')
plt.savefig('tortasLenguajes.png')
#####################
plt.show()