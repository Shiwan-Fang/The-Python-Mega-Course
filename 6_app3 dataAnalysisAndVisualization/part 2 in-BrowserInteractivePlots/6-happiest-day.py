# search Highcharts documentation, find the chart you want to use, paste the code in chart_def (needs vpn)
# you can edit the code directly about the style
import justpy as jp

import pandas
from datetime import datetime
from pytz import utc
import matplotlib.pyplot as plt

data = pandas.read_csv(
    "6_app3 dataAnalysisAndVisualization/part 1 intro/reviews.csv", parse_dates=["Timestamp"])
data['Weekday'] = data['Timestamp'].dt.strftime('%A') #A代表weekday，显示的是Monday这种单词
data['Daynumber'] = data['Timestamp'].dt.strftime('%w') #Daynumber这列都是星期几对应的数字，显示的是1、2。。。跟上面一种比得到的值不一样

weekday_average = data.groupby(['Weekday','Daynumber']).mean()
weekday_average = weekday_average.sort_values('Daynumber')

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
            text: 'Date'
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
        pointFormat: '{point.x}{point.y}'
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
        data: [[0, 15], [10, -50], [20, -56.5], [30, -46.5], [40, -22.1],
            [50, -2.5], [60, -27.7], [70, -55.7], [80, -76.5]]
    }]
}
"""


def app():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a=wp, text="Analysis of Course Reviews",
                 classes="text-h3 text-center q-pa-md")
    pi = jp.QDiv(a=wp, text="These graphs reprensent course review analysis")
    hc = jp.HighCharts(a=wp, options=chart_def)
    # python read chart_def as dictionary,try to print hc.options,we can access the dictionaries through options
    # you can change everything from chart_def
    hc.options.title.text = "Average Rating by Day"

    hc.options.xAxis.categories = list(weekday_average.index)
    hc.options.series[0].data = list(weekday_average['Rating'])

    return wp


jp.justpy(app)
