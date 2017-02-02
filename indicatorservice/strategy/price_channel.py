"""
    SMA
"""
from __future__ import division
import csv
import operator

data = []
csv_path = './indicatorservice/data/2017-01-27-ql-resources.csv'


with open(csv_path) as csvfile:
    lines = csv.DictReader(csvfile)
    for i, line in enumerate(lines):
        data.append(line)

# Relative Strength Index
def price_channel(data, days=20):
    """
    """
    copy = data[:]
    upper_channel_line = [float(value['High']) 
                          if index >= 20 else 0
                          for index, value in enumerate(copy)]
    lower_channel_line = [float(value['Low']) 
                          if index >= 20 else 0
                          for index, value in enumerate(copy)]
    centerline = [(i+j) / 2 for i, j in zip(upper_channel_line, lower_channel_line)]
    return zip(upper_channel_line, lower_channel_line, centerline)
