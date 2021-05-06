# Hacer un gráfico de barras que represente 
# los niveles de ingresos de una persona durante 
# el 2020 puedes inventar los ingresos mes a mes

import matplotlib.pyplot as plt
ingresosxPersona = [400, 300, 430, 220, 500, 456, 600, 490, 650, 280, 710, 220]
meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']

plt.bar(meses, ingresosxPersona, width= 0.5, color = 'c')

plt.title('Niveles de ingresos de una persona en el 2020')
plt.xlabel('Meses')
plt.ylabel('Ingresos en miles')
plt.savefig('graficoIngresos.png')

plt.show()