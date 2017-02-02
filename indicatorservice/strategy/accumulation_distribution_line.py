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

# Accumulation Distribution Line (ADL)
# 1. Money Flow Multiplier = [(Close  -  Low) - (High - Close)] /(High - Low) 

# 2. Money Flow Volume = Money Flow Multiplier x Volume for the Period

# 3. ADL = Previous ADL + Current Period's Money Flow Volume

def accumulation_distribution_line(data, days=20, envelope=0.025):
    """
    """
    copy = data[:]
    adl = 0
    output = []
    for index, value in enumerate(copy):
      high = float(value['High'])
      low = float(value['Low'])
      close = float(value['Close'])
      volume = float(value['Volume'])
      money_flow_multiplier = ((close - low) - (high - close)) / (high - low)
      money_flow_volume = money_flow_multiplier * volume
      adl = adl + money_flow_volume
      output.append(adl)
    return output