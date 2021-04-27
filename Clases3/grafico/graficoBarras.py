#Aqui explicaremos como hacer un grafico de barras

import matplotlib.pyplot as plt 
lenguaje = ['py', 'java', 'dart', 'ts', 'elixir']
encuesta = [50,10,20,10,10]
plt.bar(lenguaje, encuesta)
###############################
plt.title('Lenguajes más usados')
plt.xlabel('Lenguaje de programación')
plt.ylabel('% de uso de lenguaje')
plt.savefig('graficoLenguaje.png')

##############################
plt.show()