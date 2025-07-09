import justpy as jp
import pandas
from datetime import datetime
from pytz import utc
import matplotlib.pyplot as plt

# Carga los datos desde un archivo CSV y convierte la columna 'Timestamp' a formato de fecha
data = pandas.read_csv("reviews.csv", parse_dates=['Timestamp'])
data['Day'] = data['Timestamp'].dt.date  # Extrae solo la fecha (sin hora)
day_average = data.groupby('Day')['Rating'].mean()  # Calcula el promedio de calificaciones por día

# Definición del gráfico en formato JSON con el formato de manejo de https://www.highcharts.com/
chart_def = """
{
    chart: {
        type: 'spline',
        inverted: false
    },
    title: {
        text: 'Atmosphere Temperature by Altitude'
    },
    subtitle: {
        text: 'According to the Standard Atmosphere Model'
    },
    xAxis: {
        reversed: false,
        title: {
            enabled: true,
            text: 'Altitude'
        },
        labels: {
            format: '{value}'
        },  
        accessibility: {
            rangeDescription: 'Range: 0 to 80 km.'
        },
        maxPadding: 0.05,
        showLastLabel: true
    },
    yAxis: {
        title: {
            text: 'Average Rating'
        },
        labels: {
            format: '{value}'
        },
        accessibility: {
            rangeDescription: 'Range: -90°C to 20°C.'
        },
        lineWidth: 2
    },
    legend: {
        enabled: false
    },
    tooltip: {
        headerFormat: '<b>{series.name}</b><br/>',
        pointFormat: '{point.x}: {point.y}'
    },
    plotOptions: {
        spline: {
            marker: {
                enable: false
            }
        }
    },
    series: [{
        name: 'Average Rating',
        data: [
            [0, 15], [10, -50], [20, -56.5], [30, -46.5], [40, -22.1],
            [50, -2.5], [60, -27.7], [70, -55.7], [80, -76.5]
        ]
    }]
}
"""

# Función principal que define la aplicación web
def app():
    # Crea una página Quasar
    wp = jp.QuasarPage()
    
    # Agrega un encabezado y una descripción
    h1 = jp.QDiv(a=wp, text="Analysis of Course Reviews", classes="text-h3 text-center q-pa-md")
    p1 = jp.QDiv(a=wp, text="These graphs represent course review analysis.")
    
    # Agrega un gráfico interactivo basado en HighCharts
    hc = jp.HighCharts(a=wp, options=chart_def)
    hc.options.title.text = 'Average Rating by Day'  # Cambia el título del gráfico
    
    # Configura los datos del gráfico
    hc.options.xAxis.categories = list(day_average.index)  # Fechas en el eje X
    hc.options.series[0].data = list(day_average)  # Promedios en el eje Y

    return wp

# Ejecuta la aplicación en el puerto 8080
jp.justpy(app, port=8080)
