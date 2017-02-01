"""
    Absolute True Range (ATR)

    Developed by J. Welles Wilder, the Average True Range (ATR) is an indicator
    that measures volatility. 
""" 
from __future__ import division 
import csv


data = []
csv_path = './indicatorservice/data/atr.csv'


with open(csv_path) as csvfile:
    lines = csv.DictReader(csvfile)
    for i, line in enumerate(lines):
        data.append(line)

# Relative Strength Index
def absolute_true_range(data, days=14):
    """
      Calculates the SMA for a given time period
      Envelope can be 2.5%, 5%, 10%
    """
    # Method 1: Current High less the current Low
    # Method 2: Current High less the previous Close (absolute value)
    # Method 3: Current Low less the previous Close (absolute value)
    copy = data[:]
    output = []
    atr = 0
    atrs = [max(abs(float(value['High']) - float(value['Low'])),
                abs(float(value['High']) - float(copy[index - 1]['Close'])),
                abs(float(value['Low']) - float(copy[index - 1]['Close'])))
            if index >= 1 else abs(float(value['High']) - float(value['Low']))
            for index, value in enumerate(copy)]
    for index, value in enumerate(atrs):
        if index + 1 == days:
            # get sum
            atr = sum(atrs[:days]) / days
        elif index + 1 > days:
            atr = (atr * (days - 1) + atrs[index]) / days
        else:
            atr = 0
        output.append(atr)
    return output

for index, value in enumerate(absolute_true_range(data, 14)[:100]):
    print index + 1, value
