from __future__ import division
from utils import open_csv, parse_data, make_copy, average, prev_values


csv_path = './indicatorservice/data/rsi.csv'

raw_data = parse_data(open_csv(csv_path))


# Relative Strength Index
def relative_strength_index(data, period=14):
    # Sort the data first
    rsi_list = []
    average_gain = 0
    average_loss = 0
    change = relative_change(data)

    skipped_first_value = change[1:]
    for index, value in enumerate(skipped_first_value):
        if index + 1 > period:
            positive_change = value if value > 0 else 0
            negative_change = value if value < 0 else 0
            average_gain = (average_gain*13 + positive_change) / 14
            average_loss = (average_loss*13 + abs(negative_change)) / 14
        elif index + 1 == period:
            average_gain = abs(sum([change for change in skipped_first_value[:period] 
                                    if change > 0])) / 14
            average_loss = abs(sum([change for change in skipped_first_value[:period] 
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


# Make a copy
data = make_copy(raw_data)

# Filter the close prices
close_prices = [d['close'] for d in data]

