# Data Visualization Project

Este proyecto está diseñado para analizar y visualizar datos de reseñas de cursos utilizando gráficos interactivos y dinámicos. El objetivo principal es proporcionar una representación visual clara y comprensible de los datos para facilitar el análisis y la toma de decisiones.

## Características principales

- **Gráficos interactivos**: Utiliza gráficos de líneas, gráficos de pastel y otros tipos de visualizaciones para representar datos.
- **Análisis de datos**: Procesamiento y agrupación de datos para extraer información útil.
- **Interfaz web**: Implementación de una interfaz web interactiva utilizando la biblioteca JustPy.

## Librerías y dependencias utilizadas

El proyecto utiliza las siguientes librerías y dependencias:

- **JustPy**: Framework de Python para crear aplicaciones web interactivas y visualizaciones.
- **Pandas**: Biblioteca para la manipulación y análisis de datos.
- **Matplotlib**: Biblioteca para la creación de gráficos estáticos, animados e interactivos.
- **Datetime**: Módulo estándar de Python para manejar fechas y horas.
- **Pytz**: Biblioteca para trabajar con zonas horarias.

## Estructura del proyecto

El proyecto está dividido en varios módulos, cada uno de los cuales se centra en un tipo específico de visualización o análisis de datos. Los scripts incluyen:

1. **0-simple-app.py**: Una aplicación básica que muestra un encabezado y una descripción estática. Es ideal como punto de partida para entender la estructura de una aplicación JustPy.

2. **1-av-rat-day.py**: Visualiza la calificación promedio por día utilizando un gráfico de líneas. Los datos se agrupan por fecha y se calcula el promedio de las calificaciones.

3. **2-av-rat-week.py**: Representa la calificación promedio por semana en un gráfico de líneas. Los datos se agrupan por semana del año y se calcula el promedio de las calificaciones.

4. **3-av-rat-month.py**: Muestra la calificación promedio por mes en un gráfico de líneas. Los datos se agrupan por mes y se calcula el promedio de las calificaciones.

5. **4-av-rat-crs-mon.py**: Visualiza la cantidad de calificaciones por curso y por mes en un gráfico de líneas. Los datos se agrupan por curso y mes, y se cuentan las calificaciones.

6. **5-av-rat-crs-mon-stream.py**: Representa la cantidad de calificaciones por curso y por mes en un gráfico de tipo "streamgraph". Este tipo de gráfico es útil para observar tendencias a lo largo del tiempo.

7. **6-av-rat-crs-day-spline.py**: Muestra las calificaciones promedio agregadas por día de la semana en un gráfico de líneas. Los datos se agrupan por día de la semana y se calcula el promedio de las calificaciones.

8. **7-rat-crs-pie.py**: Representa la distribución de calificaciones por curso en un gráfico de pastel. Los datos se agrupan por curso y se cuentan las calificaciones.


## Cómo ejecutar el proyecto

1. Asegúrate de tener Python instalado en tu sistema.
2. Instala las dependencias necesarias utilizando `pip install -r requirements.txt` (si se proporciona un archivo de requisitos).
3. Ejecuta cualquiera de los scripts para iniciar la aplicación correspondiente. Por ejemplo:
   ```bash
   python 1-av-rat-day.py
4. Abre tu navegador web y accede a `http://localhost:8080` para interactuar con la aplicación.
   
## Fuente de datos
   
El proyecto utiliza un archivo CSV llamado `reviews.csv` que contiene datos de reseñas de cursos. Este archivo debe estar en el mismo directorio que los scripts para que las aplicaciones funcionen correctamente.