from __future__ import division
import csv

# Open a CSV file
def open_csv(filename):
    data = []
    with open(filename) as csvfile:
        rows = csv.DictReader(csvfile)
        for _, row in enumerate(rows):
            data.append(row)
        return data

# Parse the data
def parse_data(data):
    output = []
    for _, item in enumerate(data):
        d = {}
        # newdata['date'] = float(data.get('Date', 0))
        d['open'] = float(item.get('Open', 0))
        d['open'] = float(item.get('Open', 0))
        d['high'] = float(item.get('High', 0))
        d['low'] = float(item.get('Low', 0))
        d['close'] = float(item.get('Close', 0))
        d['volume'] = float(item.get('Volume', 0))
        output.append(d)
    return output

# Average
def average(data):
    try:
        return sum(data) / len(data)
    except ZeroDivisionError:
        return 0

def relative_change(data):
    return [d[i] - d[i - 1] for i, v in enumerate(data)]

# Prev values
def prev_values(data, index, period):
    diff = index + 1 - period
    if diff >= 0:
        return data[diff:index + 1]
    else:
        return [0]

def make_copy(data):
  return data[:]
