""" 
data.py


Este archivo contiene funciones para leer y escribir datos en un csv en particular, suponen que el csv tiene una estructura específica, 
con columnas de longitud, peso y circunferencia máxima de los peces, y que cada fila corresponde a un pez distinto. 

Estas funciones permiten cargar los datos en listas de Python, así como agregar nuevas columnas al csv si es necesario. 
El objetivo es facilitar el manejo de los datos relacionados con los peces, como sus longitudes, circunferencias y pesos.
"""

import csv

def read_data(path="pescados.csv"):
    """
    Lee el archivo csv y devuelve:
    longitudes, circunferencias, pesos
    """
    
    longitudes = []
    circunferencias = []
    pesos = []

    with open(path, newline="", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)

        for fila in lector:
            longitudes.append(float(fila["longitud"]))
            circunferencias.append(float(fila["circunferencia_max"]))
            pesos.append(float(fila["peso"]))

    return longitudes, circunferencias, pesos

def agregar_circunferencia(path):
    "Función para agregar la columna de circunferencias al csv. "
    circunferencias = [24.77, 21.29, 27.94, 24.77, 21.59, 31.75, 22.86]

    filas = []

    with open(path, newline="", encoding="utf-8") as f:
        lector = csv.DictReader(f)

        for i, fila in enumerate(lector):
            fila["circunferencia_max"] = circunferencias[i]
            filas.append(fila)

    with open(path, "w", newline="", encoding="utf-8") as f:
        medidas = ["longitud", "peso", "circunferencia_max"]

        escritor = csv.DictWriter(f, fieldnames=medidas)
        escritor.writeheader()
        escritor.writerows(filas)
    
