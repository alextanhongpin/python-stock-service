
from __future__ import division
import math

class Calculator:
  def __init__(self, brokerage_fee, minimum_brokerage_fee, clearing_fee, stamp_duty, tax_rate):
    self.units = units
    self.brokerage_fee = brokerage_fee
    self.minimum_brokerage_fee = minimum_brokerage_fee
    self.clearing_fee = clearing_fee
    self.stamp_duty = stamp_duty
    self.tax_rate = tax_rate
  def brokerage_fee(self, units, price_per_unit):
    """
      Calculates the brokerage fee
    """
    purchased_price = price_per_unit * units
    calculated_fee = self.brokerage_fee / 100 * purchased_price
    # Take the lowest fee
    brokerage_fee = max([calculated_fee, self.minimum_brokerage_fee])
    return brokerage_fee
  def clearing_fee (self, units, price_per_unit):
    """
      Calculate the clearing fee
    """
    output = self.clearing_fee / 100 * units * price_per_unit
    return math.ceil(output*100) / 100
  def stamp_duty(self, units, price_per_unit):
    """
      Calculate the stamp duty
    """
    return math.ceil(self.stamp_duty * units * price_per_unit)
  def total_brokerage_fee(self, units, price_per_unit):
    return self.brokerage_fee(units, price_per_unit) + self.clearing_fee(units, price_per_unit)
  def gst_tax(self, units, price_per_unit):
    """
      Calculate the after tax price
    """
    return math.ceil(self.tax_rate * self.total_brokerage_fee(units, price_per_unit)*100) / 100
  def total_fee(self, units, price_per_unit):
    """
      Calculates the broke
    """
    brokerage_fee = self.brokerage_fee(units, price_per_unit)
    clearing_fee = self.clearing_fee(units, price_per_unit)
    stamp_duty = self.stamp_duty(units, price_per_unit)
    gst_tax = self.gst_tax(units, price_per_unit)
    return brokerage_fee + clearing_fee + stamp_duty + gst_tax
  def gross_amount(self, units, price_per_unit):
    """
      The gross purchase price does not include
      the tax or brokerage fee
    """
    return units * price_per_unit
  def net_purchase_price(self, units, price_per_unit):
    gross_amount = self.gross_amount(units, price_per_unit)
    total_fee = self.total_fee(units, price_per_unit)
    return gross_amount + total_fee
  def net_sell_price(self, units, price_per_unit):
    """
      Calculate the final sell price 
    """
    gross_amount = self.gross_amount(units, price_per_unit)
    total_fee = self.total_fee(units, price_per_unit)
    return gross_amount - total_fee
  def profit_or_losses(self, units, price_per_unit_buy, price_per_unit_sell):
    """
      Calculate the profit or loss gain
      by selling the stock at the given price
    """
    net_sell_price = self.net_sell_price(units, price_per_unit_sell)
    net_purchase_price = self.net_purchase_price(units, price_per_unit_buy)
    return net_sell_price - net_purchase_price
  def profit_or_losses_percent(self, units, price_per_unit_buy, price_per_unit_sell):
    """
      Calculate the profit or loss gain
      by selling the stock at the given price
    """
    net_sell_price = self.net_sell_price(units, price_per_unit_sell)
    net_purchase_price = self.net_purchase_price(units, price_per_unit_buy)
    return (net_sell_price - net_purchase_price) / net_purchase_price * 100
  def minimum_units_for_brokerage(self, price_per_unit):
    """
      Calculates the number of units that needs to be purchased
      in order to exceed the minimum brokerage value
    """
    return math.ceil(self.minimum_brokerage_fee / price_per_unit * 100 / self.brokerage_fee)
    def lowest_price_for_brokerage(self, units):
    """
      Calculates the minimum price that needs to be paid
      in order to achieve the minimum brokerage price
    """
    return math.ceil(self.minimum_brokerage_fee / units * 100 / self.brokerage_fee * 100) / 100
  def minimum_sell_price(self, units, price_per_unit_buy):
    """
      Calculates the minimum cost of the sell
      price per unit in order to gain a profit
    """
    if price_per_unit_buy > self.lowest_price_for_brokerage(units):
      price = net_purchase_price / units
      diff = 1 - (0.42 / 100 + 0.03 / 100 + 1 / 1000 + 6 / 100 * (0.42 / 100 + 0.03 / 100))
      return math.ceil(price / diff * 100) / 100
    else: 
      price = (net_purchase_price + 12 + (6 / 100 * 12)) / units
      diff = 1 - (0.03 / 100 + 1 / 1000 + 6 / 100 * (0.03 / 100))
      return math.ceil(price / diff * 100) / 100
  def projected_values(self):
    """
      Calculates a list of projected values and
      the corresponding loss/gain
    """
    return None

brokerage_fee = 0.42
minimum_brokerage_fee = 12
clearing_fee = 0.03stamp_duty
stamp_duty = 1 / 1000
tax_rate = 0.06

units = 900
buy_price = 5.05
sell_price = 5.04

calculator = Calculator(brokerage_fee, minimum_brokerage_fee, clearing_fee, stamp_duty, tax_rate)

print 'minimum sell price', calculator.minimum_sell_price(units, buy_price)

# purchase_brokerage_fee = calculator.brokerage_fee(12, units, buy_price, 0.42)
# purchase_clearing_fee = calculator.clearing_fee (units, buy_price, 0.03)
# purchase_stamp_duty = calculator.stamp_duty(units, buy_price, 0.001)
# purchase_gst_tax = calculator.gst_tax(purchase_brokerage_fee + purchase_clearing_fee)
# gross_purchase_amount = calculator.gross_amount(units, buy_price)
# total_purchase_fee = purchase_brokerage_fee + purchase_clearing_fee + purchase_stamp_duty + purchase_gst_tax
# net_purchase_price = gross_purchase_amount + total_purchase_fee 
# print 'gross_purchase_amount', gross_purchase_amount

# print 'purchase_brokerage_fee fee:', purchase_brokerage_fee
# print 'purchase_clearing_fee:', purchase_clearing_fee
# print 'purchase_stamp_duty:', purchase_stamp_duty
# print 'gst_tax', purchase_gst_tax
# print 'total_purchase_fee', total_purchase_fee
# print 'net_purchase_price', net_purchase_price

# sell_brokerage_fee = calculator.brokerage_fee(12, units, sell_price, 0.42)
# sell_clearing_fee = calculator.clearing_fee (units, sell_price, 0.03)
# sell_stamp_duty = calculator.stamp_duty(units, sell_price, 0.001)
# sell_gst_tax = calculator.gst_tax(sell_brokerage_fee + sell_clearing_fee)
# gross_sell_amount = calculator.gross_amount(units, sell_price)
# total_sell_fee = sell_brokerage_fee + sell_clearing_fee + sell_stamp_duty + sell_gst_tax
# net_sell_price = gross_sell_amount - total_purchase_fee

# print '\n'
# print 'gross_sell_amount', gross_sell_amount
# print 'sell_brokerage_fee:', sell_brokerage_fee
# print 'sell_clearing_fee:', sell_clearing_fee
# print 'sell_stamp_duty:', sell_stamp_duty
# print 'sell_gst_tax:', sell_gst_tax
# print 'total_sell_fee', total_sell_fee
# print 'net_sell_price', net_sell_price

# profit_loss = net_sell_price - net_purchase_price
# print 'profit/loss:', math.ceil(profit_loss*100) / 100
# print '% profit:', math.ceil(profit_loss / net_purchase_price * 100 * 100) / 100

# lowest_entry_price = 12 / units * 100 / 0.42
# print 'lowest_entry_price', lowest_entry_price

# if buy_price > lowest_entry_price:
#   print 'exceeded brokerage fee of MYR 12'
#   price = net_purchase_price / units
#   diff = 1 - (0.42 / 100 + 0.03 / 100 + 1 / 1000 + 6 / 100 * (0.42 / 100 + 0.03 / 100))
#   print 'minimum sell price is MYR', math.ceil(price / diff * 100) / 100
# else:
#   print 'did not exceed brokerage fee'
#   price = (net_purchase_price + 12 + (6 / 100 * 12)) / units
#   diff = 1 - (0.03 / 100 + 1 / 1000 + 6 / 100 * (0.03 / 100))
#   print 'minimum sell price is MYR', math.ceil(price / diff * 100) / 100
