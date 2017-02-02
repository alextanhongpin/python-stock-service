"""

The Force Index is an indicator that uses price and volume to assess the
power behind a move or identify possible turning points. Developed by Alexander
Elder, the Force Index was introduced in his classic book, Trading for a Living.
According to Elder, there are three essential elements to a stock's price
movement: direction, extent and volume. The Force Index combines all three as an
oscillator that fluctuates in positive and negative territory as the balance of
power shifts. The Force Index can be used to reinforce the overall trend,
identify playable corrections or foreshadow reversals with divergences. 

"""

# Force Index(1) = {Close (current period)  -  Close (prior period)} x Volume
# Force Index(13) = 13-period EMA of Force Index(1)

from __future__ import division
import csv

data = []
csv_path = './indicatorservice/data/2017-01-27-ql-resources.csv'

with open(csv_path) as csvfile:
    lines = csv.DictReader(csvfile)
    for i, line in enumerate(lines):
        data.append(line)

# Relative Strength Index
def force_index(data, days=13):
    """
      Calculates the SMA for a given time period
      Envelope can be 2.5%, 5%, 10%
    """
    copy = data[:]
    force_index = [float(value.get('Close', default=0)) - float(copy[index - 1].get('Close', default=0)) * float(value.get('Volume', default=0))
     for index, value in enumerate(copy)]
    return force_index

# Completed: Force Index(1)
# TODO: Force Index(13)