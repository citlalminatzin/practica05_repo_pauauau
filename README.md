# Reposición de Práctica 5

## Autor

Paulina Alba Pérez

## Uso e instalación

Para ejecutar el proyecto se requieren las siguientes bibliotecas:

* `matplotlib`
* `math`
* `csv`

### Archivos del proyecto

* `main.py`: Contiene el código principal para generar las gráficas y comparar los modelos.
* `models.py`: Implementa los modelos matemáticos y las funciones de evaluación.
* `data.py`: Contiene las funciones para leer y modificar los datos almacenados en el archivo CSV.

---

## Ejercicio 1

Se consideran las siguientes mediciones de longitud y peso de distintos peces. Estos datos serán utilizados para evaluar los modelos propuestos en los ejercicios posteriores.


### Tabla de datos

| Longitud | Peso |
| -------- | ---- |
| 36.81    | 0.78 |
| 31.77    | 0.47 |
| 36.81    | 1.16 |
| 36.82    | 0.74 |
| 32.07    | 0.44 |
| 45.07    | 1.40 |
| 35.89    | 0.64 |

---

## Ejercicio 2: Modelo de similitud geométrica

En este ejercicio se utilizó el modelo de similitud geométrica, el cual asume que el peso de un pez es proporcional al cubo de su longitud: $W \propto l^3$

a partir de esta relación se observa que pequeñas variaciones en la longitud producen cambios significativamente mayores en el peso. Esto se debe al crecimiento cúbico del modelo, que aproxima cómo aumenta el volumen de un cuerpo cuando todas sus dimensiones se escalan proporcionalmente.

### ¿Qué tan bueno es el ajuste?

La gráfica de dispersión muestra una relación positiva entre las predicciones del modelo y los pesos observados. Esto indica que la longitud es una variable importante para explicar el peso de los peces. Sin embargo, los puntos no se encuentran perfectamente alineados, por lo que el modelo no explica toda la variabilidad presente en los datos.

### ¿Hay algún efecto que nuestro modelo no capture?

Si. El modelo supone que todos los peces mantienen exactamente la misma forma geométrica al cambiar de tamaño. En la práctica, peces con la misma longitud pueden presentar diferencias en su grosor o anchura, lo que genera variaciones en su peso que no son capturadas únicamente por la longitud.

---

## Ejercicio 3: Modelo con circunferencia máxima

Partiendo de la aproximación del volumen mediante la longitud y el área transversal máxima, se obtuvo el modelo

$$W \propto lC_{\max}^{2}$$

donde $(l)$ representa la longitud del pez y $(C_{\max})$ su circunferencia máxima.

### ¿Cómo queda la fórmula explícita del modelo?

La forma explícita es

$$W = k,lC_{\max}^{2}$$

donde (k) es una constante de proporcionalidad que depende de las unidades utilizadas y de la densidad promedio del pez.

### ¿Qué tan bueno es el ajuste?

El modelo que incorpora la circunferencia máxima presenta un mejor ajuste que el modelo basado únicamente en la longitud. Esto se debe a que incluye información adicional sobre el grosor del pez, lo que permite aproximar mejor su volumen y, en consecuencia, su peso.

Visualmente, los puntos se encuentran más cercanos a una relación lineal entre las predicciones y los datos observados. Además, las métricas de evaluación muestran una mejora respecto al modelo geométrico simple.

### Conclusión del ejercicio

La incorporación de la circunferencia máxima permite capturar diferencias de forma entre peces de longitudes similares. Por ello, el modelo

$$W \propto lC_{\max}^{2}$$

proporciona una descripción más realista y precisa del peso de los peces que el modelo basado únicamente en

$$W \propto l^3.$$

---

## Conclusión

Esta práctica permitió estudiar cómo los principios de similitud geométrica pueden utilizarse para construir modelos matemáticos capaces de predecir propiedades físicas de organismos reales. Además, mostró la importancia de incorporar variables adicionales cuando un modelo resulta demasiado simplificado.

Al comparar ambos enfoques, se observó que incluir información sobre la circunferencia máxima mejora la capacidad predictiva del modelo, ya que captura características de la forma del pez que no pueden describirse únicamente mediante su longitud.

Desde el punto de vista computacional, la práctica también permitió trabajar con lectura de datos, manipulación de archivos CSV, construcción de funciones reutilizables y visualización de resultados mediante gráficas.

