import justpy as jp
import pandas
from datetime import datetime
from pytz import utc
data = pandas.read_csv("reviews.csv", parse_dates=["Timestamp"])
data["Month"] = data["Timestamp"].dt.strftime("%Y-%m")
month_average = data.groupby(["Month"]).mean()

chart_def = """
{
    chart: {
        type: 'spline',
        inverted: true
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
            text: 'Temperature'
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
        name: 'Temperature',
        data: [[0, 15], [10, -50], [20, -56.5], [30, -46.5], [40, -22.1],
            [50, -2.5], [60, -27.7], [70, -55.7], [80, -76.5]]
    }]
}
"""

def app():
    wp = jp.QuasarPage()
    h3z = jp.QDiv(a=wp, text="Analysis of Course Reviews", classes="text-h3 text-center")
#    p1 = jp.QDiv(a=wp, text="The graphs represent review analysis")
    hc = jp.HighCharts(a=wp, options=chart_def)
    hc.options.title.text = "Average Rating by Month"
    hc.options.chart.inverted = False;
    hc.options.subtitle.text = "The graphs represent review analysis"
    hc.options.xAxis.labels.format = "{value}"
    x = month_average.index
    y = month_average["Rating"]
    hc.options.xAxis.categories = list(x)
    hc.options.series[0].data = list(y)
    hc.options.xAxis.title.text = "Month"
    hc.options.yAxis.title.text = "Average Rating"
    hc.options.series[0].name = "Average Rating"
    hc.options.tooltip.pointFormat = "{point.x}: {point.y}"
    """
    x = [3, 6, 8]
    y = [4, 7, 9]
    hc.options.series[0].data = list(zip(x, y))
    hc.options.series[0].data = [[3, 4], [6, 7], [8, 9]]
    """
    return wp

jp.justpy(app)
