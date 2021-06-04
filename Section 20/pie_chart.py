from datetime import datetime
import pandas
from pytz import utc
import justpy as jp

data = pandas.read_csv("reviews.csv", parse_dates=["Timestamp"])
share = data.groupby(["Course Name"])["Rating"].count()

contents = """
{
    chart: {
        plotBackgroundColor: null,
        plotBorderWidth: null,
        plotShadow: false,
        type: 'pie'
    },
    title: {
        text: 'Browser market shares in January, 2018'
    },
    tooltip: {
        pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
    },
    accessibility: {
        point: {
            valueSuffix: '%'
        }
    },
    plotOptions: {
        pie: {
            allowPointSelect: true,
            cursor: 'pointer',
            dataLabels: {
                enabled: true,
                format: '<b>{point.name}</b>: {point.percentage:.1f} %'
            }
        }
    },
    series: [{
        name: 'Brands',
        colorByPoint: true,
        data: [{
            name: 'Chrome',
            y: 61.41,
            sliced: true,
            selected: true
        }, {
            name: 'Internet Explorer',
            y: 11.84
        }, {
            name: 'Firefox',
            y: 10.85
        }, {
            name: 'Edge',
            y: 4.67
        }, {
            name: 'Safari',
            y: 4.18
        }, {
            name: 'Sogou Explorer',
            y: 1.64
        }, {
            name: 'Opera',
            y: 1.6
        }, {
            name: 'QQ',
            y: 1.2
        }, {
            name: 'Other',
            y: 2.61
        }]
    }]
}
"""

def app():
    wp = jp.QuasarPage()
    hc = jp.HighCharts(a=wp, options=contents)
    total = 0
    for i in share:
        total += i
    percent = []
    for i in range(len(share)):
        percent.append(share[i] * 100 / total)
    hc.options.series[0].data = []
    names = share.index
    for i in range(len(percent)):        
        d = {"name" : names[i], "y" : percent[i]}
        hc.options.series[0].data.append(d)
    hc.options.title.text = "Percent ratings for each course"
    return wp

jp.justpy(app)
