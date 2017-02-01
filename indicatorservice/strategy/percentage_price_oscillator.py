""" 
    The Percentage Price Oscillator (PPO) is a
    momentum oscillator that measures the difference between two moving averages as
    a percentage of the larger moving average. As with its cousin, MACD, the
    Percentage Price Oscillator is shown with a signal line, a histogram and a
    centerline. Signals are generated with signal line crossovers, centerline
    crossovers and divergences. Because these signals are no different than those
    associated with MACD, this article will focus on a few differences between the
    two. First, PPO readings are not subject to the price level of the security.
    Second, PPO readings for different securities can be compared, even when there
    are large differences in the price. See the ChartSchool article on MACD for
    information on signals common to both MACD and PPO.
"""

# Percentage Price Oscillator (PPO): {(12-day EMA - 26-day EMA)/26-day EMA} x 100

# Signal Line: 9-day EMA of PPO

# PPO Histogram: PPO - Signal Line

from __future__ import division
import csv
import operator

from exponential_moving_average import exponential_moving_average

data = []
csv_path = './indicatorservice/data/ppo.csv'
# csv_path = './indicatorservice/data/2017-01-27-ql-resources.csv'

with open(csv_path) as csvfile:
    lines = csv.DictReader(csvfile)
    for i, line in enumerate(lines):
        data.append(line)

def percentage_price_oscillator(data):
    ema12 = exponential_moving_average(data, 12)
    print ema12
    ema26 = exponential_moving_average(data, 26)
    ppos = []

    for i, j in zip(ema12, ema26):
        try:
            ppo = (float(i) - float(j)) / float(j) * 100
            ppos.append(ppo)
        except ZeroDivisionError:
            ppos.append(0)
    return ppos

for index, value in enumerate(percentage_price_oscillator(data)):
    print index + 1, value