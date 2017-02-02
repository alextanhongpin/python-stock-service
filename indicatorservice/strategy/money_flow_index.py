"""   

The Money Flow Index (MFI) is an oscillator that uses both price and
volume to measure buying and selling pressure. Created by Gene Quong and Avrum
Soudack, MFI is also known as volume-weighted RSI. MFI starts with the typical
price for each period. Money flow is positive when the typical price rises
(buying pressure) and negative when the typical price declines (selling
pressure). A ratio of positive and negative money flow is then plugged into an
RSI formula to create an oscillator that moves between zero and one hundred. As
a momentum oscillator tied to volume, the Money Flow Index (MFI) is best suited
to identify reversals and price extremes with a variety of signals.

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
def money_flow_index(data, days=14, envelope=0.025):
    """
      Calculates the SMA for a given time period
      Envelope can be 2.5%, 5%, 10%
    """
    copy = data[:]
    output = []
    positive = []
    negative = []
    for index, value in enumerate(copy):
      low = float(value['Low'])
      high = float(value['High'])
      close = float(value['Close'])

      value['Volume'] = float(value['Volume'])
      value['Typical Price'] = (low + high + close) / 3 
      value['Raw Money Flow'] = value['Typical Price'] * volume
      value['Change'] = value.get('Typical Price', default=0) - copy[index - 1].get('Typical Price', default=0)
      if value['Change'] > 0:
        positive.append(value['Raw Money Flow'])
        negative.append(0)
      else:
        positive.append(0)
        negative.append(value['Raw Money Flow'])
    results = []
    for index, value in enumerate(output):
        money_flow_ratio = sum(positive[index - days: index]) / sum(negative[index - days: index])
        money_flow_index = 100 - 100 / (1 + money_flow_ratio)
        results.append(money_flow_index)
    return results
