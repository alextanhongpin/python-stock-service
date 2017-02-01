"""

    Keltner Channels
    ~~~~~~~~~~~~~~~~

    Keltner Channels are volatility-based envelopes set above and below an
    exponential moving average. This indicator is similar to Bollinger Bands, which
    use the standard deviation to set the bands. Instead of using the standard
    deviation, Keltner Channels use the Average True Range (ATR) to set channel
    distance. The channels are typically set two Average True Range values above and
    below the 20-day EMA. The exponential moving average dictates direction and the
    Average True Range sets channel width. Keltner Channels are a trend following
    indicator used to identify reversals with channel breakouts and channel
    direction. Channels can also be used to identify overbought and oversold levels
    when the trend is flat. 
"""

from __future__ import division
import csv
import operator

from absolute_true_range import absolute_true_range
from exponential_moving_average import exponential_moving_average

data = []
csv_path = './indicatorservice/data/ema.csv'
csv_path = './indicatorservice/data/2017-01-27-ql-resources.csv'

with open(csv_path) as csvfile:
    lines = csv.DictReader(csvfile)
    for i, line in enumerate(lines):
        data.append(line)


def keltner_channels(data):
    ema20 = exponential_moving_average(data, 20)
    atr10 = [atr * 2 for atr in absolute_true_range(data, 10)]
    upper_channel_line = map(operator.add, ema20, atr10)
    lower_channel_line = map(operator.sub, ema20, atr10)
    return zip(lower_channel_line, upper_channel_line)

for index, value in enumerate(keltner_channels(data)):
    print index + 1, value