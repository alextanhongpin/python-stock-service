"""

Developed by Welles Wilder, the Parabolic SAR refers to a price-and-time-
based trading system. Wilder called this the “Parabolic Time/Price System.” SAR
stands for “stop and reverse,” which is the actual indicator used in the system.
SAR trails price as the trend extends over time. The indicator is below prices
when prices are rising and above prices when prices are falling. In this regard,
the indicator stops and reverses when the price trend reverses and breaks above
or below the indicator.

Wilder introduced the Parabolic Time/Price System in his 1978 book, New Concepts
in Technical Trading Systems. This book also includes RSI, Average True Range
(ATR), and the Directional Movement Concept (ADX). Despite being developed
before the computer age, Wilder's indicators have stood the test of time and
remain extremely popular. 

"""
from __future__ import division
import csv

data = []
csv_path = './indicatorservice/data/2017-01-27-ql-resources.csv'

with open(csv_path) as csvfile:
    lines = csv.DictReader(csvfile)
    for i, line in enumerate(lines):
        data.append(line)

# Rising SAR

# Prior SAR: The SAR value for the previous period. 

# Extreme Point (EP): The highest high of the current uptrend. 

# Acceleration Factor (AF): Starting at .02, AF increases by .02 each 
# time the extreme point makes a new high. AF can reach a maximum 
# of .20, no matter how long the uptrend extends. 

# Current SAR = Prior SAR + Prior AF(Prior EP - Prior SAR)
# 13-Apr-10 SAR = 48.28 = 48.13 + .14(49.20 - 48.13)

# The Acceleration Factor is multiplied by the difference between the 
# Extreme Point and the prior period's SAR. This is then added to the 
# prior period's SAR. Note however that SAR can never be above the
# prior two periods' lows. Should SAR be above one of those lows, use
# the lowest of the two for SAR. 


# SAR(0.02, 0.2)
ACCELERATION_FACTOR = 0.02 # The amount the acceleration factor can increase
MAXIMUM_ACCELERATION_FACTOR = 0.2 # The maximum acceleration factor

def parabolic_rising_sar(data, days=20, envelope=0.025):
    """
      Calculates the SMA for a given time period
      Envelope can be 2.5%, 5%, 10%
    """
    direction = 1 # Initial direction equals 1 (bullish)
    copy = data[:]
    output = []
    sar = 0 # stop and reverse
    ep = 0 # extreme point
    af = ACCELERATION_FACTOR # acceleration factor
    for index, value in enumerate(data):
      # Start from the second position
      if index < 2:
        # The sar value will be the recent extreme LOW/HIGH
        sar = 0
        ep = max(value['High'], ep)
      else:
        prev1_low = data[index - 1]['Low']
        prev2_low = data[index - 2]['Low']
        # SAR value must be lower than the prior
        # two periods low
        max_sar = min(prev1_low, prev2_low)
        ep = max(value['High'], ep)
        ep_minus_sar = ep - sar
        af = af + 0.02 if value['High'] > ep else af
        sar = min(max(sar + af * (ep_minus_sar), 0.2), max_sar)
      output.append(sar)
    

    
for index, value in enumerate(parabolic_sar(data, 20, 0.05)[:100]):
    print index + 1, value





# Falling SAR

# Prior SAR: The SAR value for the previous period. 

# Extreme Point (EP): The lowest low of the current downtrend. 

# Acceleration Factor (AF): Starting at .02, AF increases by .02 each 
# time the extreme point makes a new low. AF can reach a maximum
# of .20, no matter how long the downtrend extends. 

# Current SAR = Prior SAR - Prior AF(Prior SAR - Prior EP)
# 9-Feb-10 SAR = 43.56 = 43.84 - .16(43.84 - 42.07)

# The Acceleration Factor is multiplied by the difference between the 
# Prior period's SAR and the Extreme Point. This is then subtracted 
# from the prior period's SAR. Note however that SAR can never be
# below the prior two periods' highs. Should SAR be below one of
# those highs, use the highest of the two for SAR. 
