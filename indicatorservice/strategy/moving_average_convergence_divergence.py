"""
Developed by Gerald Appel in the late seventies, the Moving Average
Convergence/Divergence oscillator (MACD) is one of the simplest and most
effective momentum indicators available. The MACD turns two trend-following
indicators, moving averages, into a momentum oscillator by subtracting the
longer moving average from the shorter moving average. As a result, the MACD
offers the best of both worlds: trend following and momentum. The MACD
fluctuates above and below the zero line as the moving averages converge, cross
and diverge. Traders can look for signal line crossovers, centerline crossovers
and divergences to generate signals. Because the MACD is unbounded, it is not
particularly useful for identifying overbought and oversold levels.
"""

# MACD Line: (12-day EMA - 26-day EMA)

# Signal Line: 9-day EMA of MACD Line

# MACD Histogram: MACD Line - Signal Line


from __future__ import division
import csv
from exponential_moving_average import exponential_moving_average

data = []
csv_path = './indicatorservice/data/2017-01-27-ql-resources.csv'

with open(csv_path) as csvfile:
    lines = csv.DictReader(csvfile)
    for i, line in enumerate(lines):
        data.append(line)

# Relative Strength Index
def moving_average_convergence_divergence(data, days=20, envelope=0.025):
    """
    """
    copy = data[:]
    ema12 = exponential_moving_average(data, 12)
    ema26 = exponential_moving_average(data, 26)
    macd_line = map(operator.sub, ema12, ema26)
    signal_line = exponential_moving_average(data, 9)
    macd_histogram = map(operator.sub, macd_line, signal_line)
    return macd_histogram

