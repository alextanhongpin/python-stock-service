from __future__ import division
from ... import open_csv, parse_data, make_copy

csv_path = './indicatorservice/data/2017-01-27-ql-resources.csv'
raw_data = parse_data(open_csv(csv_path))

def upper_envelope(sma, envelope=0.025):
  return sma + sma * envelope

def lower_envelope(sma, envelope=0.025):
  return sma - sma * envelope

def simple_moving_average(data, period=20, envelope=0.025):
    """
      Calculates the SMA for a given time period
      Envelope can be 2.5%, 5%, 10%
    """
    output = [average(prev_values(data, i, period))
              if i >= period else 0
              for i, v in data]
    return [{
              "sma": sma, 
              "upper_envelope": upper_envelope(sma, envelope), 
              "lower_envelope": lower_envelope(sma, envelope) 
            } for sma in output]


# Make a copy
data = make_copy(raw_data)

# Filter the close prices
close_prices = [d['close'] for d in data]

# Calculate the SMA
sma = simple_moving_average(close_prices)
