import justpy as jp
import pandas
from datetime import datetime
from pytz import utc
import matplotlib.pyplot as plt

data = pandas.read_csv("reviews.csv", parse_dates=['Timestamp'])
share = data.groupby(['Course Name'])['Rating'].count()

print("Contenido de 'share':")
print(share)

chart_def = """
{
    chart: {
        type: 'pie',
        zooming: {
            type: 'xy'
        },
        panning: {
            enabled: true,
            type: 'xy'
        },
        panKey: 'shift'
    },
    title: {
        text: 'Course Ratings Distribution'
    },
    tooltip: {
        valueSuffix: '%'
    },
    subtitle: {
        text: 'Source: Course Reviews Dataset'
    },
    plotOptions: {
        pie: {
            allowPointSelect: true,
            cursor: 'pointer',
            dataLabels: [{
                enabled: true,
                distance: 20
            }, {
                enabled: true,
                distance: -40,
                format: '{point.percentage:.1f}%',
                style: {
                    fontSize: '1.2em',
                    textOutline: 'none',
                    opacity: 0.7
                },
                filter: {
                    operator: '>',
                    property: 'percentage',
                    value: 10
                }
            }]
        }
    },
    series: [
        {
            name: 'Percentage',
            colorByPoint: true,
            data: []
        }
    ]
}
"""

def app():
    wp = jp.QuasarPage()
    jp.QDiv(a=wp, text="Analysis of Course Reviews", classes="text-h3 text-center q-pa-md")
    jp.QDiv(a=wp, text="These graphs represent course review analysis", classes="text-h4 text-center q-pa-md")
    
    hc = jp.HighCharts(a=wp, options=chart_def)
    hc_data = [{"name": v1, "y": int(v2)} for v1, v2 in zip(share.index, share.values)]
    print("Datos para el gráfico:")
    print(hc_data)
    hc.options.series[0].data = hc_data
    print("Configuración del gráfico:")
    print(hc.options.series[0].data)
    
    return wp
    
jp.justpy(app, port=8080)
