"""
  
  Unit-Converter
  ~~~~~~~~~~~~~~

  The Unit-Converter utils provides a set of
  common unit converters

"""

import locale

# Set the default locale to en_us
locale.setlocale(locale.LC_ALL, 'en_CA.UTF-8')

def pretty_currency(value):
    """
      pretty prints the currency
    """
    return locale.currency(value, grouping=True)

def pretty_percent(value):
    """
      pretty print the currency in, e.g. 0.0845 -> 8.45%
    """
    return "{0:.2f}%".format(value * 100)
