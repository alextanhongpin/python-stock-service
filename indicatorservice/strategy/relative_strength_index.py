from __future__ import division
import csv
import math

data = []
csv_path = './indicatorservice/data/2017-01-27-ql-resources.csv'
csv_path = './indicatorservice/data/sample.csv'

with open(csv_path) as csvfile:
    lines = csv.DictReader(csvfile)
    for i, line in enumerate(lines):
        data.append(line)

# Relative Strength Index
def relative_strength_index(data, days=14):
    # Sort the data first
    copy = data[:]
    rsi_list = []
    average_gain = 0
    average_loss = 0
    data_with_change = [float(key['Close']) - float(copy[index - 1]['Close'])
                        for index, key in enumerate(copy)]
    skipped_first_value = data_with_change[1:]
    for index, value in enumerate(skipped_first_value):
        if index + 1 > days:
            positive_change = value if value > 0 else 0
            negative_change = value if value < 0 else 0
            average_gain = (average_gain*13 + positive_change) / 14
            average_loss = (average_loss*13 + abs(negative_change)) / 14
        elif index + 1 == days:
            average_gain = abs(sum([change for change in skipped_first_value[:days] 
                                    if change > 0])) / 14
            average_loss = abs(sum([change for change in skipped_first_value[:days] 
                                    if change < 0])) / 14
        try:
            rs = average_gain / average_loss
            rsi = 100 - 100 / (1 + rs)
            rsi_list.append(rsi)
        except ZeroDivisionError:
            rsi_list.append(0)
    return rsi_list



for i in relative_strength_index(data, 14):
    print i