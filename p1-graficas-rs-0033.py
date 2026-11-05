# Keyla Paola NC = 0033 | Fecha 5/nov/2026
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#crearemos nuestra tabla y la guardaremos con pandas
# Tenemos 5 listas de redes sociales con 4 elementos por lista 
fb = ['Facebook', 8833, True, 2006]
twt = ['Twitter', 8575, False, 2008]
ig = ['Instagram', 7575, True, 2010]
wsp = ['Whatsapp', 8828, True, 2009]
tel = ['Telegram', 2992, False, 2010]
lkn = ['Linkdin', 7277, False, 2012]
# Creamos una lista de listas (conformando la tabla)
lista_redes_sociales = [fb,twt,ig,wsp,tel,lkn]
# print(lista_redes_sociales)
# Utilizar Pandas para organizar la tabla (dataframe o marco de datos)
# a cada columna le agregan nombre 
df_redes_sociales = pd.DataFrame(lista_redes_sociales,columns=["Nombre","Cantidad","Es_FB","Año"])
#Creamos el archivo CSV y lo guardamos en CS
df_redes_sociales.to_csv("redessociales.csv", index=False)
print(df_redes_sociales)
#Crear grafica de lineas
# donde X es nombre en el eje horizontal 
# donde Y es cantidad en el eje vertical
plt.plot(df_redes_sociales["Nombre"], df_redes_sociales["Cantidad"])
plt.title ("Grafica redes sociales 0033")
plt.xlabel ("Nombre de las redes")
plt.ylabel ("Cantidad de usuarios")
# Mostrar Grafica
plt.show()

#Creamos una Grafica de Puntos 
plt.scatter(df_redes_sociales["Nombre"],df_redes_sociales["Cantidad"])
plt.title ("Grafica redes sociales 0033")
plt.xlabel ("Nombre de las redes")
plt.ylabel ("Cantidad de usuarios")
# Mostrar grafica
plt.show()

# Creamos una Grafica de barras 
plt.bar(df_redes_sociales["Nombre"],df_redes_sociales["Cantidad"])
plt.title ("Grafica redes sociales 0033")
plt.xlabel ("Nombre de las redes")
plt.ylabel ("Cantidad de usuarios")
# Mostrar grafica
plt.show()
# Ordenar la grafica de barras de manera horizontal
# de la mas grande la mas pequeña
df_rs_ordenar = df_redes_sociales.sort_values("Cantidad",ascending = False)
plt.bar(df_rs_ordenar["Nombre"],df_rs_ordenar["Cantidad"])
plt.title ("Grafica redes sociales 0033")
plt.xlabel ("Nombre de las redes")
plt.ylabel ("Cantidad de usuarios")
plt.show()

# Grafica con color 
plt.bar(df_rs_ordenar["Nombre"],df_rs_ordenar["Cantidad"],
        color = [ "b", "g", "c", "m", "y", "r"])
plt.title ("Grafica redes sociales 0033")
plt.xlabel ("Nombre de las redes")
plt.ylabel ("Cantidad de usuarios")
plt.show()
print(" ")
# Grafica de pastel
plt.pie(df_redes_sociales["Cantidad"],
        labels=df_redes_sociales["Nombre"])
plt.title("grafica de pastel Redes Sociales  NC = 0033")
plt.show()
print("Keyla Paola NC = 0033 | Fecha 5/nov/2026")