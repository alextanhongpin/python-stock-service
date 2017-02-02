"""

%R = (Highest High - Close)/(Highest High - Lowest Low) * -100

Lowest Low = lowest low for the look-back period
Highest High = highest high for the look-back period
%R is multiplied by -100 correct the inversion and move the decimal.

"""

from __future__ import division
import csv


data = []
csv_path = './indicatorservice/data/percentr.csv'


with open(csv_path) as csvfile:
    lines = csv.DictReader(csvfile)
    for i, line in enumerate(lines):
        data.append(line)

# Relative Strength Index
def williams(data, days=14):
    """
      Calculates the SMA for a given time period
      Envelope can be 2.5%, 5%, 10%
    """
    copy = data[:]
    output = []
    for index, value in enumerate(copy):
      if index + 1 >= days:
        prev_data = copy[index + 1 - days:index]
        highest_high = max(max([float(v['High']) for v in prev_data]), float(value['High']))
        lowest_low = min(min([float(v[' Low']) for v in prev_data]), float(value[' Low']))
        close = float(value['Current Close'])
        percent_r = (highest_high - close) / (highest_high - lowest_low) * -100
        output.append(percent_r)
      else:
        output.append(0)
    return output

for index, value in enumerate(williams(data, 14)):
    print index + 1, value

