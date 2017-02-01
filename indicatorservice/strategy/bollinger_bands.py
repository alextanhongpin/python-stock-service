# Middle Band = 20-day simple moving average (SMA)
# * Upper Band = 20-day SMA + (20-day standard deviation of price x 2) 
# * Lower Band = 20-day SMA - (20-day standard deviation of price x 2)

from __future__ import division
import csv
import statistics

from simple_moving_average import simple_moving_average

data = []
csv_path = './indicatorservice/data/2017-01-27-ql-resources.csv'


with open(csv_path) as csvfile:
    lines = csv.DictReader(csvfile)
    for i, line in enumerate(lines):
        data.append(line)

def standard_deviation(data, days=20):
    return [statistics.stdev(data[index-20:index])
     if index >= 20 else 0
     for index, _ in enumerate(data)]

def bollinger_bands(data, days=20, multiplier=2):
    sma20 = simple_moving_average(data, 20)
    stddev20 = standard_deviation(data, 20)
    return[(i, i + j * multiplier, i - j * multiplier)
           for i, j in zip(sma20, stddev20)]