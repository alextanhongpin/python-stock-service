"""
    SMA
"""
from __future__ import division
import csv


data = []
csv_path = './indicatorservice/data/2017-01-27-ql-resources.csv'


with open(csv_path) as csvfile:
    lines = csv.DictReader(csvfile)
    for i, line in enumerate(lines):
        data.append(line)

# Relative Strength Index
def simple_moving_average(data, days=20, envelope=0.025):
    """
      Calculates the SMA for a given time period
      Envelope can be 2.5%, 5%, 10%
    """
    copy = data[:]
    closing_price = [float(value['Close']) for value in copy]
    output = [sum(closing_price[index - days:index]) 
              if index >= days else 0 
              for index, _ in enumerate(closing_price)]
    return [{"sma": sma, "upper_envelope": sma + sma * 0.025, "lower_envelope": sma - sma * 0.025} 
            for sma in output]

for index, value in enumerate(simple_moving_average(data, 20, 0.05)[:100]):
    print index + 1, value

