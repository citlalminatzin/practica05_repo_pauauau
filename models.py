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

def modelo_circ(longitudes: list[float]) -> list[float]:
    """
    longitudes: list[float] ¿Qué significa longitudes? 
    (Por favor elimina la pregunta y reemplazala con su respuesta)
    ...
    """
    ... # Puedes eliminar esta línea

import math

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

def calc_error(pred:list[float], truth: list[float]):
    """Calcula el error entre una predicción y la verdad del dataset"""

def main():
    ... # Puedes eliminar esta línea

if __name__ == "__main__":
    # Si necesitas hacer pruebas de tu función las puedes escribir acá
    main()
