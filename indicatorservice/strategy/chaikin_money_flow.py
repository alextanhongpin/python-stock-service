"""

Developed by Marc Chaikin, Chaikin Money Flow measures the amount of Money
Flow Volume over a specific period. Money Flow Volume forms the basis for the
Accumulation Distribution Line. Instead of a cumulative total of Money Flow
Volume, Chaikin Money Flow simply sums Money Flow Volume for a specific look-
back period, typically 20 or 21 days. The resulting indicator fluctuates
above/below the zero line just like an oscillator. Chartists weigh the balance
of buying or selling pressure with the absolute level of Chaikin Money Flow.
Chartists can also look for crosses above or below the zero line to identify
changes on money flow. 

"""
               
# 1. Money Flow Multiplier = [(Close  -  Low) - (High - Close)] /(High - Low) 
# 2. Money Flow Volume = Money Flow Multiplier x Volume for the Period
# 3. 20-period CMF = 20-period Sum of Money Flow Volume / 20 period Sum of Volume

from __future__ import division
import csv


data = []
csv_path = './indicatorservice/data/2017-01-27-ql-resources.csv'


with open(csv_path) as csvfile:
    lines = csv.DictReader(csvfile)
    for i, line in enumerate(lines):
        data.append(line)

def chaikin_money_flow(data, days=20, envelope=0.025):
    """
    """
    copy = data[:]
    adl = 0
    money_flow_volumes = []
    output = []
    for index, value in enumerate(copy):
      high = float(value['High'])
      low = float(value['Low'])
      close = float(value['Close'])
      volume = float(value['Volume'])
      money_flow_multiplier = ((close - low) - (high - close)) / (high - low)
      money_flow_volume = money_flow_multiplier * volume
      money_flow_volumes.append({'volume': volume, 'money_flow_volume': money_flow_volume})
    for index, value in enumerate(money_flow_volumes):
      if index + 1 >= days:
        sum_of_money_flow = sum([value['money_flow_volume'] for money_flow_volumes[index - days:index])
        sum_of_volume = sum([value['volume'] for money_flow_volumes[index - days:index])
        output.append(sum_of_money_flow / sum_of_volume)
      else: 
        output.append(0)
    return output