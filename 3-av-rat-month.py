import justpy as jp
import pandas
from datetime import datetime
from pytz import utc

# Carga los datos desde un archivo CSV y convierte la columna 'Timestamp' a formato de fecha
data = pandas.read_csv("reviews.csv", parse_dates=['Timestamp'])

# Agrega una nueva columna 'Month' que contiene el año y el mes en formato 'YYYY-MM'
data['Month'] = data['Timestamp'].dt.strftime('%Y-%m')

# Agrupa los datos por mes y calcula el promedio de las calificaciones
month_average = data.groupby('Month')['Rating'].mean()

# Definición del gráfico en formato JSON con el formato de manejo de https://www.highcharts.com/
chart_def = """
{
    chart: {
        type: 'spline',
        inverted: false
    },
    title: {
        text: 'Average Rating by Month'
    },
    subtitle: {
        text: 'According to the Course Reviews Dataset'
    },
    xAxis: {
        reversed: false,
        title: {
            enabled: true,
            text: 'Month'
        },
        labels: {
            format: '{value} km'
        },
        accessibility: {
            rangeDescription: 'Range: 0 to 80 km.'
        },
        maxPadding: 0.05,
        showLastLabel: true
    },
    yAxis: {
        title: {
            text: 'Rating'
        },
        labels: {
            format: '{value}°'
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
        pointFormat: '{point.x} km: {point.y}°C'
    },
    plotOptions: {
        spline: {
            marker: {
                enable: false
            }
        }
    },
    series: [{
        name: 'Rating',
        data: [[0, 15], [10, -50], [20, -56.5], [30, -46.5], [40, -22.1],
            [50, -2.5], [60, -27.7], [70, -55.7], [80, -76.5]]
    }]
}
"""

# Función principal que define la aplicación web
def app():
    # Crea una página Quasar, que es la base de la interfaz web
    wp = jp.QuasarPage()
    
    # Agrega un encabezado con texto centrado
    h1 = jp.QDiv(a=wp, text="Analysis of Course Reviews", classes="text-h3 text-center q-pa-md")
    
    # Agrega una descripción debajo del encabezado
    p1 = jp.QDiv(a=wp, text="These graphs represent course review analysis")
    
    # Agrega un gráfico interactivo basado en HighCharts
    hc = jp.HighCharts(a=wp, options=chart_def)
    
    # Configura los datos del gráfico
    hc.options.xAxis.categories = list(month_average.index)  # Meses en el eje X
    hc.options.series[0].data = list(month_average)  # Promedios de calificaciones en el eje Y
    
    return wp

# Ejecuta la aplicación en el puerto 8080
jp.justpy(app, port=8080)
