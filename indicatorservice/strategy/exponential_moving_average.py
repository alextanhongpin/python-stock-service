"""
    EMA Calculates
"""

from __future__ import division
import csv


data = []
csv_path = './indicatorservice/data/ema.csv'

with open(csv_path) as csvfile:
    lines = csv.DictReader(csvfile)
    for i, line in enumerate(lines):
        data.append(line)

def exponential_moving_average(data, days):
    """
      Calculates the EMA for a given time period
    """
    copy = data[:]
    sma = sum([float(value['Close']) for _, value in enumerate(copy[:days])]) / days
    multiplier = ema_multiplier(days)
    ema = sma
    output = []
    for index, value in enumerate(copy):
        if index + 1 >= days:
            ema = (float(value['Close']) - ema) * multiplier + ema
            output.append(ema)
        else:
            output.append(0)
    return output

def ema_multiplier(days):
    """
      Calculates the multiplier for the EMA
      based on the time period
    """
    percentage = 2 / (days + 1)
    return percentage

for i, v in enumerate(exponential_moving_average(data, 10)):
    print i + 1, v
