"""
main.py

Este archivo coordina la ejecución de la práctica. Primero agrega al
archivo de datos la información de las circunferencias máximas de los peces,
luego carga los datos desde el CSV y genera las predicciones de los dos
modelos estudiados: el modelo de similitud geométrica basado en la longitud
al cubo y el modelo que incorpora la circunferencia máxima.

Finalmente, produce gráficas de dispersión que comparan las predicciones de
cada modelo con los pesos reales observados, permitiendo evaluar visualmente
su capacidad de ajuste.
"""


import matplotlib.pyplot as plt
from models import calc_error, modelo_geom, modelo_circ
from data import read_data, agregar_circunferencia

agregar_circunferencia("pescados.csv")

def make_plot(predicciones, pesos, titulo):
    """
    Grafica la estimación de un modelo contra los datos reales.
    """

    plt.figure()

    plt.scatter(predicciones, pesos)

    plt.title(titulo)
    plt.xlabel("Predicción del modelo")
    plt.ylabel("Peso real")

    plt.show()

def main():
    """Lee los datos de los peces, calcula las predicciones de ambos modelos
    y genera las gráficas que comparan dichas predicciones con los pesos
    reales del conjunto de datos."""

    longitudes, circunferencias, pesos = read_data()
    pred_geom = modelo_geom(longitudes)
    pred_circ = modelo_circ(longitudes, circunferencias)
    
    make_plot(pred_geom,pesos,"Modelo geométrico")
    make_plot(pred_circ,pesos,"Modelo con circunferencia máxima")

if __name__ == "__main__":
    main()
