#-----------------Importar datos-----------------#
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

#-----------------Corroborar datos-----------------#
datos_hombres = pd.read_csv("tabla_hombres.csv")
datos_mujeres = pd.read_csv("tabla_mujeres.csv")
datos_totales = pd.concat([datos_mujeres, datos_hombres])

datos_totales.info()
datos_totales.head()

#-----------------Grafica-----------------#
sb.scatterplot(x = "altura", y = "peso", data = datos_totales,
               hue = "peso", palette = "coolwarm")
#plt.show()

#-----------------Caracteristicas (x) y etiqueta (y)-----------------#
X_hombre = datos_hombres["altura"]
y_hombre = datos_hombres["peso"]

X_mujeres = datos_mujeres["altura"]
y_mujeres = datos_mujeres["peso"]

X = datos_totales["altura"]
y = datos_totales["peso"]

#print(X_hombre, y_hombre, X_mujeres, y_mujeres)
#print("#" * 50)

#-----------------Ajustes de posicion-----------------#
X1_procesada = X_hombre.values.reshape(-1, 1)
X2_procesada = X_mujeres.values.reshape(-1, 1)

y1_procesada = y_hombre.values.reshape(-1, 1)
y2_procesada = y_mujeres.values.reshape(-1, 1)

#print(X1_procesada)
#print(y1_procesada)

#print(X2_procesada)
#rint(y2_procesada)

#-----------------Modelo de regresion Lineal-----------------#
modelo_hombre = LinearRegression()
modelo_hombre.fit(X1_procesada, y1_procesada)

modelo_mujer = LinearRegression()
modelo_mujer.fit(X2_procesada, y2_procesada)
#-----------------Prediccion-----------------#
genero = int(input("Escoja su genero: \n 1: Mujer \n 2: Hombre \n"))
if genero == 1:
    altura_mujer = float(input("Ingrese su altura: "))
    prediccion_mujer = modelo_mujer.predict([[altura_mujer]])
    print(f'Tu altura de {altura_mujer} cm significa que pesas {prediccion_mujer}. Nivel de error {modelo_mujer.score(X2_procesada, y2_procesada)}')
elif genero == 2:
    altura_hombre = float(input("Ingrese su altura: "))
    prediccion_hombre = modelo_hombre.predict([[altura_hombre]])
    print(f'Tu altura de {altura_hombre} cm significa que pesas {prediccion_hombre}. Nivel de error {modelo_hombre.score(X1_procesada, y1_procesada)}')
else:
    print("Dato incorrecto")