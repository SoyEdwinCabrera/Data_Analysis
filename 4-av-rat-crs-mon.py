import justpy as jp
import pandas
from datetime import datetime
from pytz import utc
import matplotlib.pyplot as plt

# Carga los datos desde un archivo CSV y convierte la columna 'Timestamp' a formato de fecha
data = pandas.read_csv("reviews.csv", parse_dates=['Timestamp'])

# Agrega una nueva columna 'Month' que contiene el año y el mes en formato 'YYYY-MM'
data['Month'] = data['Timestamp'].dt.strftime('%Y-%m')

# Define las columnas numéricas que se utilizarán para el análisis
numeric_cols = ['Rating']  # Puedes agregar más columnas numéricas si es necesario

# Agrupa los datos por mes y curso, y cuenta las calificaciones
month_average_crs = data.groupby(['Month', 'Course Name'])[numeric_cols].count().unstack()

# Imprime los datos agrupados para depuración
print(month_average_crs)

# Definición del gráfico en formato JSON con el formato de manejo de https://www.highcharts.com/
chart_def = """
{
    chart: {
        type: 'spline'
    },
    title: {
        text: 'Moose and deer hunting in Norway, 2000 - 2024'
    },
    subtitle: {
        text: 'Source: <a href="https://www.ssb.no/jord-skog-jakt-og-fiskeri/jakt" target="_blank">SSB</a>'
    },
    legend: {
        layout: 'vertical',
        align: 'left',
        verticalAlign: 'top',
        x: 120,
        y: 70,
        floating: true,
        borderWidth: 1,
        backgroundColor: '#ffffff'
    },
    xAxis: {
        plotBands: [{
            from: 2020,
            to: 2023,
            color: 'rgba(68, 170, 213, .2)'
        }]
    },
    yAxis: {
        title: {
            text: 'Quantity'
        }
    },
    tooltip: {
        shared: true,
        headerFormat: '<b>Hunting season starting autumn {point.x}</b><br>'
    },
    credits: {
        enabled: false
    },
    plotOptions: {
        series: {
            pointStart: 2000
        },
        areaspline: {
            fillOpacity: 0.5
        }
    },
    series: [{
        name: 'Moose',
        data: [
            38000, 37300, 37892, 38564, 36770, 36026, 34978, 35657, 35620, 35971,
            36409, 36435, 34643, 34956, 33199, 31136, 30835, 31611, 30666, 30319,
            31766, 29278, 27487, 26007
        ]
    }, {
        name: 'Deer',
        data: [
            22534, 23599, 24533, 25195, 25896, 27635, 29173, 32646, 35686, 37709,
            39143, 36829, 35031, 36202, 35140, 33718, 37773, 42556, 43820, 46445,
            50048, 52804, 49317, 52490
        ]
    }]
}
"""

# Función principal que define la aplicación web
def app():
    # Crea una página Quasar, que es la base de la interfaz web
    wp  = jp.QuasarPage()
    
    # Agrega un encabezado con texto centrado
    jp.QDiv(a=wp, text="Average Rating by Month", classes="text-h3 text-center q-pa-md")
    
    # Agrega una descripción debajo del encabezado
    jp.QDiv(a=wp, text="These graphs represent course review analysis.")
    
    # Agrega un gráfico interactivo basado en HighCharts
    hc = jp.HighCharts(a=wp, options=chart_def)
    
    # Configura las bandas de los datos en el eje X
    hc.options.xAxis.plotBands =  list(month_average_crs.index)
    
    # Prepara los datos para el gráfico
    hc_data = [{"name": v1, "data": [v2 for v2 in month_average_crs[v1]]} for v1 in month_average_crs.columns]
    
    # Asigna los datos al gráfico
    hc.options.series = hc_data
        
    return wp

# Ejecuta la aplicación en el puerto 8080
jp.justpy(app, port=8080)
