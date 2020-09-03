
import sqlite3	
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

connectionObject = sqlite3.connect("templates/database/proyecto_python.db")
cursorObject = connectionObject.cursor()
# createTable = "CREATE TABLE DATA(id INTEGER,idPersona varchar(10), idSecion INTEGER, enojado REAL, disgusto REAL, miedo REAL, feliz REAL, triste REAL, sorpresa REAL, neutral REAL)"

# cursorObject.execute(createTable)

queryTable = "SELECT * from DATA"
queryResults = cursorObject.execute(queryTable)
print("Datos registrados:")
data = []
for result in queryResults:
    data.append(result[3:])
    # print(result)

label_mapdisgust = ['enojado', 'disgusto', 'miedo', 'feliz', 'triste', 'sorpresa', 'neutral']
x=np.array(data)
y=np.transpose(x)
# print(len(x.shape))
x = range(49)

fig, a = plt.subplots(7, sharex=True, sharey=True, gridspec_kw={'hspace': 0})

fig.suptitle('Emociones')
#Generamos una grafica lineal para una recta en X
a[0].plot(x, y[0])
a[0].text(-10, .4, 'Enojado')
#Generamos otra grafica lineal para una X cuadratica
a[1].plot(x, y[1], 'tab:orange')
a[1].text(-10, .4, 'Disgusto')
#Generamos una grafica lineas para una X Cubica
a[2].plot(x, y[2], 'tab:green')
a[2].text(-10, .4, 'Miedo')
#Agregamos las etiquetas y añadimos una leyenda.
a[3].plot(x, y[3], 'tab:red')
a[3].text(-10, .4, 'Feliz')
#Generamos otra grafica lineal para una X cuadratica
a[4].plot(x, y[4], 'tab:blue')
a[4].text(-10, .4, 'Triste')
#Generamos una grafica lineas para una X Cubica
a[5].plot(x, y[5], 'tab:green')
a[5].text(-10, .4, 'Sorpresa')
#Agregamos las etiquetas y añadimos una leyenda.
a[6].plot(x, y[6],  'tab:orange')
a[6].text(-10, .4, 'Neutral')

# plt.title("Simple Plot")
plt.legend()
plt.axis([0, 160, 0, 1])
# plt.savefig('grafica_lineal.png')
plt.show()
