
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
   longitudes, circunferencias, pesos = read_data()
   
   pred_geom = modelo_geom(longitudes)
   pred_circ = modelo_circ(longitudes, circunferencias)
   
   make_plot(pred_geom,pesos,"Modelo geométrico")
   make_plot(pred_circ,pesos,"Modelo con circunferencia máxima")

if __name__ == "__main__":
    main()
