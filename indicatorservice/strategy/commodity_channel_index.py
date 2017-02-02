"""

Commodity Channel Index


Developed by Donald Lambert and featured in Commodities magazine in 1980, the Commodity Channel Index (CCI) is a versatile indicator that can be used to identify a new trend or warn of extreme conditions. Lambert originally developed CCI to identify cyclical turns in commodities, but the indicator can successfully applied to indices, ETFs, stocks and other securities. In general, CCI measures the current price level relative to an average price level over a given period of time. CCI is relatively high when prices are far above their average. CCI is relatively low when prices are far below their average. In this manner, CCI can be used to identify overbought and oversold levels.
"""


# CCI = (Typical Price  -  20-period SMA of TP) / (.015 x Mean Deviation)

# Typical Price (TP) = (High + Low + Close)/3

# Constant = .015

# There are four steps to calculating the Mean Deviation. First, subtract 
# the most recent 20-period average of the typical price from each period's 
# typical price. Second, take the absolute values of these numbers. Third, 
# sum the absolute values. Fourth, divide by the total number of periods (20). 


from __future__ import division
import csv

def calculate_typical_price(low, high, close):
  return (low + high + close) / 3


data = []
csv_path = './indicatorservice/data/cci.csv'

with open(csv_path) as csvfile:
    lines = csv.DictReader(csvfile)
    for i, line in enumerate(lines):
        data.append(line)

constant = 0.015
# Relative Strength Index
def commodity_channel_index(data, days=20):
    """
      Calculates the SMA for a given time period
      Envelope can be 2.5%, 5%, 10%
    """
    copy = data[:]
    output = []
    typical_prices = [calculate_typical_price(float(value['Low']), float(value['High']), float(value['Close'])) for value in copy]
    for index, value in enumerate(typical_prices):
      if index + 1 >= days:
        prev_data = typical_prices[index + 1 - days:index]
        sma20 = (sum(prev_data) + value) / days
        mean_deviation = (sum([abs(sma20 - v) for v in prev_data]) + abs(sma20 - value)) / days
        cci = (value - sma20) / (constant * mean_deviation)
        output.append(cci)
      else:
        output.append(0)
    return output

for index, value in enumerate(commodity_channel_index(data)):
  print index + 1, value