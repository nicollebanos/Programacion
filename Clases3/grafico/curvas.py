
import matplotlib.pyplot as plt

tiempo = [0,1,2,3,4,5]
sensor = [4,5,6,8,9,10]
plt.plot(tiempo,sensor,'--,c')
############
plt.title('Gráfico Sensor contra el tiempo')
plt.xlabel('Tiempo(s)')
plt.ylabel('Voltaje(mV)')
plt.savefig('sensor')
############
plt.show()

print('-----------------------------------------')
diccionario = {}
diccionario['NombresEstudiantes'] = ['Andre','Ignacio','Gabito','Lobo']
diccionario['EdadEstudiantes'] = [18,20,27,19]
diccionario['Peso'] = [65,72,64,57]
print(diccionario)

print('-------------------------------------------')
print(diccionario['NombresEstudiantes'][-1],diccionario['EdadEstudiantes'][-1],diccionario['Peso'][-1])