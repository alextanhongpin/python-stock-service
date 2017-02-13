"""
    # NOT TESTED
    Stochastic

    %K = (Current Close - Lowest Low)/(Highest High - Lowest Low) * 100
    %D = 3-day SMA of %K

    Lowest Low = lowest low for the look-back period
    Highest High = highest high for the look-back period
    %K is multiplied by 100 to move the decimal point two places
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
def stochastic(data, days=14):
    """
    """
    # Get the %K (highest high over the past 14 days
    # and the lowest low over the past 14 days
    copy = data[:]

    percentage_ks = []
    percentage_ds = []

    for index, value in enumerate(copy):
        if index >= days:
            values = copy[index - days:index]
            highest_high = max([float(d['High']) for d in values])
            lowest_low = max([float(d['Low']) for d in values])

            percentage_k = (float(value['Close'])-lowest_low) / (highest_high - lowest_low) * 100
            percentage_ks.append(percentage_k)
        else: 
            # Exclude the first 14-days
            percentage_ks.append(0)

    for index, _ in enumerate(percentage_ks):
        if index >= 3:
            prev_values = percentage_ks[index - 3:index]
            percentage_d = sum(prev_values) / len(prev_values)
            percentage_ds.append(percentage_d)
        else:
            percentage_ds.append(0)

    return zip(percentage_ks, percentage_ds)

