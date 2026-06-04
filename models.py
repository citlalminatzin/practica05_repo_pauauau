"""
models.py

Este archivo contiene las funciones principales para los modelos de similitud
geométrica de la Práctica 5. Se encarga de transformar las variables físicas
de los peces como sus longitudes y circunferencias para predecir su peso, así como de 
evaluar el ajuste y el error de los modelos propuestos.
"""

import numpy as np

def modelo_geom(longitudes: list[float]) -> list[float]:
    """
    longitudes: Lista con las medidas de la longitud de los peces en cm.
    Esta función retorna una lista con las longitudes al cubo
    """
    return [l**3 for l in longitudes]

def pearson(x: list[float], y: list[float]) -> float:
    n = len(x)
    
    
    promedio_x = sum(x) / n
    promedio_y = sum(y) / n
    
    numerador = 0.0
    denominador_x = 0.0
    denominador_y = 0.0
    

    for i in range(n):
        dif_x = x[i] - promedio_x
        dif_y = y[i] - promedio_y
        
        numerador += dif_x * dif_y
        denominador_x += dif_x ** 2
        denominador_y += dif_y ** 2
        
    denominador_total = math.sqrt(denominador_x * denominador_y)
    
    return numerador / denominador_total

def modelo_circ(longitudes: list[float], circunferencias: list[float]) -> list[float]:
    """longitudes: Lista con las medidas de la longitud de los peces en cm. 
       circunferencias: medidas de la circunferencia de los peces en cm."""

    return [longitudes[i] * (circunferencias[i]**2) for i in range(len(longitudes))]


def calc_error(pred:list[float], truth: list[float]):
    """Calcula el error entre una predicción y la verdad del dataset"""
    n = len(pred)
    suma_errores_cuadrados = 0.0
    
    for i in range(n):
        diferencia = pred[i] - truth[i]
        suma_errores_cuadrados += diferencia ** 2
        
    return suma_errores_cuadrados / n

def main():
    ... # Puedes eliminar esta línea

if __name__ == "__main__":
    # Si necesitas hacer pruebas de tu función las puedes escribir acá
    main()
